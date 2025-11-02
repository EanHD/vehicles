"""Vehicle normalization helpers for cost-efficient research routing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


ALIASES: Dict[str, Dict[str, str]] = {
    "make": {
        "chevy": "Chevrolet",
        "vw": "Volkswagen",
        "merc": "Mercedes-Benz",
    },
    "model": {
        "cruze diesel": "Cruze",
        "135 i": "135i",
        "f-150 lariat": "F-150",
    },
}

# Example engine to family mapping; extend through telemetry feedback.
ENGINE_FAMILY_MAP: Dict[str | tuple, str] = {
    "LUJ": "GM_1_4T_Family",
    "LUH": "GM_1_4T_Family",
    "4G63": "Mitsubishi_4G63_Family",
    "4G64": "Mitsubishi_4G6_Family",
}

# Platform mapping keyed by (make, model)
PLATFORM_MAP: Dict[tuple[str, str], str] = {
    ("Chevrolet", "Cruze"): "GM_Delta_II",
    ("Volkswagen", "Golf"): "VW_MQB",
}


@dataclass(frozen=True)
class NormalizedVehicle:
    """Lightweight record with normalized vehicle metadata."""

    year: int
    make: str
    model: str
    engine_code: Optional[str]
    engine_family: Optional[str]
    platform: Optional[str]


def _normalize_name(value: str, alias_map: Dict[str, str]) -> str:
    if not value:
        return value
    canonical = alias_map.get(value.lower(), value)
    return canonical.title() if canonical.islower() else canonical


def normalize_vehicle(
    year: int,
    make: str,
    model: str,
    engine_code: Optional[str] = None,
) -> Dict[str, Optional[str] | int]:
    """Normalize vehicle fields for cache-friendly keys."""

    normalized_make = _normalize_name(make, ALIASES["make"])
    normalized_model = _normalize_name(model, ALIASES["model"])

    engine_code_norm = (engine_code or "").upper().strip() or None
    engine_family = None

    if engine_code_norm and engine_code_norm in ENGINE_FAMILY_MAP:
        engine_family = ENGINE_FAMILY_MAP[engine_code_norm]

    platform = PLATFORM_MAP.get((normalized_make, normalized_model))

    return {
        "year": int(year),
        "make": normalized_make,
        "model": normalized_model,
        "engine_code": engine_code_norm,
        "engine_family": engine_family,
        "platform": platform,
    }


def cache_keys(vehicle: Dict[str, Optional[str] | int], service: str) -> List[str]:
    """Return cache keys ordered from most specific to generic."""

    engine_fragment = vehicle.get("engine_code") or vehicle.get("engine_family") or ""

    exact = f"{service}|{vehicle['year']}|{vehicle['make']}|{vehicle['model']}|{engine_fragment}"
    family = f"{service}|{vehicle.get('engine_family') or ''}"
    platform = f"{service}|{vehicle.get('platform') or ''}"
    generic = f"{service}"
    return [exact, family, platform, generic]
