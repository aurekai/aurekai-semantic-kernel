#!/usr/bin/env python3
"""Benchmark the Aurekai semantic cache via Semantic Kernel plugin."""
import subprocess
from semantic_kernel.functions import kernel_function


class AurekaiPlugin:
    @kernel_function(description="Benchmark the Aurekai semantic cache")
    def aurekai_semantic_cache_bench(self, queries: int = 100) -> str:
        out = subprocess.run(
            ["akai", "cache", "bench", "--queries", str(queries), "--json"],
            capture_output=True, text=True
        )
        return out.stdout + out.stderr


if __name__ == "__main__":
    p = AurekaiPlugin()
    print(p.aurekai_semantic_cache_bench(queries=100))
