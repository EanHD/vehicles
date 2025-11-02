"""Quality regression checks for generated HTML documents."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Set


SUP_PATTERN = re.compile(r"<sup[^>]*>\[(\d+)\]</sup>", re.I)
REF_PATTERN = re.compile(r"<li[^>]*>\[(\d+)\]", re.I)
TORQUE_PATTERN = re.compile(r"\b\d+\s*(?:ft-?lb|ft/lb|nm|n·m)\b", re.I)
VERIFY_PATTERN = re.compile(r"verify torque", re.I)


@dataclass
class QualityReport:
    missing_references: Set[int]
    torque_ratio: float
    verify_placeholders: List[str]

    def is_pass(self) -> bool:
        return not self.missing_references and self.torque_ratio >= 0.8 and not self.verify_placeholders


def _extract_reference_indices(html: str) -> Set[int]:
    return {int(match.group(1)) for match in SUP_PATTERN.finditer(html)}


def _extract_reference_targets(html: str) -> Set[int]:
    return {int(match.group(1)) for match in REF_PATTERN.finditer(html)}


def _count_torque_mentions(html: str) -> int:
    return len(TORQUE_PATTERN.findall(html or ""))


def _collect_verify_placeholders(html: str) -> List[str]:
    return VERIFY_PATTERN.findall(html or "")


def evaluate_quality(candidate_html: str, baseline_html: str) -> QualityReport:
    """Compare candidate HTML against baseline for reference and spec coverage."""

    sup_indices = _extract_reference_indices(candidate_html or "")
    ref_targets = _extract_reference_targets(candidate_html or "")
    missing = sup_indices - ref_targets

    baseline_torque = max(1, _count_torque_mentions(baseline_html))
    candidate_torque = _count_torque_mentions(candidate_html)
    torque_ratio = candidate_torque / baseline_torque

    verify_flags = _collect_verify_placeholders(candidate_html)

    return QualityReport(
        missing_references=missing,
        torque_ratio=torque_ratio,
        verify_placeholders=verify_flags,
    )
