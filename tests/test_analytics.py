import importlib


def test_self_healing_triggers_retry(monkeypatch, tmp_path):
    monkeypatch.setenv("SWOOP_CACHE_DIR", str(tmp_path / "cache"))

    import swoop.postprocess as postprocess_mod
    import swoop.router as router_mod
    import swoop.cache as cache_mod

    importlib.reload(postprocess_mod)
    monkeypatch.setattr(postprocess_mod, "SPEC_LIBRARY", {}, raising=False)
    monkeypatch.setattr(postprocess_mod, "_LOCAL_SPEC_CACHE", {}, raising=False)

    importlib.reload(cache_mod)
    importlib.reload(router_mod)

    calls = {"count": 0}

    def fake_sonar(vehicle, service, max_tokens=None, existing=None, hint=None):
        calls["count"] += 1
        if calls["count"] == 1:
            return (
                {
                    "vehicle": vehicle,
                    "service": service,
                    "facts": [
                        {
                            "k": "mystery_bolt",
                            "v": "verify",
                            "fastener_type": "Mystery Bolt",
                            "src": "https://example.com/bolt",
                        }
                    ],
                    "notes": [],
                },
                {"sonar_in": 120, "sonar_out": 80},
            )
        return (
            {
                "vehicle": vehicle,
                "service": service,
                "facts": [
                    {
                        "k": "mystery_bolt",
                        "v": "Torque mystery bolt to 40 ft-lb (54 Nm)",
                        "fastener_type": "Mystery Bolt",
                        "torque_ft_lb": 40,
                        "torque_nm": 54,
                        "src": "https://example.com/spec",
                    }
                ],
                "notes": [],
            },
            {"sonar_in": 40, "sonar_out": 60},
        )

    events = []

    monkeypatch.setattr(router_mod, "sonar_facts_compact", fake_sonar)
    monkeypatch.setattr(router_mod, "log_event", lambda kind, meta: events.append((kind, meta)))

    payload, meta = router_mod.ensure_research(
        {"year": 2020, "make": "Toyota", "model": "Camry", "engine_code": "A25A"},
        "custom_service",
    )

    assert calls["count"] == 2
    assert meta["healed"] is True
    assert meta["quality"]["torque_coverage"] >= 0.8
    assert any(kind == "self_heal" for kind, _ in events)
    assert any(
        fact.get("torque_ft_lb") == 40 and "Torque mystery bolt" in fact.get("v", "")
        for fact in payload.get("facts", [])
    )


def test_enrich_facts_records_local_spec(monkeypatch, tmp_path):
    import swoop.postprocess as postprocess

    monkeypatch.setattr(postprocess, "LOCAL_LIBRARY_PATH", tmp_path / "spec_library_local.json", raising=False)
    monkeypatch.setattr(postprocess, "_LOCAL_SPEC_CACHE", {}, raising=False)

    recorded = []

    def fake_persist(service, spec):
        recorded.append((service, spec))

    monkeypatch.setattr(postprocess, "_persist_local_spec", fake_persist, raising=False)
    monkeypatch.setattr(postprocess, "SPEC_LIBRARY", {}, raising=False)

    payload = {
        "facts": [
            {
                "k": "custom_bolt",
                "v": "Torque custom bolt to 45 ft-lb (61 Nm)",
                "fastener_type": "Custom Bolt",
                "torque_ft_lb": 45,
                "torque_nm": 61,
                "src": 1,
            }
        ],
        "steps": [],
        "notes": [],
        "refs": [{"index": 1, "url": "https://example.com/spec"}],
        "sources": ["https://example.com/spec"],
    }

    result = postprocess.enrich_facts(payload, "custom_service_local")

    assert any("custom bolt" in entry[1].get("fastener_type", "").lower() for entry in recorded)
    assert any("45 ft-lb" in fact.get("v", "") for fact in result.get("facts", []))
