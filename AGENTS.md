# Vehicle Dataset Agent Rules

- Always source vehicle information from reliable references, prioritizing Wikipedia vehicle generation pages and citing the exact article in commit notes or documentation (note the revision date when possible).
- Capture production years, make, model (including generation/platform codes), engine options, transmission options, drivetrain layouts, body styles, hybrid/diesel availability, and notable service notes relevant to a mobile mechanic—even for brass-era and classic vehicles.
- Verify that `difficulty_modifier` values are never below `1.00`; scale upward for complex service procedures, high-voltage systems, or fragile antique construction, and document the rationale in the `notes` field.
- Record engines and transmissions exactly as sold in North America unless a clearly documented import configuration is common in the region.
- Add only factual entries; if information cannot be confirmed, create a TODO item and exclude the detail until an authoritative source is found.
- Preserve JSON validity: use arrays for multi-valued fields and keep property names consistent across entries.
- Before adding new vehicles, scan for existing duplicates to avoid overlapping coverage of the same make/model/generation.
- Update `CHECKLIST.md`, `CHECKLIST_STATUS.md`, and `tracking.md` as you progress so historical coverage status stays synchronized with `vehicles.json`.
