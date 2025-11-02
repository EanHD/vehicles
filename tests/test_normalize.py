import pytest

from swoop.normalize import cache_keys, normalize_vehicle


def test_normalize_applies_alias_and_family():
    record = normalize_vehicle(2015, "chevy", "cruze diesel", "LUJ")
    assert record["make"] == "Chevrolet"
    assert record["model"] == "Cruze"
    assert record["engine_code"] == "LUJ"
    assert record["engine_family"] == "GM_1_4T_Family"
    assert record["platform"] == "GM_Delta_II"


def test_normalize_handles_missing_engine_code():
    record = normalize_vehicle(2020, "Volkswagen", "Golf")
    assert record["engine_code"] is None
    assert record["platform"] == "VW_MQB"


def test_cache_keys_priority_order():
    vehicle = {
        "year": 2020,
        "make": "Ford",
        "model": "F-150",
        "engine_code": None,
        "engine_family": "Ford_EcoBoost",
        "platform": "Ford_T1",
    }
    keys = cache_keys(vehicle, "oil_change")
    assert keys[0].startswith("oil_change|2020|Ford|F-150|")
    assert keys[1] == "oil_change|Ford_EcoBoost"
    assert keys[2] == "oil_change|Ford_T1"
    assert keys[3] == "oil_change"
