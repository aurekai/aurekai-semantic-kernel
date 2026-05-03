#!/usr/bin/env python3
"""Pack model memory artifacts for the given tag via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Pack model memory artifacts for the given tag")
    def aurekai_model_memory_pack(self, tag: str = "latest") -> str:
        out = subprocess.run(
            ["akai", "pack", "--tag", tag, "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_model_memory_pack(tag="latest"))
