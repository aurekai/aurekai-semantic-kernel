#!/usr/bin/env python3
"""Export a verifiable proof bundle of the current pipeline state via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Export a verifiable proof bundle of the current pipeline state")
    def aurekai_proof_bundle_export(self, output_path: str = "/tmp/aurekai-proof-bundle.tar.gz") -> str:
        out = subprocess.run(
            ["akai", "proof", "export", "--output", output_path],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_proof_bundle_export(output_path="/tmp/aurekai-proof-bundle.tar.gz"))
