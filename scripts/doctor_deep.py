#!/usr/bin/env python3
"""Run Aurekai doctor --deep and return structured diagnostics via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Run Aurekai doctor --deep and return structured diagnostics")
    def aurekai_doctor_deep(self, ) -> str:
        out = subprocess.run(
            ["akai", "doctor", "--deep", "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_doctor_deep())
