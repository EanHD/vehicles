import importlib
from pathlib import Path

import pytest


def _prime_modules(monkeypatch, tmp_path):
    monkeypatch.setenv("SWOOP_CACHE_DIR", str(tmp_path))
    import swoop.cache as cache_mod
    import swoop.router as router_mod
    import swoop.normalize as normalize_mod

    importlib.reload(cache_mod)
    importlib.reload(router_mod)
    importlib.reload(normalize_mod)
    return cache_mod, router_mod, normalize_mod


def _sample_payload():
    return {
        "vehicle": {"year": 2015, "make": "Chevrolet", "model": "Cruze", "engine": "LUJ"},
        "service": "brake_pads_replacement_front",
        "steps": [
            {
                "n": 1,
                "text": "Secure vehicle on stands and remove front wheels.",
                "src": "https://example.com/steps/setup",
            },
            {
                "n": 2,
                "text": "Compress caliper pistons and remove slide pins.",
                "torque_ft_lb": 23,
                "src": "https://example.com/steps/caliper",
            },
        ],
        "facts": [
            {
                "k": "torque_front_caliper",
                "v": "verify",
                "fastener_type": "Front caliper slide pin",
                "src": "https://example.com/torque",
            },
            {
                "k": "pad_thickness_min",
                "v": "3 mm minimum thickness",
                "src": "https://example.com/spec",
            },
            {
                "k": "bleed_sequence",
                "v": "RR, LR, RF, LF",
                "src": "https://example.com/bleed",
            },
            {
                "k": "rotor_spec",
                "v": "305 mm vented rotor, discard at 28 mm",
                "src": "https://example.com/rotor",
            },
            {
                "k": "wheel_torque",
                "v": "verify",
                "fastener_type": "Wheel lug nut",
                "src": "https://example.com/wheel",
            },
        ],
        "notes": [],
        "refs": [{"index": 1, "url": "https://example.com/torque"}],
        "sources": ["https://example.com/torque"],
    }


def test_router_uses_cache(monkeypatch, tmp_path):
    cache_mod, router_mod, normalize_mod = _prime_modules(monkeypatch, tmp_path)

    calls = []

    def fake_sonar(vehicle, service, max_tokens=600, existing=None, hint=None):
        calls.append({"existing": existing})
        return _sample_payload(), {"sonar_in": 120, "sonar_out": 380}

    monkeypatch.setattr(router_mod, "sonar_facts_compact", fake_sonar)

    vehicle = {"year": 2015, "make": "Chevy", "model": "Cruze", "engine_code": "LUJ"}

    first_data, first_meta = router_mod.ensure_research(vehicle, "brake_pads_replacement_front")
    assert len(calls) == 1
    assert first_meta["cache_hit"] is False
    assert first_meta["tokens"]["sonar_in"] == 120
    assert first_data["refs"]

    second_data, second_meta = router_mod.ensure_research(vehicle, "brake_pads_replacement_front")
    assert len(calls) == 1  # cache hit, no new sonar call
    assert second_meta["cache_hit"] is True
    assert second_data == first_data


def test_router_merges_partial_cache(monkeypatch, tmp_path):
    cache_mod, router_mod, normalize_mod = _prime_modules(monkeypatch, tmp_path)

    partial = _sample_payload()
    partial["facts"] = partial["facts"][:3]
    norm_vehicle = normalize_mod.normalize_vehicle(2018, "Chevy", "Cruze", "LUJ")
    cache_key = normalize_mod.cache_keys(norm_vehicle, "brake_pads_replacement_front")[0]
    cache_mod.set_(cache_key, partial)

    calls = []

    def fake_sonar(vehicle, service, max_tokens=600, existing=None, hint=None):
        calls.append(existing)
        fresh = _sample_payload()
        fresh["facts"] = fresh["facts"][3:]
        return fresh, {"sonar_in": 100, "sonar_out": 200}

    monkeypatch.setattr(router_mod, "sonar_facts_compact", fake_sonar)

    vehicle = {"year": 2018, "make": "Chevy", "model": "Cruze", "engine_code": "LUJ"}
    data, meta = router_mod.ensure_research(vehicle, "brake_pads_replacement_front")

    assert calls[-1] is not None
    assert meta["used_partial"] is True
    assert len(data["facts"]) >= 5
    caliper_fact = next(f for f in data["facts"] if f["k"] == "torque_front_caliper")
    assert "verify" not in caliper_fact["v"].lower()
    assert "<sup" in caliper_fact["v"]
