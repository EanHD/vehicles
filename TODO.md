# Vehicle Dataset Coverage Checklist

- [ ] Populate `NA.txt` with the canonical list of North American makes/models (domestic brands, Canadian/Mexican divisions, and common imports) or replace it with an automated scrape output; eliminate duplicates and normalize naming to match Wikipedia article titles.
- [ ] Reconcile `NA.txt` against `na_manufacturing.json` and `List_of_US_automobiles.html` to confirm no marques or models are missing; log any gaps that need manual research.
- [ ] For each manufacturer in the consolidated list, create a tracking table noting generation/platform codes, North American production years, and whether hybrid/diesel trims exist.
- [ ] Prioritize the highest-volume service candidates (full-size pickups, compact crossovers, popular sedans) and document the research order so critical coverage lands first.
- [ ] When researching a model, pull powertrain, drivetrain, body-style, and transmission data directly from the corresponding Wikipedia generation page; capture the citation URL and revision date.
- [ ] Record service-impact notes (e.g., timing chain access, hybrid battery placement, AWD serviceability) and assign a `difficulty_modifier` ≥ 1.00 before committing the entry to `vehicles.json`.
- [ ] Run `jq` validation and lint checks on `vehicles.json` after every batch of additions to ensure structural integrity and consistent field ordering.
- [ ] Cross-reference new `difficulty_modifier` values with `services.json` labor times to flag vehicles that may require custom pricing adjustments.
- [ ] Maintain a change log (commit messages or separate journal) listing which models were added, their source citations, and any pending follow-up data.
