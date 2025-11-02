"""Router coordinating cache hierarchy and research calls."""

from __future__ import annotations

from typing import Dict, Tuple

from .cache import get, set_
from .normalize import cache_keys, normalize_vehicle
from .postprocess import compute_quality_metrics, enrich_facts
from .sonar import sonar_facts_compact
from .telemetry import log_event
from .validators import covers_most_facts, has_required_facts, merge_partials

STRATEGIES = ["exact", "family", "platform", "generic"]


def ensure_research(vehicle: Dict, service: str, max_tokens: int | None = 600) -> Tuple[Dict, Dict]:
    """Return research JSON and metadata, hydrating cache hierarchy as needed."""

    normalized = normalize_vehicle(
        vehicle["year"],
        vehicle["make"],
        vehicle["model"],
        vehicle.get("engine_code"),
    )
    keys = cache_keys(normalized, service)

    meta = {
        "cache_hit": False,
        "strategy": None,
        "cache_key": None,
        "tokens": {"sonar_in": 0, "sonar_out": 0},
        "used_partial": False,
        "healed": False,
        "retry_tokens": {"sonar_in": 0, "sonar_out": 0},
    }

    fallback_data = None
    fallback_strategy = None

    for idx, key in enumerate(keys):
        cached = get(key)
        if not cached:
            continue
        if has_required_facts(cached):
            enriched = enrich_facts(cached, service)
            if enriched is not cached:
                set_(key, enriched)
            metrics = compute_quality_metrics(service, enriched)
            meta.update(
                {
                    "cache_hit": True,
                    "strategy": STRATEGIES[idx],
                    "cache_key": key,
                    "quality": metrics,
                    "missing_specs": len(metrics.get("missing_components", [])),
                    "placeholders": metrics.get("placeholders", 0),
                    "healed": False,
                    "retry_tokens": {"sonar_in": 0, "sonar_out": 0},
                }
            )
            return enriched, meta
        if covers_most_facts(cached) and fallback_data is None:
            fallback_data = cached
            fallback_strategy = STRATEGIES[idx]

    payload, tokens = sonar_facts_compact(
        normalized,
        service,
        max_tokens=max_tokens,
        existing=fallback_data,
    )

    if fallback_data:
        payload = merge_partials(payload, fallback_data)
        meta["used_partial"] = True
        meta["strategy"] = fallback_strategy

    payload = enrich_facts(payload, service)

    metrics = compute_quality_metrics(service, payload)
    meta.update(
        {
            "cache_key": keys[0],
            "tokens": tokens,
            "strategy": meta["strategy"] or "miss",
            "quality": metrics,
            "missing_specs": len(metrics.get("missing_components", [])),
            "placeholders": metrics.get("placeholders", 0),
        }
    )

    needs_heal = metrics.get("torque_coverage", 1.0) < 0.8 or metrics.get("placeholders", 0) > 0

    if needs_heal:
        missing_components = metrics.get("missing_components", [])
        hint = ""
        if missing_components:
            hint = "Provide precise torque specs for: " + ", ".join(missing_components[:6])
        else:
            hint = "Provide any missing torque specifications to replace placeholders."
        retry_payload, retry_tokens = sonar_facts_compact(
            normalized,
            service,
            max_tokens=min(300, max_tokens or 300),
            existing=payload,
            hint=hint,
        )
        merged = merge_partials(retry_payload, payload)
        payload = enrich_facts(merged, service)
        retry_metrics = compute_quality_metrics(service, payload)
        meta["quality"] = retry_metrics
        meta["missing_specs"] = len(retry_metrics.get("missing_components", []))
        meta["placeholders"] = retry_metrics.get("placeholders", 0)
        meta["healed"] = True
        meta["retry_tokens"] = retry_tokens
        meta["tokens"]["sonar_in"] += retry_tokens.get("sonar_in", 0)
        meta["tokens"]["sonar_out"] += retry_tokens.get("sonar_out", 0)
        log_event(
            "self_heal",
            {
                "service": service,
                "vehicle": normalized,
                "missing_specs": len(missing_components),
                "retry_tokens": retry_tokens,
                "cache_key": keys[0],
                "healed": True,
            },
        )

    set_(keys[0], payload)

    return payload, meta
