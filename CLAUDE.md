# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository maintains a comprehensive JSON dataset of North American vehicle makes, models, and specifications for a mobile mechanic pricing system. Coverage spans from brass-era vehicles (1910s) through current EVs, capturing production years, powertrains, drivetrain/body configurations, hybrid/diesel availability, and service complexity modifiers.

## Core Data Files

- `vehicles.json`: Primary dataset containing vehicle entries with years, make, model, engines, transmissions, drivetrain, body styles, hybrid/diesel flags, difficulty_modifier (≥1.00), and service notes
- `services.json`: Mobile mechanic service catalog with labor times, pricing ranges, and parts requirements (DO NOT modify unless explicitly instructed)
- `CHECKLIST.md`: Decade-organized manufacturer roster tracking which models have been researched and added
- `CHECKLIST_STATUS.md`: High-level tracker indicating which of the 37 manufacturers have completed historical audits
- `tracking.md`: Generation notes, hybrid/diesel availability matrix, and high-volume research priorities
- `NA.txt`: Canonical list of North American makes/models used as seed data

## JSON Validation

After any batch of additions to `vehicles.json`, always validate with:
```bash
jq empty vehicles.json
```

This ensures structural integrity and catches syntax errors before committing.

## Data Collection Workflow

1. **Source Selection**: Consult `CHECKLIST_STATUS.md` to identify the next manufacturer needing historical audit
2. **Research**: Use Wikipedia vehicle generation pages as the primary source; capture exact article URLs and revision dates for citations
3. **Entry Creation**:
   - Each distinct generation gets its own JSON object (do not overwrite historical data)
   - Set `difficulty_modifier` ≥ 1.00, scaling higher for brass-era vehicles (fragile construction, obsolete tooling), high-voltage EV systems, or complex service scenarios
   - Document rationale for elevated modifiers in the `notes` field
4. **Progress Tracking**: Update `CHECKLIST.md` checkboxes and `tracking.md` as models are completed
5. **Completion**: Mark manufacturer complete in `CHECKLIST_STATUS.MD` once all historical and current models are verified in `vehicles.json`

## Schema Requirements

- `years`: Array of integers (North American model years)
- `engines`: Array of descriptions including displacement, code, and notable output differences
- `transmissions`: Array with gear counts and transmission codes where available
- `drivetrain`: Array (FWD/RWD/AWD/4WD)
- `body_styles`: Array describing variants sold in North America
- `hybrid` / `diesel`: Boolean flags
- `difficulty_modifier`: Numeric (minimum 1.00); scale upward for service complexity
- `notes`: Service-critical details (timing chain/belt, HV battery isolation, specialty tools, etc.)

## Data Quality Standards

- Only use factual data verified against Wikipedia (primary source for this workflow)
- If information is ambiguous or missing, leave it out and create a TODO rather than guessing
- Preserve JSON insertion order to maintain change history clarity
- Ensure hybrid/diesel flags align with captured powertrain lists
- Record North American configurations only, unless a common import variant is well-established
- Avoid duplicates by scanning existing entries before adding new vehicles
- For brass-era and classic vehicles, use concise, era-appropriate field values

## Agent Rules Reference

The repository includes `AGENTS.md` and `PROMPT.md` that define the automated data collection loop for AI agents:
- Always cite Wikipedia sources with URLs and revision dates
- Update all tracking files (`CHECKLIST.md`, `CHECKLIST_STATUS.md`, `tracking.md`) synchronously with `vehicles.json`
- Validate difficulty modifiers ≥ 1.00 and document scaling rationale
- Preserve historical entries instead of overwriting when adding new generations

## Current Coverage Status

As of October 2025, Chevrolet has partial coverage including recent additions (Kingswood Estate, Monte Carlo generations, Malibu 5th–8th gens, Camaro 1st–5th gens, S-10 second gen, Tahoe GMT800/900/K2XX, plus numerous 2000s–2020s models). Other manufacturers are pending historical audits. Consult `tracking.md` for high-volume research priorities (F-150, Silverado/Sierra, RAV4, CR-V, etc.).
