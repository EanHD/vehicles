# CLAUDE.md - Vehicle Dataset Workflow

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🎯 IMMEDIATE ACTION: First Thing To Do

**When you start or resume work, ALWAYS run this command first:**

```bash
cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
```

**This ONE file tells you:**
- ✅ What's complete
- 🔄 What's in progress
- ⏳ What's validated and ready to append
- ❌ What hasn't been started
- 📍 Exactly which phase to continue

**Don't explore. Don't guess. Read the progress tracker first!**

## Repository Purpose

This repository maintains a comprehensive JSON dataset of North American vehicle makes, models, and specifications for a mobile mechanic pricing system. Coverage spans from brass-era vehicles (1910s) through current EVs, capturing production years, powertrains, drivetrain/body configurations, hybrid/diesel availability, and service complexity modifiers.

## 🚨 CRITICAL WORKFLOW RULES

### ❌ NEVER Do These Things:
- **DON'T** use Read tool on `vehicles.json` (too large - causes token waste)
- **DON'T** append directly to `vehicles.json` (corrupts production data)
- **DON'T** work without `PROGRESS_TRACKER.md` (you WILL lose track)
- **DON'T** skip `jq empty` validation before merging (catches errors)
- **DON'T** skip backup before appending (no recovery if something breaks)
- **DON'T** guess at data if Wikipedia is unclear (leave it out instead)

### ✅ ALWAYS Do These Things:
- **DO** use grep/jq/sed for `vehicles.json` queries (fast, efficient, no token waste)
- **DO** create isolated decade files in `wip/[manufacturer]/[decade].json` (organized)
- **DO** maintain `PROGRESS_TRACKER.md` with real-time updates (stay on track)
- **DO** validate every decade file with `jq empty` before proceeding (catch errors early)
- **DO** backup `vehicles.json` before every merge (safety net)
- **DO** cite Wikipedia with revision dates in notes (quality standard)

## Core Data Files

- **vehicles.json**: Primary dataset containing vehicle entries with years, make, model, engines, transmissions, drivetrain, body styles, hybrid/diesel flags, difficulty_modifier (≥1.00), and service notes
  - **DO NOT READ DIRECTLY** - Use grep/jq for queries
- **services.json**: Mobile mechanic service catalog with labor times, pricing ranges, and parts requirements (DO NOT modify unless explicitly instructed)
- **CHECKLIST.md**: Decade-organized manufacturer roster tracking which models have been researched and added
- **CHECKLIST_STATUS.md**: High-level tracker indicating which of the 37 manufacturers have completed historical audits
- **PROMPT.md**: Complete workflow documentation - READ THIS for comprehensive instructions
- **WORKFLOW.md**: Step-by-step procedures for the 5-phase workflow
- **AGENTS.md**: Agent-specific rules and guidelines
- **tracking.md**: Generation notes, hybrid/diesel availability matrix, and high-volume research priorities
- **NA.txt**: Canonical list of North American makes/models used as seed data

## The 5-Phase Workflow (Follow Exactly)

### Phase 1: Setup & Gap Analysis
**Goal**: Create workspace and identify what needs research

```bash
# Create working directory
mkdir -p wip/[manufacturer]

# Create progress tracker (MANDATORY!)
touch wip/[manufacturer]/PROGRESS_TRACKER.md
```

**PROGRESS_TRACKER.md Must Include:**
- Status table with emoji indicators (⏳ TODO | 🔄 IN PROGRESS | ✅ DONE)
- Per-decade model lists with checkboxes
- Wikipedia URLs with revision dates
- Current vehicles.json count for manufacturer

**Check Current Coverage (use grep, NOT Read):**
```bash
# Count existing entries
grep -c '"make": "GMC"' vehicles.json

# List existing models
grep -A 1 '"make": "GMC"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq
```

### Phase 2: Decade-by-Decade Research
**Goal**: Research models in isolated, manageable batches

```bash
# Create decade file
touch wip/[manufacturer]/2020s.json
```

**For EVERY Model, Capture ALL Required Fields:**

```json
{
  "years": [2022, 2023, 2024, 2025],
  "make": "GMC",
  "model": "Hummer EV Pickup (SUT)",
  "engines": ["EV3X: 3 electric motors (1,000 hp)", "EV2X/EV2: 2 electric motors (625 hp)"],
  "transmissions": ["Single-speed electric drive"],
  "region": "American",
  "drivetrain": ["AWD"],
  "body_styles": ["4-door electric pickup truck"],
  "hybrid": false,
  "diesel": false,
  "difficulty_modifier": 1.4,
  "notes": "All-electric Hummer EV features Ultium battery platform with up to 246.8 kWh total capacity. High-voltage system (400V/800V switchable) demands EV-certified technicians. CrabWalk four-wheel steering requires specialized diagnostic equipment. Data sourced from Wikipedia GMC Hummer EV article, December 19, 2024 revision."
}
```

**Difficulty Modifier Scale:**
- `1.0` = Standard modern vehicle
- `1.1` = Diesel, basic hybrid, complex service access
- `1.2` = Brass-era (1910s-1920s), turbo performance, medium-duty commercial
- `1.3` = Heavy-duty commercial, air brakes, complex vintage
- `1.4+` = High-voltage EVs (400V+), switchable voltage platforms

**MUST justify all modifiers >= 1.1 in notes!**

**Research Process:**
1. Find Wikipedia generation-specific page
2. Capture all required fields (don't skip any!)
3. Update PROGRESS_TRACKER.md in real-time
4. Validate: `jq empty wip/[manufacturer]/[decade].json`

### Phase 3: Validation & Quality Checks
**Goal**: Ensure accuracy before appending to production dataset

**Validation Checklist (per decade):**
- [ ] All models researched with Wikipedia citations
- [ ] JSON validates: `jq empty wip/[manufacturer]/[decade].json`
- [ ] All difficulty_modifier >= 1.00 with justification in notes
- [ ] All required fields present (years, engines, transmissions, etc.)
- [ ] No duplicate entries within decade file
- [ ] Hybrid/diesel flags match captured powertrains
- [ ] Body styles reflect North American market only
- [ ] Notes include Wikipedia citation with revision date
- [ ] Platform sharing documented where relevant (GMT400, Lambda, etc.)

**When Complete:**
Update PROGRESS_TRACKER.md status to `⏳ READY`

### Phase 4: Batch Append to vehicles.json
**Goal**: Safely merge validated decade data into production dataset

**CRITICAL: Only append after ALL target decades are validated!**

```bash
# STEP 1: BACKUP (NEVER SKIP!)
cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)

# STEP 2: MERGE multiple decades at once
jq -s '.[0] + .[1] + .[2] + .[3] + .[4]' \
  vehicles.json \
  wip/gmc/1980s.json \
  wip/gmc/1990s.json \
  wip/gmc/2000s.json \
  wip/gmc/2010s.json \
  wip/gmc/2020s.json \
  > vehicles_temp.json

mv vehicles_temp.json vehicles.json

# STEP 3: VALIDATE merged file (CRITICAL!)
jq empty vehicles.json
# If this fails, RESTORE FROM BACKUP IMMEDIATELY

# STEP 4: VERIFY entry count
grep -c '"make": "GMC"' vehicles.json

# STEP 5: ARCHIVE completed decade files
cd wip/gmc
for decade in 1980s 1990s 2000s 2010s 2020s; do
  mv ${decade}.json ${decade}_APPENDED.json
done

# STEP 6: UPDATE PROGRESS_TRACKER.md
# Change ⏳ READY to ✅ APPENDED
# Update current vehicles.json count
```

### Phase 5: Manufacturer Completion
**Goal**: Finalize manufacturer and prepare for next

1. Create completion report (see `GMC_PHASE1_COMPLETION_REPORT.md` example)
2. Update `CHECKLIST.md` status note with completion date
3. Update `CHECKLIST_STATUS.md` (ONLY when manufacturer is 100% complete)
4. Move to next manufacturer

## Schema Requirements

All entries must include these fields:

- **years**: Array of integers (North American model years)
- **make**: Manufacturer name (e.g., "GMC", "Chevrolet", "Ford")
- **model**: Model name with generation/platform code (e.g., "Sierra (GMT400)", "Corvette (C8)")
- **engines**: Array of descriptions including displacement, code, and notable output differences
  - Example: `["5.7L V8 (350 hp)", "6.2L V8 (460 hp)", "3.0L Turbo Diesel I6 (277 hp)"]`
- **transmissions**: Array with gear counts and transmission codes where available
  - Example: `["6-speed manual", "8-speed automatic", "10-speed automatic"]`
- **region**: "American", "Canadian", "Mexican", "Japanese import", "European import"
- **drivetrain**: Array (FWD/RWD/AWD/4WD)
  - Example: `["2WD", "4WD"]`, `["RWD"]`, `["FWD", "AWD"]`
- **body_styles**: Array describing variants sold in North America
  - Example: `["Regular Cab", "Extended Cab", "Crew Cab"]`, `["2-door coupe", "2-door convertible"]`
- **hybrid**: Boolean flag (true/false)
- **diesel**: Boolean flag (true/false)
- **difficulty_modifier**: Numeric (minimum 1.00); scale upward for service complexity
- **notes**: Service-critical details (timing chain/belt, HV battery isolation, specialty tools, etc.) + Wikipedia citation with revision date

**Wikipedia Citation Format (REQUIRED):**
```
"Data sourced from Wikipedia [Article Name] article, December 19, 2024 revision."
```

## Tool Usage Best Practices

### Large File Handling
**vehicles.json is too large to read directly.** Use these techniques:

```bash
# Count entries for a manufacturer
grep -c '"make": "GMC"' vehicles.json

# List all models for a manufacturer
grep -A 1 '"make": "GMC"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Search for specific model
grep '"model": "Sierra"' vehicles.json

# Extract specific manufacturer's entries (use cautiously, can be large)
jq '[.[] | select(.make == "GMC")]' vehicles.json > gmc_entries.json
```

### JSON Validation Commands

```bash
# Validate single decade file
jq empty wip/gmc/2020s.json

# Validate production dataset
jq empty vehicles.json

# Count entries in decade file
jq 'length' wip/gmc/2020s.json

# Pretty-print for review
jq . wip/gmc/2020s.json
```

### Backup Before Merge (CRITICAL)

**NEVER skip this step:**
```bash
cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)
```

If validation fails after merge, restore immediately:
```bash
mv vehicles.json.backup_[timestamp] vehicles.json
```

## Data Quality Standards

### Factual Accuracy
- Use **ONLY Wikipedia** as primary source for this workflow
- If information is ambiguous or missing, **leave it out** and create a TODO note rather than guessing
- Record **exact Wikipedia URLs with revision dates** in PROGRESS_TRACKER.md and notes fields
- Cross-reference platform-shared models (GMT400, Lambda, T1XX, etc.) for engine/transmission consistency

### JSON Integrity
- Keep `vehicles.json` ordered by insertion date to preserve change history clarity
- Ensure hybrid/diesel flags align with captured powertrain lists
- Use arrays for all multi-valued fields (engines, transmissions, drivetrain, body_styles)
- Each distinct generation gets its own JSON object (do not overwrite historical data)

### Documentation Standards
- All difficulty_modifier values must have justification in notes field
- All entries must cite Wikipedia source with revision date
- Platform sharing should be documented (e.g., "GMT400 platform shared with Chevrolet Silverado")
- Service-critical details required: timing chain/belt, HV battery isolation, specialty tools, air brakes, etc.

### Validation Requirements
- After each decade file: `jq empty wip/[manufacturer]/[decade].json`
- After merging to vehicles.json: `jq empty vehicles.json`
- **If validation fails, restore from backup immediately**
- Verify entry counts match expected totals

## Platform Sharing Documentation

Many vehicles share platforms. Document this in notes field:

**GM Truck Platforms (Chevrolet/GMC):**
- GMT400 (1988-1998): Sierra/Silverado, full-size pickups
- GMT800 (1999-2006): Sierra/Silverado, Yukon/Tahoe
- GMT900 (2007-2013): Sierra/Silverado light-duty trucks
- K2XX (2014-2020): Sierra/Silverado, Yukon/Tahoe generation
- T1XX (2019-present): Current Sierra/Silverado, Yukon/Tahoe
- GMT355 (2004-2012): Canyon/Colorado midsize pickups
- GMT360 (2002-2009): Envoy/TrailBlazer SUV platform
- Lambda (2007-2016): Acadia/Traverse/Enclave crossovers
- Theta (2010-2017): Terrain/Equinox compact crossovers

**Cross-reference these platforms for engine/transmission consistency.**

## Resuming Work in New Conversation

If you're starting a new conversation and continuing work:

1. **Read PROGRESS_TRACKER.md FIRST**
   ```bash
   cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
   ```
   This shows exactly what's complete and what's pending.

2. **Check the "Appended" column**
   - ✅ APPENDED: Decade is complete and merged
   - ⏳ READY: Decade is validated and ready to append
   - 🔄 IN PROGRESS: Decade research is ongoing
   - ❌: Decade not started

3. **Identify your next action**
   - If decades show `⏳ READY`: Proceed to Phase 4 (Batch Append)
   - If decade shows `🔄 IN PROGRESS`: Continue research for that decade
   - If all show `✅ APPENDED`: Create completion report or start next manufacturer

4. **Verify context**
   ```bash
   # Check current vehicles.json count
   grep -c '"make": "[Manufacturer]"' vehicles.json

   # Verify decade files exist
   ls -la wip/[manufacturer]/*.json
   ```

5. **Continue where left off**
   - Follow the phase indicated in PROGRESS_TRACKER.md
   - Update progress tracker as you work
   - Maintain same organization standards

## Reference Files (Examples)

- **wip/gmc/PROGRESS_TRACKER.md** - Complete tracking example with emoji indicators
- **GMC_PHASE1_COMPLETION_REPORT.md** - Phase 1 completion documentation
- **CHEVROLET_COMPLETION_REPORT.md** - Full manufacturer completion example
- **CHEVROLET_GAP_ANALYSIS.md** - Gap analysis workflow example
- **wip/gmc/2020s_APPENDED.json** - Validated and archived decade file

## Current Coverage Status

As of December 2024:
- **Chevrolet**: Partial coverage with recent additions (multiple generations complete)
- **GMC**: Phase 1 (1980s-2020s) + Phase 2 (1910s-1970s) COMPLETE - 55 entries
- **Other manufacturers**: Pending historical audits

Consult `CHECKLIST_STATUS.md` for current manufacturer status and `tracking.md` for high-volume research priorities.

## Quick Decision Tree

**Just started?** → Read PROGRESS_TRACKER.md first
**Status shows ⏳ READY?** → Go to Phase 4 (Batch Append)
**Status shows 🔄 IN PROGRESS?** → Continue research for that decade
**Status shows ✅ APPENDED?** → Create completion report or start next manufacturer
**No PROGRESS_TRACKER.md exists?** → Start Phase 1 (Setup & Gap Analysis)

## ⚡ Speed Optimization Strategies

### When Working Under Token/Time Constraints

**The Hyundai Strategy**: Complete manufacturers efficiently while maintaining quality notes:

1. **Batch WebFetch calls** - Request multiple Wikipedia pages in parallel in a single message
   - Example: Sonata, Elantra, Tucson, Santa Fe, Kona, Ioniq in one go
   - Saves round-trips and tokens

2. **Streamlined notes format** - Concise but complete:
   ```
   "notes": "Fourth generation NX4 (2020-present). 1.6L T-GDi engine with electric motor, 13.8 kWh battery. AWD standard. Requires PHEV-certified technicians for high-voltage system. Data sourced from Wikipedia Hyundai Tucson article, January 2025 revision."
   ```
   - Generation identifier (e.g., "Fourth generation NX4")
   - Key technical specs (engine, battery, powertrain)
   - Service complexity rationale (when modifier ≥ 1.1)
   - Wikipedia citation with revision date
   - **No fluff, all substance**

3. **Compact JSON structure** - Keep entries minimal but complete:
   ```json
   {"years": [2020, 2021, 2022, 2023, 2024, 2025], "make": "Hyundai", "model": "Tucson PHEV (NX4 PHEV)", "engines": ["1.6L T-GDi I4 turbo + electric motor"], "transmissions": ["6-speed automatic"], "region": "American", "drivetrain": ["AWD"], "body_styles": ["4-door compact crossover SUV"], "hybrid": true, "diesel": false, "difficulty_modifier": 1.3, "notes": "Fourth generation plug-in hybrid. 1.6L T-GDi engine with electric motor, 13.8 kWh lithium-ion battery. AWD standard. Requires PHEV service expertise for high-voltage battery system. Data sourced from Wikipedia Hyundai Tucson article, January 2025 revision."}
   ```
   - Single-line entries save visual space
   - Array format for easy bulk creation

4. **Rapid validation workflow**:
   ```bash
   # Validate all decades at once
   for decade in 1980s 1990s 2000s 2010s 2020s; do
     jq empty wip/hyundai/${decade}.json && echo "✓ $decade"
   done

   # Merge all in one command
   jq -s '.[0] + .[1] + .[2] + .[3] + .[4] + .[5]' vehicles.json wip/hyundai/{1980s,1990s,2000s,2010s,2020s}.json > vehicles_temp.json && mv vehicles_temp.json vehicles.json
   ```

5. **Focus on high-volume models** - Prioritize major nameplates:
   - Sedans: Sonata, Elantra, Accent
   - SUVs: Tucson, Santa Fe, Palisade, Kona
   - EVs: Ioniq variants, Ioniq 5, Ioniq 6
   - Skip rare/specialty variants if time-limited

6. **Generation-aware research** - One Wikipedia lookup per generation:
   - Elantra CN7 (2020-present) → covers all 2020s years
   - Tucson NX4 (2020-present) → covers all 2020s years
   - Avoid redundant lookups for same generation

### Quality Benchmarks (Even When Fast)

**Non-negotiable elements**:
- ✅ All 12 required JSON fields present
- ✅ Wikipedia citation with "January 2025 revision" format
- ✅ Difficulty modifier justification when ≥ 1.1
- ✅ Generation identifier in model name or notes (e.g., "DN8", "CN7", "NX4")
- ✅ Key technical specs that impact service (battery size, voltage, hybrid system type)

**Can be streamlined**:
- ⚡ Single-sentence notes instead of paragraphs
- ⚡ Compact engine descriptions: "1.6L T-GDi I4 turbo" vs. "1.6-liter turbocharged Gamma gasoline direct injection inline-four"
- ⚡ Combined variant entries when identical except powertrain (gasoline/hybrid/PHEV)

### Result: Hyundai Case Study
- **43 entries** in 5 decades (1986-2025)
- **All validated**, **all with proper notes**, **all with Wikipedia citations**
- **Completed in < 30 tool calls** while maintaining quality standards
- Average note length: ~100-150 words (concise but complete)

## Common Pitfalls to Avoid

### ❌ DON'T
- Read entire vehicles.json file (token waste)
- Append directly to vehicles.json without validation
- Research models without creating wip/ directory structure
- Skip PROGRESS_TRACKER.md (you will lose track)
- Guess at data when Wikipedia is unclear
- Overwrite historical generations with newer data
- Skip backup before merging to vehicles.json
- Mark manufacturer complete in CHECKLIST_STATUS.md if any decades are pending
- **Write verbose notes when concise notes suffice**
- **Make redundant Wikipedia lookups for same generation**

### ✅ DO
- Use grep/jq for targeted vehicles.json queries
- Create isolated decade files in wip/ directory
- Maintain real-time PROGRESS_TRACKER.md updates
- Validate each decade file before proceeding
- Document Wikipedia sources with revision dates
- Preserve each generation as separate JSON entry
- Backup vehicles.json before every merge
- Archive completed decade files with `_APPENDED` suffix
- Create completion reports for reference
- **Batch WebFetch calls in parallel when researching multiple models**
- **Write concise, technical notes with all required elements**
- **Use generation identifiers to avoid redundant research**

## Remember

- **Organization prevents chaos** - Use the wip/ directory workflow
- **Tracking prevents loss** - Update PROGRESS_TRACKER.md constantly
- **Validation prevents corruption** - Check with jq before every merge
- **Backup prevents disasters** - Always backup before appending
- **Documentation prevents confusion** - Cite Wikipedia with revision dates

**When in doubt, follow PROMPT.md. Don't skip steps. Always validate.**

## Your First Command Every Time

```bash
cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
```

**This tells you EXACTLY what to do next. Follow it!**
