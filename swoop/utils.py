"""Utility helpers used across the Swoop v2 pipeline."""

from __future__ import annotations

import json
import re
from typing import Any, Iterable


JSON_PATTERN = re.compile(r"\{.*\}", re.DOTALL)


def count_tokens(text: str) -> int:
    """Rudimentary token estimator for telemetry fallbacks."""
    if not text:
        return 0
    # Approximate GPT-style tokens using a simple heuristic.
    words = len(text.split())
    return max(1, int(words * 1.33))


def safe_json_extract(payload: str) -> dict[str, Any]:
    """Extract JSON object from a response that may include END marker."""
    if not payload:
        raise ValueError("No content to parse")

    cleaned = payload.strip()
    if cleaned.endswith("END"):
        cleaned = cleaned[: -len("END")].strip()

    match = JSON_PATTERN.search(cleaned)
    if not match:
        raise ValueError("No JSON object found in response")

    snippet = match.group(0)
    return json.loads(snippet)


def dedupe_facts(facts: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Remove duplicate fact entries preserving order."""
    seen: set[tuple[Any, Any]] = set()
    output: list[dict[str, Any]] = []
    for fact in facts:
        key = fact.get("k"), fact.get("src")
        if key not in seen:
            seen.add(key)
            output.append(fact)
    return output
