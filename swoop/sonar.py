"""Perplexity Sonar compact research client."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, Optional, Tuple

import requests

from .telemetry import summarize_request
from .utils import count_tokens, safe_json_extract


SONAR_API_KEY = os.getenv("PERPLEXITY_API_KEY")
SONAR_MODEL = os.getenv("SONAR_MODEL", "sonar-pro")
SONAR_TEMPERATURE = float(os.getenv("SONAR_TEMPERATURE", "0.3"))
DEFAULT_MAX_TOKENS = int(os.getenv("SONAR_MAX_TOKENS", "600"))


class SonarError(RuntimeError):
    """Raised when Sonar responses cannot be parsed."""


def _build_messages(
    prompt_template: str,
    instruction: str,
    existing: Optional[Dict] = None,
) -> list[dict[str, str]]:
    messages = [{"role": "system", "content": prompt_template}]
    if existing:
        user_content = (
            f"{instruction}\n\n"
            "Existing JSON (retain confirmed facts, fill only missing keys):\n"
            f"{json.dumps(existing, ensure_ascii=False)}"
        )
    else:
        user_content = instruction
    messages.append({"role": "user", "content": user_content})
    return messages


def sonar_facts_compact(
    vehicle: Dict[str, str],
    service: str,
    max_tokens: Optional[int] = None,
    existing: Optional[Dict] = None,
    hint: Optional[str] = None,
) -> Tuple[Dict, Dict[str, int]]:
    """Call Sonar to fetch compact fact JSON."""

    if not SONAR_API_KEY:
        raise SonarError("PERPLEXITY_API_KEY is not configured")

    prompt_template = Path("prompts/sonar_facts_compact.txt").read_text(encoding="utf-8")
    instruction = (
        f"Vehicle: {vehicle['year']} {vehicle['make']} {vehicle['model']} "
        f"({vehicle.get('engine_code') or vehicle.get('engine_family') or 'Unknown'})\n"
        f"Service: {service}\n"
        "Respond with compact JSON facts."
    )
    if hint:
        instruction = f"{instruction}\nFocus: {hint}"

    limit = min(int(max_tokens or DEFAULT_MAX_TOKENS), DEFAULT_MAX_TOKENS)
    payload = {
        "model": SONAR_MODEL,
        "messages": _build_messages(prompt_template, instruction, existing),
        "max_tokens": limit,
        "temperature": SONAR_TEMPERATURE,
    }

    headers = {"Authorization": f"Bearer {SONAR_API_KEY}", "Content-Type": "application/json"}
    api_url = os.getenv("PERPLEXITY_API_URL", "https://api.perplexity.ai/chat/completions")

    # Prefer stop sequences when the API allows it; fall back gracefully if unsupported.
    stop_sequence = ["\nEND"]
    if os.getenv("SONAR_DISABLE_STOP_SEQUENCE", "").lower() not in {"1", "true", "yes"}:
        payload["stop"] = stop_sequence

    response = requests.post(api_url, headers=headers, json=payload, timeout=60)
    if response.status_code == 400:
        try:
            error_body = response.json()
        except ValueError:
            error_body = {}
        if (
            "error" in error_body
            and isinstance(error_body["error"], dict)
            and "custom stop words" in (error_body["error"].get("message") or "").lower()
        ):
            payload.pop("stop", None)
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)

    response.raise_for_status()
    body = response.json()

    try:
        content = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise SonarError(f"Unexpected Sonar response: {body}") from exc

    try:
        data = safe_json_extract(content)
    except (ValueError, json.JSONDecodeError) as exc:
        raise SonarError(f"Failed to parse Sonar JSON: {content[:200]}") from exc

    usage_raw = body.get("usage") or {}
    tokens = {
        "sonar_in": usage_raw.get("prompt_tokens") or count_tokens(json.dumps(payload)),
        "sonar_out": usage_raw.get("completion_tokens") or count_tokens(content),
    }

    summarize_request(
        "sonar_request",
        tokens,
        meta={"vehicle": vehicle, "service": service, "cache": bool(existing)},
    )
    return data, tokens
