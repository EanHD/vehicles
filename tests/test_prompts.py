from pathlib import Path
import json
import random

import pytest

from swoop.utils import safe_json_extract


def test_sonar_prompt_includes_constraints():
    prompt = Path("prompts/sonar_facts_compact.txt").read_text(encoding="utf-8")
    assert "Return compact JSON ONLY" in prompt
    assert "\"steps\"" in prompt
    assert "\"refs\"" in prompt
    assert "END" in prompt.splitlines()[-1]


@pytest.mark.parametrize("seed", range(5))
def test_safe_json_extract_handles_end_marker(seed):
    rnd = random.Random(seed)
    payload = {
        "vehicle": {"year": 2021, "make": "Ford", "model": "Bronco", "engine": "2.7T"},
        "service": "oil_change",
        "steps": [
            {"n": 1, "text": "Warm engine to operating temperature.", "src": 1},
            {
                "n": 2,
                "text": "Drain engine oil and torque plug to 27 ft-lb (37 Nm).",
                "torque_ft_lb": 27,
                "torque_nm": 36.6,
                "src": 2,
            },
        ],
        "facts": [{"k": "capacity", "v": f"{5 + rnd.randint(0,2)} qt", "src": 3}],
        "notes": [],
        "refs": [
            {"index": 1, "url": "https://example.com/prep"},
            {"index": 2, "url": "https://example.com/drain"},
            {"index": 3, "url": "https://example.com/spec"},
        ],
        "sources": ["https://example.com"],
    }
    text = json.dumps(payload) + "\nEND"
    extracted = safe_json_extract(text)
    assert extracted["vehicle"]["model"] == "Bronco"
    assert extracted["facts"][0]["k"] == "capacity"
