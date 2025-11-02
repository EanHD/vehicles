#!/usr/bin/env python3
"""CLI utility to compare baseline and candidate service documents."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import re

from swoop.cache import read_doc
from swoop.quality import evaluate_quality


SECTION_PATTERN = re.compile(r"<h[12][^>]*>(.*?)</h[12]>", re.I | re.S)


def _extract_sections(html: str) -> set[str]:
    return {re.sub(r"\s+", " ", match.strip()) for match in SECTION_PATTERN.findall(html or "")}


def compare_docs(baseline_path: Path, candidate_path: Path) -> int:
    baseline_text = read_doc(baseline_path)
    candidate_text = read_doc(candidate_path)

    report = evaluate_quality(candidate_text, baseline_text)

    baseline_sections = _extract_sections(baseline_text)
    candidate_sections = _extract_sections(candidate_text)

    missing_sections = baseline_sections - candidate_sections
    new_sections = candidate_sections - baseline_sections

    print(f"Comparing baseline={baseline_path} candidate={candidate_path}")
    print(f"- Missing references: {sorted(report.missing_references) or 'none'}")
    print(f"- Torque coverage: {report.torque_ratio*100:.1f}% of baseline")
    if report.verify_placeholders:
        print(f"- Verify placeholders present: {len(report.verify_placeholders)}")
    else:
        print("- Verify placeholders present: none")
    if missing_sections:
        print(f"- Sections missing from candidate: {sorted(missing_sections)}")
    if new_sections:
        print(f"- New sections in candidate: {sorted(new_sections)}")

    if report.is_pass():
        print("✅ Candidate meets quality thresholds.")
        return 0

    print("❌ Candidate failed quality checks.")
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path, help="Path to baseline HTML document")
    parser.add_argument("candidate", type=Path, help="Path to candidate HTML document")
    args = parser.parse_args(argv)

    if not args.baseline.exists():
        print(f"Baseline file not found: {args.baseline}", file=sys.stderr)
        return 2
    if not args.candidate.exists():
        print(f"Candidate file not found: {args.candidate}", file=sys.stderr)
        return 2

    return compare_docs(args.baseline, args.candidate)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
