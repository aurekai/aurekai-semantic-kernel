#!/usr/bin/env python3
"""Run a Sparse Autoencoder (SAE) audit on the given model via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Run a Sparse Autoencoder (SAE) audit on the given model")
    def aurekai_sae_audit(self, model_id: str = "default") -> str:
        out = subprocess.run(
            ["akai", "sae", "audit", "--model", model_id, "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_sae_audit(model_id="default"))
