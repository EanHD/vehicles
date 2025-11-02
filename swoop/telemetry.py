"""Lightweight telemetry utilities for tracking token usage and cost."""

from __future__ import annotations

import json
import os
import time
from typing import Dict


LOG_PATH = os.getenv("SWOOP_COST_LOG", "cost_log.jsonl")

PRICES = {
    "sonar_in": 3.00 / 1_000_000,
    "sonar_out": 15.00 / 1_000_000,
    "fmt_in": 0.15 / 1_000_000,
    "fmt_out": 0.60 / 1_000_000,
}


def log_event(kind: str, meta: Dict) -> None:
    """Append an event to the telemetry log."""
    record = {"ts": time.time(), "kind": kind, **meta}
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")


def estimate_cost(tokens: Dict[str, int]) -> float:
    """Estimate USD cost based on provider price sheets."""
    return sum(tokens.get(measure, 0) * rate for measure, rate in PRICES.items())


def summarize_request(kind: str, tokens: Dict[str, int], meta: Dict | None = None) -> None:
    """Convenience helper to log a request with cost computed."""
    meta = meta or {}
    meta_tokens = {k: v for k, v in tokens.items() if v}
    cost = estimate_cost(meta_tokens)
    log_event(kind, {**meta, "tokens": meta_tokens, "cost_estimate_usd": round(cost, 6)})
