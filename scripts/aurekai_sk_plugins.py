"""
aurekai_semantic_kernel.py — Semantic Kernel plugins for Aurekai capability families.
All plugins generated from aurekai.capabilities.json.
"""
from __future__ import annotations

import json
import subprocess
from typing import Any, Annotated

from semantic_kernel.functions import kernel_function


def _run_akai(args: list[str], timeout: int = 300) -> str:
    result = subprocess.run(
        ["akai", *args, "--json"],
        capture_output=True, text=True, timeout=timeout,
    )
    return result.stdout or result.stderr


class AurekaiRuntimePlugin:
    """Aurekai Runtime capability family — for use with SK kernel."""

    @kernel_function(name="doctor", description="Run Akai runtime deep diagnostics")
    def doctor(self, deep: Annotated[bool, "Run deep diagnostics"] = True) -> Annotated[str, "JSON result"]:
        return _run_akai(["doctor", "--deep"] if deep else ["doctor"])

    @kernel_function(name="capabilities", description="List all Akai capability families and commands")
    def capabilities(self) -> Annotated[str, "JSON capability registry"]:
        return _run_akai(["runtime", "capabilities"])

    @kernel_function(name="manifest_verify", description="Verify artifact.json manifest")
    def manifest_verify(
        self, manifest: Annotated[str, "Path to manifest file"] = "artifact.json"
    ) -> Annotated[str, "JSON validation result"]:
        return _run_akai(["verify", "--manifest", manifest])

    @kernel_function(name="queue_enqueue", description="Enqueue work into AkaiQueue")
    def queue_enqueue(self, queue: Annotated[str, "Queue name"] = "default") -> Annotated[str, "JSON result"]:
        return _run_akai(["queue", "enqueue", "--queue", queue])


class AurekaiMediaPlugin:
    """Aurekai Intake/Publish capability family."""

    @kernel_function(name="transcribe", description="Transcribe an audio file")
    def transcribe(
        self,
        audio_path: Annotated[str, "Path to audio file"],
        language: Annotated[str, "Language code"] = "en",
    ) -> Annotated[str, "JSON transcript result"]:
        return _run_akai(["transcribe", "audio", "--input", audio_path, "--language", language], timeout=600)

    @kernel_function(name="transcript_clean", description="Clean and normalize a transcript")
    def transcript_clean(self, transcript_id: Annotated[str, "Transcript artifact ID"]) -> Annotated[str, "JSON result"]:
        return _run_akai(["transcript", "clean", "--id", transcript_id])

    @kernel_function(name="generate_brief", description="Generate a brief from an artifact")
    def generate_brief(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON brief"]:
        return _run_akai(["brief", "generate", "--artifact", artifact_id])

    @kernel_function(name="pack_deliverable", description="Pack a deliverable from a brief")
    def pack_deliverable(self, brief_id: Annotated[str, "Brief artifact ID"]) -> Annotated[str, "JSON result"]:
        return _run_akai(["pack", "deliverable", "--brief", brief_id])


class AurekaiMemoryPlugin:
    """Aurekai Memory capability family — FPQ, vec, SAE."""

    @kernel_function(name="vec_search", description="Vector search over Akai model memory")
    def vec_search(
        self,
        query: Annotated[str, "Search query"],
        top_k: Annotated[int, "Number of results"] = 10,
    ) -> Annotated[str, "JSON search results"]:
        return _run_akai(["vec", "search", "--query", query, "--top-k", str(top_k)])

    @kernel_function(name="fpq_compress", description="FPQ compress a model")
    def fpq_compress(
        self,
        model_tag: Annotated[str, "Model tag"],
        bits: Annotated[int, "Quantization bits"] = 8,
    ) -> Annotated[str, "JSON result"]:
        return _run_akai(["fpq", "compress", "--model", model_tag, "--bits", str(bits)], timeout=600)

    @kernel_function(name="sae_activate", description="Run SAE feature activation on an artifact")
    def sae_activate(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON features"]:
        return _run_akai(["sae", "activate", "--artifact", artifact_id])


class AurekaiProofPlugin:
    """Aurekai Proof capability family."""

    @kernel_function(name="proof_bundle", description="Export an Akai proof bundle")
    def proof_bundle(self, run_id: Annotated[str, "Run ID"] = "") -> Annotated[str, "JSON proof"]:
        args = ["proof", "bundle"]
        if run_id:
            args += ["--run-id", run_id]
        return _run_akai(args)

    @kernel_function(name="graph_lineage", description="Get artifact lineage graph")
    def graph_lineage(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON lineage"]:
        return _run_akai(["graph", "lineage", "--artifact", artifact_id])

    @kernel_function(name="canon_hash", description="Canonical hash of an artifact")
    def canon_hash(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON hash"]:
        return _run_akai(["canon", "hash", "--artifact", artifact_id])


class AurekaiCommercePlugin:
    """Aurekai Commerce capability family."""

    @kernel_function(name="meter_record", description="Record a metering event")
    def meter_record(
        self,
        event: Annotated[str, "Event name"],
        units: Annotated[float, "Units consumed"] = 1.0,
        client_id: Annotated[str, "Client ID"] = "",
    ) -> Annotated[str, "JSON result"]:
        args = ["meter", "record", "--event", event, "--units", str(units)]
        if client_id:
            args += ["--client", client_id]
        return _run_akai(args)

    @kernel_function(name="generate_invoice", description="Generate client invoice")
    def generate_invoice(
        self,
        client_id: Annotated[str, "Client ID"],
        period: Annotated[str, "Billing period"] = "current",
    ) -> Annotated[str, "JSON invoice"]:
        return _run_akai(["pay", "invoice", "--client", client_id, "--period", period])


class AurekaiReasonPlugin:
    """Aurekai Reason capability family."""

    @kernel_function(name="reason_start", description="Start a reasoning session")
    def reason_start(self, prompt: Annotated[str, "Initial prompt"] = "") -> Annotated[str, "JSON session"]:
        args = ["reason", "start"]
        if prompt:
            args += ["--prompt", prompt]
        return _run_akai(args)

    @kernel_function(name="reason_branch", description="Branch a reasoning session")
    def reason_branch(self, session_id: Annotated[str, "Session ID"]) -> Annotated[str, "JSON branch"]:
        return _run_akai(["reason", "branch", "--session", session_id])

    @kernel_function(name="reason_diff", description="Diff two reasoning branches")
    def reason_diff(self, session_id: Annotated[str, "Session ID"]) -> Annotated[str, "JSON diff"]:
        return _run_akai(["reason", "diff", "--session", session_id])


class AurekaiWirePlugin:
    """Aurekai Wire/Telephony capability family."""

    @kernel_function(name="wire_report", description="Generate wire report for a capture")
    def wire_report(self, capture_id: Annotated[str, "Capture artifact ID"]) -> Annotated[str, "JSON report"]:
        return _run_akai(["wire", "report", "--capture", capture_id])

    @kernel_function(name="tel_sim_call", description="Simulate a telephony call")
    def tel_sim_call(self, target: Annotated[str, "Target number or SIP URI"]) -> Annotated[str, "JSON result"]:
        return _run_akai(["tel", "sim-call", "--target", target])


class AurekaiPublishPlugin:
    """Aurekai Publish capability family."""

    @kernel_function(name="distribute_bundle", description="Distribute an artifact bundle")
    def distribute_bundle(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON result"]:
        return _run_akai(["distribute", "bundle", "--artifact", artifact_id])

    @kernel_function(name="repurpose_content", description="Repurpose content for distribution")
    def repurpose_content(self, artifact_id: Annotated[str, "Artifact ID"]) -> Annotated[str, "JSON result"]:
        return _run_akai(["repurpose", "content", "--artifact", artifact_id])


# All plugins as a list for easy kernel registration
ALL_AUREKAI_PLUGINS = [
    ("AurekaiRuntime", AurekaiRuntimePlugin()),
    ("AurekaiMedia", AurekaiMediaPlugin()),
    ("AurekaiMemory", AurekaiMemoryPlugin()),
    ("AurekaiProof", AurekaiProofPlugin()),
    ("AurekaiCommerce", AurekaiCommercePlugin()),
    ("AurekaiReason", AurekaiReasonPlugin()),
    ("AurekaiWire", AurekaiWirePlugin()),
    ("AurekaiPublish", AurekaiPublishPlugin()),
]
