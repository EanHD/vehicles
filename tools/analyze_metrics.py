#!/usr/bin/env python3
"""Summarize recent Swoop v2.3 quality and cost metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import Any, Dict, List


def _load_events(log_path: Path) -> List[Dict[str, Any]]:
    if not log_path.exists():
        return []
    events: List[Dict[str, Any]] = []
    with open(log_path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def _safe_mean(values: List[float]) -> float:
    return round(mean(values), 4) if values else 0.0


def summarize(log_path: Path) -> None:
    events = _load_events(log_path)
    docs = [event for event in events if event.get("kind") == "doc_generation"]
    heals = [event for event in events if event.get("kind") == "self_heal"]

    total_docs = len(docs)
    avg_cost = _safe_mean([event.get("cost_estimate_usd", 0.0) for event in docs])
    avg_coverage = _safe_mean([event.get("torque_coverage_percent", 0.0) for event in docs])
    avg_references = _safe_mean([event.get("reference_count", 0) for event in docs])
    avg_compression = _safe_mean([event.get("compression_ratio", 0.0) for event in docs])
    total_healed = sum(1 for event in docs if event.get("healed"))

    retry_in = sum((event.get("retry_tokens") or {}).get("sonar_in", 0) for event in docs)
    retry_out = sum((event.get("retry_tokens") or {}).get("sonar_out", 0) for event in docs)

    print("Swoop Data Metrics Summary")
    print("=" * 32)
    print(f"Log file: {log_path}")
    print(f"Total documents: {total_docs}")
    print(f"Self-heal retries: {len(heals)} events ({total_healed} docs healed)\n")
    print("Averages (doc_generation events)")
    print("-------------------------------")
    print(f"Avg cost (USD):         {avg_cost:.4f}")
    print(f"Avg torque coverage %:  {avg_coverage:.2f}")
    print(f"Avg references:         {avg_references:.2f}")
    print(f"Avg compression %:      {avg_compression:.2f}")
    print()
    print("Retry Tokens")
    print("-------------")
    print(f"Sonar retry prompt tokens:     {retry_in}")
    print(f"Sonar retry completion tokens: {retry_out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "log_file",
        nargs="?",
        default="cost_log.jsonl",
        help="Path to cost log JSONL file (default: cost_log.jsonl)",
    )
    args = parser.parse_args()
    summarize(Path(args.log_file))


if __name__ == "__main__":
    main()
