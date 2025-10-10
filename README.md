# Vehicles Dataset

This repository maintains a structured JSON dataset of North American vehicle makes, models, and common import entries for use in mobile mechanic workflows. Each record captures production spans from the earliest Chevrolet models of the 1910s through current EVs, powertrain combinations, drivetrain and body styles, plus maintenance-oriented metadata.

## JSON Schema

- `years`: Array of integers covering the model years sold in North America.
- `make`: Manufacturer name.
- `model`: Model name with generation or platform code when relevant.
- `engines`: Array of engine descriptions, including displacement, configuration, and notable output differences.
- `transmissions`: Array of transmission options offered for those model years.
- `region`: Region classification (`American`, `Canadian`, `Mexican`, `Japanese import`, etc.).
- `drivetrain`: Array of drivetrain layouts.
- `body_styles`: Array describing the body styles sold in the region.
- `hybrid` / `diesel`: Boolean flags indicating alternative propulsion availability.
- `difficulty_modifier`: Numeric labor multiplier; must be `>= 1.00`.
- `notes`: Important service insights or configuration clarifications.

## Contribution Rules

1. Use reliable sources, defaulting to Wikipedia vehicle pages for verification, and capture citations for future reference.
2. Maintain valid JSON formatting and keep field names consistent.
3. Ensure every `difficulty_modifier` is at least `1.00`; increase the value for complicated service scenarios (including brass-era restorations and high-voltage EV work) and justify the value in `notes`.
4. Reflect only documented North American configurations unless a common import variant is well established.
5. Avoid duplicate coverage of the same make/model/generation; create a new entry for each distinct generation instead of overwriting historic data.
6. Document any assumptions made and prefer leaving fields blank over guessing when data cannot be confirmed.
7. Keep `CHECKLIST.md`, `CHECKLIST_STATUS.md`, and `tracking.md` synchronized with the research you perform so the historical coverage roadmap stays accurate.

## Getting Started

- Review `CHECKLIST.md` for the decade-organized model roster per manufacturer and identify the next unchecked section.
- Use `CHECKLIST_STATUS.md` to mark when a manufacturer’s historical coverage audit is complete.
- Append new vehicle entries to `vehicles.json` following the schema and validate with `jq empty vehicles.json`.
