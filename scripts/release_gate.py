#!/usr/bin/env python3
"""Run the release gate check for the given version via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Run the release gate check for the given version")
    def aurekai_release_gate(self, version: str = "0.8.0-alpha.4") -> str:
        out = subprocess.run(
            ["akai", "release", "gate", "--version", version, "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_release_gate(version="0.8.0-alpha.4"))
