from __future__ import annotations

import re

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin


CALLOUT_START = re.compile(
    r'^(?P<indent>[ \t]*)>\s*\[!(?P<kind>[A-Za-z][A-Za-z0-9_-]*)\](?P<fold>[+-]?)\s*(?P<title>.*)$'
)
BQ_LINE = re.compile(r'^(?P<indent>[ \t]*)>\s?(?P<text>.*)$')
TITLE_LINE_RE = re.compile(r"^\*\*.+\*\*\s*$")


def _to_def_list(
    title_line: str, cls: str, number_within: str, body_lines: list[str], fold: str = ""
) -> str:
    body = "\n".join(body_lines).rstrip("\n")
    if body.strip() == "":
        body = ""

    dd = []
    for ln in body.splitlines():
        if ln.strip() == "":
            dd.append("")
        else:
            dd.append("    " + ln)

    dd_text = "\n".join(dd).rstrip("\n")

    dt_classes = [f".{cls}", f".within-{number_within}"]
    if fold == "+":
        dt_classes.extend([".dm-callout-collapsible", ".dm-callout-open"])
    elif fold == "-":
        dt_classes.extend([".dm-callout-collapsible", ".dm-callout-closed"])

    dt = f"{title_line} " + "{" + " ".join(dt_classes) + "}"
    dt = dt.rstrip()
    if dd_text:
        return f"{dt}\n:   \n{dd_text}\n"
    else:
        return f"{dt}\n:   \n"

class CalloutsPlugin(BasePlugin):
    config_scheme = (
        (
            "number_within",
            c.Choice(("section", "subsection", "subsubsection", "none"), default="section"),
        ),
    )

    def on_page_markdown(self, markdown, page, config, files):
        number_within = self.config.get("number_within", "section")
        lines = markdown.splitlines()
        out = []
        i = 0
        n = len(lines)

        while i < n:
            m = CALLOUT_START.match(lines[i])
            if not m:
                out.append(lines[i])
                i += 1
                continue

            indent = m.group("indent") or ""
            kind = m.group("kind")
            cls = kind.lower()
            fold = m.group("fold") or ""

            block = []
            i += 1
            while i < n:
                # If another callout starts at the same nesting level, stop here
                # so consecutive callouts are parsed as separate blocks.
                next_callout = CALLOUT_START.match(lines[i])
                if next_callout and (next_callout.group("indent") or "") == indent:
                    break
                mm = BQ_LINE.match(lines[i])
                if not mm:
                    break
                if (mm.group("indent") or "") != indent:
                    break
                block.append(mm.group("text"))
                i += 1

            while block and block[0].strip() == "":
                block.pop(0)

            title = m.group("title").strip()
            body = block

            if not title:
                if body:
                    if TITLE_LINE_RE.match(body[0].strip()):
                        title = body[0].strip()
                        body = body[1:]
                    while body and body[0].strip() == "":
                        body.pop(0)
                if not title:
                    # Keep the definition-list term non-empty while rendering no title text.
                    title = "<span class='dm-empty-title'></span>"

            converted = _to_def_list(title, cls, number_within, body, fold=fold)

            conv_lines = converted.rstrip("\n").splitlines()
            for ln in conv_lines:
                out.append(indent + ln if ln else indent)
            out.append("")
            # Python-Markdown's def_list merges adjacent terms into one <dl>.
            # Insert a neutral block HTML separator only between consecutive
            # callouts at the same indentation to force independent <dl> blocks.
            j = i
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n:
                nm = CALLOUT_START.match(lines[j])
                if nm and (nm.group("indent") or "") == indent:
                    out.append(indent + "<div class='dm-callout-split'></div>")
                    out.append("")
        return "\n".join(out) + "\n"
