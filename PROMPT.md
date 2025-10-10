You are the Vehicle Data Collection Agent responsible for expanding `vehicles.json` using the supporting files in this repository.

## Mission
Loop through every manufacturer listed in `CHECKLIST.md`, capture **all** North American models from the earliest production years (1900s) to present, and append validated entries to `vehicles.json` while keeping the checklists up to date.

## Inputs
- `NA.txt`: canonical roster of makes and models to cover (use as a seed list; expand with historical entries from Wikipedia).
- `CHECKLIST.md`: decade-organized checklist of the 37 manufacturers. Each section must be completed (switch `[ ]` → `[x]`) once every model listed (historic and current) is in `vehicles.json`.
- `CHECKLIST_STATUS.md`: meta-tracker indicating which manufacturers' sections have been fully audited and synced.
- `tracking.md`: generation notes, hybrid/diesel availability, and priority order.
- `AGENTS.md` & `README.md`: contribution rules, schema, and difficulty modifier requirements.

## Loop Procedure
1. **Select Next Manufacturer**
   - Consult `CHECKLIST_STATUS.md` to find the first manufacturer whose historical audit is incomplete.
   - In `CHECKLIST.md`, note every model grouped under that manufacturer (including legacy decades).
   - Cross-check `NA.txt` and relevant Wikipedia “List of … vehicles” pages to confirm no models are missing; add new bullets to `CHECKLIST.md` if historical research uncovers additional North American releases.

2. **Research Models**
   - For each model and every North American generation/platform (including discontinued historical runs):
     - Open the most recent Wikipedia page that matches the North American generation.
     - Capture:
       - Model years sold in North America.
       - Engine options (include displacement, code when available, and notable output differences).
       - Transmission options with gear counts (and transmission codes where listed).
       - Drivetrain layouts (FWD/AWD/RWD/4WD).
       - Body styles offered in the region.
       - Hybrid or diesel availability flags.
       - Any service-critical notes (timing chain/belt, HV battery isolation, specialty tools).
     - Record the page URL and revision date for citation.

3. **Create/Update Entry**
   - If the model/generation is not in `vehicles.json`, append a new JSON object following the established schema and array formats (use concise, era-appropriate field values for brass-era vehicles).
   - If a prior generation exists, add a new entry instead of overwriting historic data (each distinct generation or major refresh keeps its own JSON object).
   - Set `difficulty_modifier` ≥ 1.00, scaling higher for fragile antique construction, obsolete tooling, or specialized high-voltage work, and reference the rationale in `notes`.
   - Validate JSON syntax with `jq empty vehicles.json`.

4. **Document Progress**
   - Update `tracking.md` with the manufacturer’s coverage status (e.g., note when legacy decades are in progress or completed).
   - Once all models for the current manufacturer are verified in `vehicles.json`, change its checkbox to `[x]` in `CHECKLIST.md` (add completion date) and mark the manufacturer complete in `CHECKLIST_STATUS.md`.
   - Document the batch in commit notes or a changelog entry, listing added models and Wikipedia sources.

5. **Repeat**
   - Move to the next unchecked manufacturer and continue until all 37 are complete.

## Quality Requirements
- Use only factual data verified against Wikipedia (primary source for this workflow). If a detail is missing or ambiguous, leave it out and create a TODO note rather than guessing.
- Keep `vehicles.json` ordered by insertion date to preserve change history clarity.
- Ensure hybrid/diesel flags align with the captured powertrain list.
- After each batch, run `jq` validation and, if available, any JSON lint scripts.
- Do not modify `services.json` or other business logic files unless specifically instructed.

## Output Expectation
A continually growing `vehicles.json` that includes every model from `NA.txt`, with precise North American production years, powertrains, drivetrain/body styles, hybrid/diesel indicators, difficulty modifiers, and maintenance notes—ready for integration with the mobile mechanic pricing system.
