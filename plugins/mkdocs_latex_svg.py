from __future__ import annotations

import hashlib
import html
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options as c


LATEX_BLOCK_RE = re.compile(
    r"^(?P<indent>[ \t]*)```latex(?:\s*\{(?P<opts>[^}]*)\})?\s*\n"
    r"(?P<body>.*?\n)"
    r"^(?P=indent)```\s*$",
    re.DOTALL | re.MULTILINE,
)
OPT_RE = re.compile(r"(?P<k>[a-zA-Z_]\w*)\s*=\s*(?P<v>[^\s]+)")
SVG_TAG_RE = re.compile(r"<svg\b[^>]*>.*?</svg>", re.DOTALL | re.IGNORECASE)
SVG_OPEN_RE = re.compile(r"<svg\b([^>]*)>", re.IGNORECASE)
WH_RE = re.compile(r'\b(width|height)="([^"]+)"')
ID_RE = re.compile(r'\bid="([^"]+)"')
P_WRAPPED_LATEX_BLOCK_RE = re.compile(
    r"<p>\s*"
    r"(?P<block>"
    r"<div class='latex-svg-block'>"
    r"<div class='latex-svg-inner'>.*?</div>"
    r"(?:\s*<details>.*?</details>)?"
    r"\s*</div>"
    r")\s*</p>",
    re.DOTALL,
)


@dataclass
class LatexOpts:
    hide: bool = False
    latex_zoom: str = "100%"
    cmd: bool | None = None
    raw_opts: dict[str, str] = field(default_factory=dict)


def _as_bool(value: str) -> bool:
    return value.lower() in ("1", "true", "yes", "on")


def parse_opts(s: str | None) -> LatexOpts:
    opts = LatexOpts()
    if not s:
        return opts

    for m in OPT_RE.finditer(s):
        k = m.group("k")
        v = m.group("v")
        opts.raw_opts[k] = v

    if "hide" in opts.raw_opts:
        opts.hide = _as_bool(opts.raw_opts["hide"])

    if "latex_zoom" in opts.raw_opts:
        opts.latex_zoom = opts.raw_opts["latex_zoom"]

    if "cmd" in opts.raw_opts:
        opts.cmd = _as_bool(opts.raw_opts["cmd"])

    return opts


def _scale_len(val: str, scale: float) -> str:
    m = re.match(r"^\s*([0-9]*\.?[0-9]+)\s*([a-zA-Z%]*)\s*$", val)
    if not m:
        return val
    num = float(m.group(1)) * scale
    unit = m.group(2)
    num_str = f"{num:.4f}".rstrip("0").rstrip(".")
    return f"{num_str}{unit}"


def _prefix_svg_ids(svg: str, prefix: str) -> str:
    if not prefix:
        return svg

    seen: set[str] = set()
    ids: list[str] = []
    for m in ID_RE.finditer(svg):
        old = m.group(1)
        if old in seen:
            continue
        seen.add(old)
        ids.append(old)

    for old in ids:
        new = f"{prefix}{old}"
        svg = re.sub(
            rf'(\bid="){re.escape(old)}(")',
            lambda mm: f'{mm.group(1)}{new}{mm.group(2)}',
            svg,
        )
        svg = re.sub(
            rf'(xlink:href="#){re.escape(old)}(")',
            lambda mm: f'{mm.group(1)}{new}{mm.group(2)}',
            svg,
        )
        svg = re.sub(
            rf'(\bhref="#){re.escape(old)}(")',
            lambda mm: f'{mm.group(1)}{new}{mm.group(2)}',
            svg,
        )
        svg = re.sub(
            rf'(url\(#){re.escape(old)}(\))',
            lambda mm: f'{mm.group(1)}{new}{mm.group(2)}',
            svg,
        )
    return svg


def read_svg_inline(svg_path: Path, scale: float = 1.0, id_prefix: str = "") -> str:
    s = svg_path.read_text(encoding="utf-8", errors="replace")
    m = SVG_TAG_RE.search(s)
    if not m:
        return s.strip()

    svg = m.group(0).strip()

    svg = _prefix_svg_ids(svg, id_prefix)

    if abs(scale - 1.0) < 1e-9:
        # Keep inline SVG on one logical line to avoid markdown inserting <br />.
        return " ".join(svg.split())

    m2 = SVG_OPEN_RE.search(svg)
    if not m2:
        return svg

    attrs = m2.group(1)

    def repl_wh(mm):
        key = mm.group(1)
        val = mm.group(2)
        return f'{key}="{_scale_len(val, scale)}"'

    new_attrs = WH_RE.sub(repl_wh, attrs)

    new_svg = svg[:m2.start()] + f"<svg{new_attrs}>" + svg[m2.end():]
    return " ".join(new_svg.split())


def strip_indent(text: str, indent: str) -> str:
    if not indent:
        return text
    lines = text.splitlines(True)
    out = []
    for ln in lines:
        if ln.startswith(indent):
            out.append(ln[len(indent):])
        else:
            out.append(ln)
    return "".join(out)


def reindent_block(s: str, indent: str) -> str:
    if not indent:
        return "\n\n" + s.strip() + "\n\n"

    lines = s.strip().splitlines()
    out = [indent + ln if ln else indent for ln in lines]
    # Keep block HTML as a standalone block even inside nested contexts.
    return "\n\n" + "\n".join(out) + "\n\n"


def run(cmd: list[str], cwd: Path) -> None:
    p = subprocess.run(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )

    if p.returncode != 0:
        raise RuntimeError(
            f"Command failed: {cmd}\n"
            f"cwd: {cwd}\n"
            f"--- stdout ---\n{p.stdout}\n"
            f"--- stderr ---\n{p.stderr}\n"
        )


def zoom_to_scale(z: str) -> float:
    try:
        if z.endswith("%"):
            return float(z[:-1]) / 100.0
        return float(z)
    except ValueError:
        return 1.0


class LatexSvgPlugin(BasePlugin):

    config_scheme = (
        ("enabled", c.Type(bool, default=True)),
        ("gen_dir", c.Type(str, default="_gen_latex_svg")),
        ("strict_cmd", c.Type(bool, default=False)),
        ("latexmk_args", c.Type(list, default=[
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-silent"
        ])),
        ("pdf2svg_args", c.Type(list, default=[])),
    )

    def on_config(self, config):

        self.enabled = self.config["enabled"]
        self.gen_dir = self.config["gen_dir"]
        self.strict_cmd = self.config["strict_cmd"]
        self.latexmk_args = self.config["latexmk_args"]
        self.pdf2svg_args = self.config["pdf2svg_args"]

        self.docs_dir = Path(config["docs_dir"]).resolve()
        self.project_root = self.docs_dir.parent.resolve()

        self.out_dir = (self.docs_dir / self.gen_dir).resolve()
        self.out_dir.mkdir(parents=True, exist_ok=True)

        return config

    def on_page_markdown(self, markdown, page, config, files):

        if not self.enabled:
            return markdown

        def repl(m: re.Match[str]) -> str:

            indent = m.group("indent") or ""
            opts = parse_opts(m.group("opts"))
            body = strip_indent(m.group("body"), indent)

            if opts.cmd and self.strict_cmd:
                raise RuntimeError("cmd=true is not allowed")

            if "\\documentclass" not in body or "\\end{document}" not in body:
                raise RuntimeError(
                    "latex block must contain a full LaTeX document "
                    "(\\documentclass ... \\end{document})"
                )

            tex = body

            key_material = tex
            h = hashlib.sha256(key_material.encode()).hexdigest()[:16]

            svg_rel = f"{self.gen_dir}/{h}.svg"
            svg_path = self.docs_dir / svg_rel

            if not svg_path.exists():
                self._build_svg(tex, h)

            scale = zoom_to_scale(opts.latex_zoom)

            inline_svg = read_svg_inline(svg_path, scale=scale, id_prefix=f"dm-{h}-")

            img_html = (
                "<div class='latex-svg-block'>"
                f"<div class='latex-svg-inner'>{inline_svg}</div>"
                "</div>"
            )

            if opts.hide:
                return reindent_block(img_html, indent)

            src = html.escape(body)

            html = (
                "<div class='latex-svg-block'>"
                f"{img_html}"
                "<details>"
                "<summary>LaTeX source</summary>"
                f"<pre><code>{src}</code></pre>"
                "</details>"
                "</div>"
            )

            return reindent_block(html, indent)

        return LATEX_BLOCK_RE.sub(repl, markdown)

    def on_page_content(self, html, page, config, files):
        # callouts/def_list + nl2br can wrap block HTML into <p>...</p>,
        # which yields invalid markup and can break SVG rendering.
        return P_WRAPPED_LATEX_BLOCK_RE.sub(lambda m: m.group("block"), html)

    def _build_svg(self, tex: str, h: str):

        for cmd in ("latexmk", "pdf2svg"):
            if shutil.which(cmd) is None:
                raise RuntimeError(
                    f"Required command '{cmd}' not found in PATH while building LaTeX SVG"
                )

        work = self.out_dir / f"work_{h}"
        work.mkdir(parents=True, exist_ok=True)

        tex_path = work / "main.tex"
        pdf_path = work / "main.pdf"
        svg_path = self.out_dir / f"{h}.svg"

        tex_path.write_text(tex, encoding="utf-8")

        cmd = [
            "latexmk",
            *self.latexmk_args,
            f"-outdir={work}",
            str(tex_path),
        ]

        run(cmd, cwd=self.project_root)

        if not pdf_path.exists():
            raise RuntimeError("latexmk did not produce PDF")

        cmd = ["pdf2svg", str(pdf_path), str(svg_path), *self.pdf2svg_args]

        run(cmd, cwd=work)

        if not svg_path.exists():
            raise RuntimeError("pdf2svg failed")
