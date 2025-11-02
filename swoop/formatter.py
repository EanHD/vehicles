"""Formatter model client for HTML rendering."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import requests

from .telemetry import summarize_request
from .utils import count_tokens


OAI_KEY = os.getenv("OPENAI_API_KEY")
FORMATTER_MODEL = os.getenv("FORMATTER_MODEL", "gpt-4o-mini")
FORMATTER_TEMPERATURE = float(os.getenv("FORMATTER_TEMPERATURE", "0.2"))

DEBUG_PAYLOAD_PATH = Path("debug_failed_payload.json")
MAX_USER_PAYLOAD_CHARS = 15_000


def _log_failed_payload(payload: Dict) -> None:
    """Persist the failing payload for postmortem debugging."""
    try:
        DEBUG_PAYLOAD_PATH.write_text(
            json.dumps({"ts": time.time(), "payload": payload}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[ERROR] Logged failed formatter payload to {DEBUG_PAYLOAD_PATH}")
    except OSError as exc:
        print(f"[ERROR] Failed to write debug payload: {exc}")


def safe_chat_completion(
    payload: Dict,
    headers: Dict[str, str],
    api_url: str,
    retries: int = 3,
    delay: int = 2,
) -> Dict:
    """Call chat completion endpoint with retry/backoff for transient failures."""

    wait = delay
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response else None
            if status and status >= 500 and attempt < retries:
                print(f"[WARN] Formatter HTTP {status}; retrying in {wait}s (attempt {attempt}/{retries})")
                time.sleep(wait)
                wait *= 2
                continue
            _log_failed_payload(payload)
            if status and status >= 500:
                print(f"[ERROR] Formatter HTTP {status} after {attempt} attempts: {exc}")
            else:
                print(f"[ERROR] Formatter HTTP {status or 'unknown'}: {exc}")
            raise
        except requests.RequestException as exc:
            if attempt < retries:
                print(f"[WARN] Formatter request error: {exc}; retrying in {wait}s (attempt {attempt}/{retries})")
                time.sleep(wait)
                wait *= 2
                continue
            _log_failed_payload(payload)
            print(f"[ERROR] Formatter request error after {attempt} attempts: {exc}")
            raise

    _log_failed_payload(payload)
    raise RuntimeError("Formatter API failed after retries")


CATEGORY_KEYWORDS = {
    "oil": ["oil", "drain", "filter"],
    "brake": ["brake", "pad", "rotor"],
    "battery": ["battery"],
    "cooling": ["coolant", "radiator"],
}

CATEGORY_TOOL_IDS = {
    "oil": {"torque_wrench", "socket_set_metric", "floor_jack"},
    "brake": {"torque_wrench", "socket_set_metric", "inspection_light"},
    "battery": {"socket_set_metric"},
    "cooling": {"torque_wrench", "inspection_light"},
}

CATEGORY_CONSUMABLE_IDS = {
    "oil": {"shop_rags", "anti_seize"},
    "brake": {"shop_rags", "dielectric_grease"},
    "battery": {"dielectric_grease"},
    "cooling": {"shop_rags"},
}

CATEGORY_PART_IDS = {
    "oil": {"oil_filter_oem", "drain_plug_washer"},
    "brake": {"brake_pads_front", "brake_hardware_kit"},
    "battery": {"battery_terminal_protector"},
    "cooling": {"coolant_premix"},
}


def _flatten_items(grouped: Dict[str, Iterable[Dict]]) -> List[Dict]:
    items: List[Dict] = []
    for values in grouped.values():
        if isinstance(values, list):
            items.extend(values)
    return items


def _dedupe_items(items: Iterable[Dict]) -> List[Dict]:
    seen = set()
    deduped: List[Dict] = []
    for item in items:
        key = item.get("id") or item.get("label")
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


def _detect_category(service: str) -> str:
    slug = (service or "").lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in slug for keyword in keywords):
            return category
    return "general"


def merge_job_specific_partials(payload: Dict, partials: Dict | None) -> Dict:
    """Filter and dedupe partials based on service category."""
    if not partials:
        return {}

    category = _detect_category(payload.get("service", ""))
    tool_ids = CATEGORY_TOOL_IDS.get(category, set())
    consumable_ids = CATEGORY_CONSUMABLE_IDS.get(category, set())

    filtered: Dict[str, Dict[str, List[Dict]]] = {}

    tools = partials.get("tools") or {}
    consumables = partials.get("consumables") or {}
    safety = partials.get("safety") or {}
    parts = partials.get("parts") or {}

    existing_tool_labels = {item.get("label") for item in payload.get("tools", []) or []}
    existing_consumable_labels = {item.get("label") for item in payload.get("consumables", []) or []}

    if tools:
        flat_tools = _flatten_items(tools)
        if tool_ids:
            flat_tools = [item for item in flat_tools if item.get("id") in tool_ids]
        if existing_tool_labels:
            flat_tools = [item for item in flat_tools if item.get("label") not in existing_tool_labels]
        filtered["tools"] = {"recommended": _dedupe_items(flat_tools)}

    if consumables:
        flat_consumables = _flatten_items(consumables)
        if consumable_ids:
            flat_consumables = [item for item in flat_consumables if item.get("id") in consumable_ids]
        if existing_consumable_labels:
            flat_consumables = [
                item for item in flat_consumables if item.get("label") not in existing_consumable_labels
            ]
        filtered["consumables"] = {"recommended": _dedupe_items(flat_consumables)}

    if safety:
        filtered["safety"] = safety

    if parts:
        flat_parts = _flatten_items(parts)
        part_ids = CATEGORY_PART_IDS.get(category, set())
        if part_ids:
            flat_parts = [item for item in flat_parts if item.get("id") in part_ids]
        existing_part_labels = {item.get("label") for item in payload.get("parts", []) or []}
        if existing_part_labels:
            flat_parts = [item for item in flat_parts if item.get("label") not in existing_part_labels]
        if flat_parts:
            filtered["parts"] = {"recommended": _dedupe_items(flat_parts)}

    return filtered


def merge_with_partials(payload: Dict, partials: Dict) -> Dict:
    """Attach local partials to payload for the formatter."""
    merged = dict(payload)
    scoped_partials = merge_job_specific_partials(payload, partials)
    if scoped_partials:
        merged["partials"] = scoped_partials
        if "parts" in scoped_partials and scoped_partials["parts"].get("recommended"):
            merged.setdefault("parts", scoped_partials["parts"]["recommended"])
        if "safety" in scoped_partials and scoped_partials["safety"]:
            merged.setdefault("safety", scoped_partials["safety"])
    return merged


def render_html(sonar_json: Dict, partials: Dict | None = None, doc_context: Dict | None = None) -> Tuple[str, Dict[str, int]]:
    """Render HTML using the formatter model."""

    if not OAI_KEY:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    sys_prompt = Path("prompts/formatter_html_template.txt").read_text(encoding="utf-8")
    merged = merge_with_partials(sonar_json, partials or {})
    user_json = json.dumps(merged, ensure_ascii=False, separators=(",", ":"))
    if len(user_json) > MAX_USER_PAYLOAD_CHARS:
        print(
            f"[WARN] Formatter payload length {len(user_json)} exceeds {MAX_USER_PAYLOAD_CHARS}; "
            "using compact JSON payload."
        )

    payload = {
        "model": FORMATTER_MODEL,
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_json},
        ],
        "temperature": FORMATTER_TEMPERATURE,
    }

    headers = {"Authorization": f"Bearer {OAI_KEY}", "Content-Type": "application/json"}
    api_url = os.getenv("OPENAI_API_URL", "https://api.openai.com/v1/chat/completions")
    body = safe_chat_completion(payload, headers, api_url)

    html = body["choices"][0]["message"]["content"]

    usage_raw = body.get("usage") or {}
    tokens = {
        "fmt_in": usage_raw.get("prompt_tokens") or count_tokens(user_json + sys_prompt),
        "fmt_out": usage_raw.get("completion_tokens") or count_tokens(html),
    }
    summarize_request("formatter_request", tokens, meta=doc_context or {})
    return html, tokens
