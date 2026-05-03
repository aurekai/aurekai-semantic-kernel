#!/usr/bin/env python3
"""Verify an Aurekai manifest against the deploy schema via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Verify an Aurekai manifest against the deploy schema")
    def aurekai_manifest_verify(self, manifest_path: str = "artifact.json") -> str:
        out = subprocess.run(
            ["akai", "verify", "--manifest", manifest_path, "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_manifest_verify(manifest_path="artifact.json"))
