"""Validation helpers for research payload quality control."""

from __future__ import annotations

from typing import Any, Dict

from .utils import dedupe_facts


REQUIRED_KEYS = {"facts"}


def has_required_facts(data: Dict[str, Any]) -> bool:
    facts = data.get("facts") if data else None
    return bool(facts) and len(facts) >= 5


def covers_most_facts(data: Dict[str, Any]) -> bool:
    facts = data.get("facts") if data else None
    return bool(facts) and len(facts) >= 3


def merge_partials(primary: Dict[str, Any], fallback: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two fact payloads without duplicating facts."""
    if not fallback:
        return primary
    merged = {**fallback, **primary}
    primary_facts = primary.get("facts", [])
    fallback_facts = fallback.get("facts", [])
    merged["facts"] = dedupe_facts(list(primary_facts) + list(fallback_facts))
    if "notes" in primary or "notes" in fallback:
        merged["notes"] = list((primary.get("notes") or [])) + [
            note for note in fallback.get("notes") or [] if note not in (primary.get("notes") or [])
        ]
    if "sources" in primary or "sources" in fallback:
        merged["sources"] = list(dict.fromkeys((primary.get("sources") or []) + (fallback.get("sources") or [])))
    return merged
