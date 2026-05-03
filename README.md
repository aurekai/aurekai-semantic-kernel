<p align="center">
  <img src="https://raw.githubusercontent.com/aurekai/aurekai/main/assets/aurekai-logo.svg" alt="Aurekai" width="520" />
</p>

# `aurekai-semantic-kernel` · v0.8.0-alpha.5

Official Semantic Kernel integration for Aurekai — 8 typed plugins covering all capability families.

## Plugins

| Plugin | Family | Functions |
|---|---|---|
| `AurekaiRuntimePlugin` | runtime | `doctor`, `capabilities`, `manifest_verify`, `queue_enqueue` |
| `AurekaiMediaPlugin` | intake/publish | `transcribe`, `transcript_clean`, `generate_brief`, `pack_deliverable` |
| `AurekaiMemoryPlugin` | memory | `vec_search`, `fpq_compress`, `sae_activate` |
| `AurekaiProofPlugin` | proof | `proof_bundle`, `graph_lineage`, `canon_hash` |
| `AurekaiCommercePlugin` | commerce | `meter_record`, `generate_invoice` |
| `AurekaiReasonPlugin` | reason | `reason_start`, `reason_branch`, `reason_diff` |
| `AurekaiWirePlugin` | wire | `wire_report`, `tel_sim_call` |
| `AurekaiPublishPlugin` | publish | `distribute_bundle`, `repurpose_content` |

## Quick Start

```python
import semantic_kernel as sk
from aurekai_sk_plugins import ALL_AUREKAI_PLUGINS

kernel = sk.Kernel()
for name, plugin in ALL_AUREKAI_PLUGINS:
    kernel.add_plugin(plugin, plugin_name=name)

result = await kernel.invoke(kernel.plugins["AurekaiRuntime"]["doctor"])
```


Aurekai integration surface for Semantic Kernel.

Status: active
Type: agent

## Core Template Set

- doctor-deep
- manifest-verify
- model-memory-pack
- sae-audit
- semantic-cache-bench
- proof-bundle-export
- release-gate

## Canonical References

- Platform: https://github.com/aurekai/aurekai
- Native runtime: https://github.com/aurekai/native-runtime
- Integration registry: https://github.com/aurekai/aurekai/blob/main/registry/integrations.json
- Ecosystem map: https://github.com/aurekai/aurekai/blob/main/ECOSYSTEM_NAMES.md
