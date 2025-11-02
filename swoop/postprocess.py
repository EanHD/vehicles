"""Post-processing utilities to enrich compact Sonar payloads."""

from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


RAW_SPEC_LIBRARY: Dict[str, List[Dict[str, Any]]] = {
    "oil_change": [
        {
            "id": "drain_plug",
            "keywords": ["drain plug", "oil pan bolt", "drain bolt"],
            "value": "Tighten drain plug to 27 ft-lb (37 Nm)",
            "torque_ft_lb": 27,
            "torque_nm": 37,
            "spec_units": "ft-lb",
            "fastener_type": "Oil drain plug",
            "source": "https://manual.swoopservice.com/specs/toyota_camry_oil_change",
        },
        {
            "id": "filter_housing",
            "keywords": ["filter housing", "oil filter", "filter cap"],
            "value": "Tighten oil filter housing to 18 ft-lb (24 Nm)",
            "torque_ft_lb": 18,
            "torque_nm": 24,
            "spec_units": "ft-lb",
            "fastener_type": "Oil filter housing",
            "source": "https://manual.swoopservice.com/specs/toyota_camry_oil_change",
        },
        {
            "id": "oil_capacity",
            "keywords": ["oil capacity", "fill capacity", "refill"],
            "value": "Fill with 4.8 qt (4.5 L) 0W-16 synthetic oil",
            "spec_units": "qt",
            "source": "https://manual.swoopservice.com/specs/toyota_camry_oil_change",
        },
    ],
    "brake_pads_replacement_front": [
        {
            "id": "caliper_bracket",
            "keywords": ["caliper bracket", "anchor bolts", "mounting bolts"],
            "value": "Torque front caliper bracket bolts to 74 ft-lb (100 Nm)",
            "torque_ft_lb": 74,
            "torque_nm": 100,
            "spec_units": "ft-lb",
            "fastener_type": "Front caliper bracket bolt",
            "source": "https://manual.swoopservice.com/specs/brake_pads_replacement_front",
        },
        {
            "id": "caliper_slide",
            "keywords": ["slide pin", "guide pin"],
            "value": "Torque front caliper slide pins to 23 ft-lb (31 Nm)",
            "torque_ft_lb": 23,
            "torque_nm": 31,
            "spec_units": "ft-lb",
            "fastener_type": "Front caliper slide pin",
            "source": "https://manual.swoopservice.com/specs/brake_pads_replacement_front",
        },
        {
            "id": "wheel_lug",
            "keywords": ["wheel lug", "lug nut", "wheel torque"],
            "value": "Torque wheel lug nuts to 100 ft-lb (135 Nm) in a star pattern",
            "torque_ft_lb": 100,
            "torque_nm": 135,
            "spec_units": "ft-lb",
            "fastener_type": "Wheel lug nut",
            "source": "https://manual.swoopservice.com/specs/brake_pads_replacement_front",
        },
    ],
}


PLACEHOLDER_PATTERN = re.compile(r"\b(verify|tbd|unknown|check manual)\b", re.I)
VERIFY_SPAN_PATTERN = re.compile(r"<span class='verify'>.*?</span>", re.I)
SUP_TAG_PATTERN = re.compile(r"<sup[^>]*>.*?</sup>", re.I)
MAIN_LIBRARY_PATH = Path(__file__).with_name("spec_library.json")
LOCAL_LIBRARY_PATH = Path(__file__).with_name("spec_library_local.json")


def _load_library_file(path: Path) -> Dict[str, List[Dict[str, Any]]]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {k: list(v) for k, v in data.items() if isinstance(v, list)}
    except (OSError, json.JSONDecodeError):
        pass
    return {}


def _merge_spec_libraries(base: Dict[str, List[Dict[str, Any]]], extra: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    merged: Dict[str, List[Dict[str, Any]]] = {service: list(entries) for service, entries in base.items()}
    for service, entries in extra.items():
        dest = merged.setdefault(service, [])
        for entry in entries:
            if entry not in dest:
                dest.append(entry)
    return merged


BASE_SPEC_LIBRARY = _merge_spec_libraries(RAW_SPEC_LIBRARY, _load_library_file(MAIN_LIBRARY_PATH))
LOCAL_SPEC_LIBRARY = _load_library_file(LOCAL_LIBRARY_PATH)
SPEC_LIBRARY = _merge_spec_libraries(BASE_SPEC_LIBRARY, LOCAL_SPEC_LIBRARY)
_LOCAL_SPEC_CACHE = {service: list(entries) for service, entries in LOCAL_SPEC_LIBRARY.items()}


def _spec_signature(service: str, spec: Dict[str, Any]) -> Tuple[str, Optional[str], Optional[float], Optional[float], Optional[str]]:
    component = spec.get("fastener_type") or spec.get("component") or spec.get("id") or spec.get("k")
    value = spec.get("value")
    return (
        service,
        (component or "").lower().strip(),
        spec.get("torque_ft_lb"),
        spec.get("torque_nm"),
        value.strip() if isinstance(value, str) else value,
    )


def _ensure_spec_entry_list(service: str) -> List[Dict[str, Any]]:
    _LOCAL_SPEC_CACHE.setdefault(service, _LOCAL_SPEC_CACHE.get(service, []))
    return SPEC_LIBRARY.setdefault(service, [])


def _persist_local_spec(service: str, spec: Dict[str, Any]) -> None:
    signature = _spec_signature(service, spec)
    existing_signatures = {_spec_signature(service, entry) for entry in _LOCAL_SPEC_CACHE.get(service, [])}
    if signature in existing_signatures:
        return
    stored_spec = {k: v for k, v in spec.items() if k != "service"}
    _LOCAL_SPEC_CACHE.setdefault(service, []).append(stored_spec)
    try:
        LOCAL_LIBRARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOCAL_LIBRARY_PATH.write_text(
            json.dumps(_LOCAL_SPEC_CACHE, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except OSError:
        return


def _add_spec_to_memory(service: str, spec: Dict[str, Any]) -> None:
    if not service:
        return
    entries = _ensure_spec_entry_list(service)
    signature = _spec_signature(service, spec)
    if signature in {_spec_signature(service, entry) for entry in entries}:
        return
    stored_spec = {k: v for k, v in spec.items() if k != "service"}
    entries.append(stored_spec)
    _persist_local_spec(service, stored_spec)


def _strip_sup(text: Optional[str]) -> str:
    if not isinstance(text, str):
        return ""
    return SUP_TAG_PATTERN.sub("", text).strip()


def _register_spec_from_payload(
    service: str,
    entry: Dict[str, Any],
    tracker: "ReferenceTracker",
    component_fields: List[str],
    value_field: str,
) -> None:
    component = None
    for field in component_fields:
        value = entry.get(field)
        if value:
            component = value
            break
    component = (component or "").strip()
    if not component:
        return
    torque_ft_lb = entry.get("torque_ft_lb")
    torque_nm = entry.get("torque_nm")
    if torque_ft_lb is None and torque_nm is None:
        return
    raw_value = entry.get(value_field)
    value_clean = _strip_sup(raw_value)
    source_url = tracker.url_for(entry.get("ref")) or tracker.url_for(entry.get("src"))
    spec_record = {
        "id": entry.get("id") or entry.get("k") or component.replace(" ", "_"),
        "keywords": [component],
        "value": value_clean or raw_value,
        "torque_ft_lb": torque_ft_lb,
        "torque_nm": torque_nm,
        "spec_units": entry.get("spec_units"),
        "fastener_type": component,
        "source": source_url,
        "service": service,
    }
    _add_spec_to_memory(service, spec_record)


def _ensure_list(data: Optional[Iterable]) -> List:
    if not data:
        return []
    return list(data)


def _tokenize(text: str) -> Set[str]:
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def _normalize_step(step: Dict[str, Any]) -> Dict[str, Any]:
    normalized = dict(step)
    normalized.setdefault("n", step.get("n") or step.get("step") or 0)
    normalized.setdefault("text", step.get("text") or step.get("description", ""))
    return normalized


class ReferenceTracker:
    """Utility to assign sequential reference numbers for unique URLs."""

    def __init__(self, initial: Optional[Dict[int, str]] = None, sources: Optional[List[str]] = None) -> None:
        self._url_to_index: "OrderedDict[str, int]" = OrderedDict()
        if initial:
            for idx in sorted(initial):
                url = initial[idx]
                if url:
                    self._url_to_index[str(url)] = int(idx)
        if sources:
            for url in sources:
                self.add(url)

    def add(self, url: Optional[str]) -> Optional[int]:
        if not url:
            return None
        normalized = str(url).strip()
        if not normalized:
            return None
        if normalized in self._url_to_index:
            return self._url_to_index[normalized]
        index = len(self._url_to_index) + 1
        self._url_to_index[normalized] = index
        return index

    def to_list(self) -> List[Dict[str, Any]]:
        return [{"index": idx, "url": url} for url, idx in self._url_to_index.items()]

    def urls(self) -> List[str]:
        return list(self._url_to_index.keys())

    def url_for(self, index: Optional[int]) -> Optional[str]:
        if index is None:
            return None
        for url, idx in self._url_to_index.items():
            if idx == index:
                return url
        return None


def _extract_existing_refs(raw_refs: Any) -> Dict[int, str]:
    mapping: Dict[int, str] = {}
    if isinstance(raw_refs, dict):
        for key, url in raw_refs.items():
            try:
                idx = int(key)
            except (TypeError, ValueError):
                continue
            mapping[idx] = url
    elif isinstance(raw_refs, list):
        for item in raw_refs:
            if not isinstance(item, dict):
                continue
            idx = item.get("index") or item.get("id")
            url = item.get("url")
            if isinstance(idx, int) and isinstance(url, str):
                mapping[idx] = url
    return mapping


def _inject_sup(text: str, index: int) -> str:
    if not text:
        return text
    tag = f'<sup id="ref-{index}">[{index}]</sup>'
    if f"ref-{index}" in text:
        return text
    if text.endswith(" "):
        return text + tag
    return f"{text.rstrip()} {tag}".strip()


def _match_spec_entry(service: str, *candidates: str) -> Optional[Dict[str, Any]]:
    library = SPEC_LIBRARY.get(service) or []
    tokens = [_tokenize(candidate) for candidate in candidates if candidate]
    for entry in library:
        keywords = entry.get("keywords", [])
        for keyword in keywords:
            keyword_tokens = _tokenize(keyword)
            if any(keyword_tokens <= token_set or keyword.lower() in " ".join(token_set) for token_set in tokens):
                return entry
    return None


def _apply_spec_to_fact(fact: Dict[str, Any], spec: Dict[str, Any], service: str) -> None:
    if not spec:
        return
    if PLACEHOLDER_PATTERN.search(str(fact.get("v", ""))):
        fact["v"] = spec.get("value", fact.get("v"))
    fact.setdefault("fastener_type", spec.get("fastener_type"))
    if spec.get("torque_ft_lb") and not fact.get("torque_ft_lb"):
        fact["torque_ft_lb"] = spec.get("torque_ft_lb")
    if spec.get("torque_nm") and not fact.get("torque_nm"):
        fact["torque_nm"] = spec.get("torque_nm")
    if spec.get("spec_units") and not fact.get("spec_units"):
        fact["spec_units"] = spec.get("spec_units")
    fact.setdefault("src", spec.get("source"))
    _add_spec_to_memory(service, {**spec, "service": service})


def _apply_spec_to_step(step: Dict[str, Any], spec: Dict[str, Any], service: str) -> None:
    if not spec:
        return
    if spec.get("torque_ft_lb") and not step.get("torque_ft_lb"):
        step["torque_ft_lb"] = spec.get("torque_ft_lb")
    if spec.get("torque_nm") and not step.get("torque_nm"):
        step["torque_nm"] = spec.get("torque_nm")
    if spec.get("fastener_type") and not step.get("fastener_type"):
        step["fastener_type"] = spec.get("fastener_type")
    replacement_text = spec.get("value")
    if replacement_text:
        if VERIFY_SPAN_PATTERN.search(step.get("text", "")):
            step["text"] = VERIFY_SPAN_PATTERN.sub(replacement_text, step["text"])
        elif "verify torque" in step.get("text", "").lower():
            step["text"] = step["text"].replace("Verify torque", replacement_text)
    step.setdefault("src", spec.get("source"))
    _add_spec_to_memory(service, {**spec, "service": service})


def enrich_facts(payload: Dict[str, Any], service: str) -> Dict[str, Any]:
    if not payload:
        return payload

    data = dict(payload)
    steps = [_normalize_step(step) for step in _ensure_list(data.get("steps"))]
    facts = _ensure_list(data.get("facts"))
    notes = _ensure_list(data.get("notes"))

    existing_ref_map = _extract_existing_refs(data.get("refs"))
    tracker = ReferenceTracker(existing_ref_map, data.get("sources"))

    # Hydrate facts with library data when placeholders remain.
    for fact in facts:
        spec = _match_spec_entry(service, fact.get("k", ""), fact.get("fastener_type", ""))
        if spec:
            _apply_spec_to_fact(fact, spec, service)

    # Attempt to enrich steps using spec library when torque placeholders remain.
    for step in steps:
        spec = _match_spec_entry(service, step.get("text", ""), step.get("fastener_type", ""))
        if spec:
            _apply_spec_to_step(step, spec, service)

    # Ensure torque conversions.
    for entry in steps + facts:
        if entry.get("torque_ft_lb") and not entry.get("torque_nm"):
            entry["torque_nm"] = round(float(entry["torque_ft_lb"]) * 1.35582, 1)
        if entry.get("torque_nm") and not entry.get("torque_ft_lb"):
            entry["torque_ft_lb"] = round(float(entry["torque_nm"]) / 1.35582, 1)

    def resolve_url(src: Any) -> Optional[str]:
        if src in (None, "", [], {}):
            return None
        if isinstance(src, list):
            for candidate in src:
                resolved = resolve_url(candidate)
                if resolved:
                    return resolved
            return None
        if isinstance(src, int):
            return existing_ref_map.get(src)
        if isinstance(src, str):
            stripped = src.strip()
            if not stripped:
                return None
            if stripped.isdigit():
                return existing_ref_map.get(int(stripped))
            return stripped
        return None

    def attach_ref(entry: Dict[str, Any], text_field: Optional[str] = None) -> None:
        src = entry.get("src")
        url = resolve_url(src) or entry.get("source") or entry.get("src_url") or entry.get("url")
        idx = tracker.add(url) or tracker.add("https://manual.swoopservice.com/verify")
        entry["src"] = idx
        entry["ref"] = idx
        if text_field and entry.get(text_field):
            entry[text_field] = _inject_sup(entry[text_field], idx)

    for step in steps:
        attach_ref(step, "text")
        if not step.get("n"):
            step["n"] = len(steps)

    for fact in facts:
        attach_ref(fact, "v")

    for note in notes:
        if isinstance(note, dict):
            attach_ref(note, "v")

    # Fill in missing spec facts from the library when absent.
    existing_keys = {fact.get("k") for fact in facts}
    for spec in SPEC_LIBRARY.get(service, []):
        if spec.get("id") in existing_keys:
            continue
        new_fact = {
            "k": spec.get("id"),
            "v": spec.get("value"),
            "torque_ft_lb": spec.get("torque_ft_lb"),
            "torque_nm": spec.get("torque_nm"),
            "spec_units": spec.get("spec_units"),
            "fastener_type": spec.get("fastener_type"),
            "src": spec.get("source"),
        }
        attach_ref(new_fact, "v")
        facts.append(new_fact)

    torque_specs = _ensure_list(data.get("torque_specs"))
    existing_components = {entry.get("component", "").lower() for entry in torque_specs if isinstance(entry, dict)}

    for spec in SPEC_LIBRARY.get(service, []):
        if not spec.get("torque_ft_lb") and not spec.get("torque_nm"):
            continue
        component = (spec.get("fastener_type") or spec.get("id") or "").strip()
        if component.lower() in existing_components:
            continue
        entry = {
            "component": component or spec.get("id"),
            "value": spec.get("value"),
            "torque_ft_lb": spec.get("torque_ft_lb"),
            "torque_nm": spec.get("torque_nm"),
            "notes": spec.get("notes"),
            "src": spec.get("source"),
        }
        attach_ref(entry, "value")
        torque_specs.append(entry)
        existing_components.add(component.lower())

    data["steps"] = steps
    data["facts"] = facts
    data["notes"] = notes
    if torque_specs:
        data["torque_specs"] = torque_specs
    for fact in facts:
        _register_spec_from_payload(service, fact, tracker, ["fastener_type", "component", "k"], "v")
    for spec_entry in torque_specs:
        _register_spec_from_payload(service, spec_entry, tracker, ["component", "fastener_type"], "value")
    data["refs"] = tracker.to_list()
    data["sources"] = tracker.urls()

    return data


def _iter_text_fields(payload: Dict[str, Any]) -> Iterable[str]:
    for step in payload.get("steps") or []:
        text = step.get("text")
        if text:
            yield text
    for fact in payload.get("facts") or []:
        value = fact.get("v")
        if value:
            yield value
    for note in payload.get("notes") or []:
        if isinstance(note, dict):
            value = note.get("v")
            if value:
                yield value
    for spec in payload.get("torque_specs") or []:
        value = spec.get("value")
        if value:
            yield value


def _count_placeholders(payload: Dict[str, Any]) -> int:
    count = 0
    for text in _iter_text_fields(payload):
        normalized = text.lower()
        if "verify" in normalized:
            count += 1
    return count


def _torque_components_from_payload(payload: Dict[str, Any]) -> Set[str]:
    components: Set[str] = set()
    for spec in payload.get("torque_specs") or []:
        component = (spec.get("component") or spec.get("fastener_type") or "").strip().lower()
        if component:
            components.add(component)
    for fact in payload.get("facts") or []:
        component = (fact.get("fastener_type") or fact.get("k") or "").strip().lower()
        if component and (fact.get("torque_ft_lb") or fact.get("torque_nm")):
            components.add(component)
    return components


def compute_quality_metrics(service: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    expected_components = {
        (spec.get("fastener_type") or spec.get("id") or "").strip().lower()
        for spec in SPEC_LIBRARY.get(service, [])
        if spec.get("torque_ft_lb") or spec.get("torque_nm")
    }
    expected_components.discard("")
    actual_components = _torque_components_from_payload(payload)
    expected_count = len(expected_components) or (1 if actual_components else 0)
    actual_count = len(actual_components)
    coverage = min(1.0, actual_count / expected_count) if expected_count else (1.0 if actual_count else 0.0)
    placeholders = _count_placeholders(payload)
    reference_list = payload.get("refs") or []
    missing_components = sorted(expected_components - actual_components)
    return {
        "torque_expected": expected_count,
        "torque_actual": actual_count,
        "torque_coverage": coverage,
        "placeholders": placeholders,
        "reference_count": len(reference_list),
        "missing_components": missing_components,
    }


def identify_missing_specs(service: str, payload: Dict[str, Any]) -> List[str]:
    metrics = compute_quality_metrics(service, payload)
    return metrics.get("missing_components", [])
