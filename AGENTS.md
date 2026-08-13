# AGENTS.md — deepmath

## Project overview

- This repository publishes Japanese mathematics notes with MkDocs Material.
- Author markdown under `docs/` and source styles under `docs/assets/scss/`.
- `site/` is generated output. Do not edit it directly; rebuild it instead.
- Custom MkDocs plugins live in `plugins/` and are registered in `pyproject.toml` under `[project.entry-points."mkdocs.plugins"]`.

## Commands and environment

- Use `uv` for every Python command. Run Python as `uv run ...`; never invoke `python` or `python3` directly unless the user explicitly requests it.
- Synchronize the environment after changing `pyproject.toml` or `uv.lock` with `uv sync`.
- Validate documentation changes with `uv run mkdocs build`.
- Rebuild the stylesheet with `npm run build:css` after changing `docs/assets/scss/extra.scss`. The `css-build` MkDocs plugin is disabled by default, so a normal MkDocs build does not run this command.
- When modifying a custom plugin or its registration, run `uv sync` before the MkDocs build so the editable project is reinstalled and entry points are refreshed.

## Documentation conventions

- Preserve the existing Japanese writing style and the terminology used by adjacent notes.
- Keep Markdown source in `docs/`; use repository-relative links that work in the generated site.
- When moving, renaming, or broadly restructuring pages, update `mkdocs.yml`, index pages, and inbound links consistently.
- Keep blank lines around headings, lists, tables, and fenced code blocks. Preserve any formatting constraints specified by the user.
- For formulas, follow the MathJax and fenced-math conventions already used in the surrounding page. Do not add a second math-rendering pipeline without a clear need.

## Custom MkDocs plugins

- Keep plugin configuration schemas and corresponding `mkdocs.yml` options in sync.
- Make plugin behavior deterministic and report failures with actionable context (command, working directory, stdout, and stderr where applicable).
- Do not silently skip a requested build step or external command; honor its configured `enabled`/strictness option.
- Test plugin changes with `uv run mkdocs build`. If a change requires LaTeX SVG generation, also verify the relevant `latexmk`/`pdf2svg` path when those tools are available.

## PDF work

- For PDF inspection, use `pdftotext` from `poppler-utils` first.
- If structured extraction is necessary, use Python libraries through `uv run`.
- Write temporary extraction artifacts under `/tmp` unless the user asks to retain them.
- Map PDF-derived edits back to concrete Markdown files and sections.
- If extraction is incomplete or uncertain because of layout or encoding, state that clearly and cross-check multiple pages or sources before editing.

## Validation and change hygiene

- Prefer focused checks during development, then run the relevant full build before handoff.
- Distinguish pre-existing warnings from warnings introduced by the change; do not conceal either.
- Do not manually modify generated files, lockfiles, or unrelated working-tree changes unless the task requires it.
- Report the files changed and the validation command run in the final handoff.
