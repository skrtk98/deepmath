from __future__ import annotations

import subprocess
from pathlib import Path

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin


class CssBuildPlugin(BasePlugin):
    config_scheme = (
        ("enabled", c.Type(bool, default=True)),
        ("command", c.Type(list, default=["npm", "run", "build:css"])),
    )

    def on_config(self, config):
        self.enabled = self.config["enabled"]
        self.command = self.config["command"]
        docs_dir = Path(config["docs_dir"]).resolve()
        self.project_root = docs_dir.parent.resolve()
        return config

    def on_pre_build(self, config):
        if not self.enabled:
            return

        p = subprocess.run(
            self.command,
            cwd=str(self.project_root),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError(
                "CSS build command failed.\n"
                f"command: {self.command}\n"
                f"cwd: {self.project_root}\n"
                f"--- stdout ---\n{p.stdout}\n"
                f"--- stderr ---\n{p.stderr}\n"
            )
