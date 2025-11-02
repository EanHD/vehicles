import importlib
import json

import pytest


@pytest.fixture
def formatter_module(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    import swoop.formatter as formatter

    importlib.reload(formatter)
    return formatter


def test_render_html_merges_partials(monkeypatch, formatter_module):
    captured = {}

    def fake_post(url, headers, json, timeout):
        captured["payload"] = json

        class FakeResponse:
            def raise_for_status(self):
                return None

            def json(self):
                html = """<html><body>
                <section id="title">Title</section>
                <section id="vehicle-summary">Vehicle Summary</section>
                <section id="tools-consumables">Tools/Consumables</section>
                <section id="procedure-steps">Procedure Steps</section>
                <section id="specs-torques">Specs & Torques</section>
                <section id="safety">Safety</section>
                <section id="edge-cases">Edge Cases</section>
                <section id="references">References</section>
                </body></html>"""
                return {
                    "choices": [{"message": {"content": html}}],
                    "usage": {"prompt_tokens": 42, "completion_tokens": 128},
                }

        return FakeResponse()

    monkeypatch.setattr(formatter_module.requests, "post", fake_post)

    sonar_payload = {
        "vehicle": {"year": 2021, "make": "Ford", "model": "Bronco", "engine": "2.7T"},
        "service": "oil_change",
        "facts": [{"k": "oil_capacity", "v": "6.0 qt with filter", "src": "https://example.com"}],
        "notes": [],
        "sources": ["https://example.com"],
    }
    partials = {"safety": {"general": []}}

    html, tokens = formatter_module.render_html(sonar_payload, partials, {"doc_id": "test"})

    assert "<section id=\"title\">" in html
    assert tokens["fmt_in"] == 42
    assert tokens["fmt_out"] == 128

    user_blob = captured["payload"]["messages"][1]["content"]
    sent_json = json.loads(user_blob)
    assert "partials" in sent_json
    assert sent_json["partials"]["safety"] == {"general": []}
