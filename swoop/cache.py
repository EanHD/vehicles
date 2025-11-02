"""Filesystem-backed cache for research payloads."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Optional, Tuple


CACHE_DIR = Path(os.getenv("SWOOP_CACHE_DIR", ".cache"))


def _hashed_path(key: str) -> Path:
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{digest}.json"


def get(key: str) -> Optional[dict[str, Any]]:
    """Return cached JSON data if present."""
    path = _hashed_path(key)
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (json.JSONDecodeError, OSError):
        return None


def set_(key: str, data: dict[str, Any]) -> Path:
    """Persist data to cache and return the file path."""

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _hashed_path(key)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
    return path


def _ensure_gzip_path(path: Path) -> Path:
    if path.suffix == ".gz":
        return path
    return path.with_suffix(path.suffix + ".gz")


def write_doc(path: Path, html: str) -> Tuple[Path, float]:
    """Write HTML content as gzip-compressed data and return path with compression ratio."""

    path = Path(path)
    target = _ensure_gzip_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    raw_bytes = html.encode("utf-8")
    with gzip.open(target, "wb") as handle:
        handle.write(raw_bytes)
    compressed_size = target.stat().st_size
    ratio = 0.0
    if raw_bytes:
        ratio = max(0.0, 1 - (compressed_size / len(raw_bytes)))
        ratio = round(ratio, 4)
    return target, ratio


def read_doc(path: Path) -> str:
    """Read HTML content, handling gzip compression transparently."""

    path = Path(path)
    attempt_paths = [path]
    if path.suffix != ".gz":
        attempt_paths.append(_ensure_gzip_path(path))

    for candidate in attempt_paths:
        if not candidate.exists():
            continue
        if candidate.suffix == ".gz":
            with gzip.open(candidate, "rt", encoding="utf-8") as handle:
                return handle.read()
        with open(candidate, "r", encoding="utf-8") as handle:
            return handle.read()
    raise FileNotFoundError(f"Document not found for paths: {attempt_paths}")
