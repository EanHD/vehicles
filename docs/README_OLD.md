# Vehicles Dataset

This repository maintains a structured JSON dataset of North American vehicle makes, models, and common import entries for use in mobile mechanic workflows. Each record captures production spans from the earliest Chevrolet models of the 1910s through current EVs, powertrain combinations, drivetrain and body styles, plus maintenance-oriented metadata.

## Quick Start for New Contributors

**IMPORTANT**: Before contributing, read `WORKFLOW.md` for the complete decade-based research process. This prevents token waste and ensures data integrity.

### First Steps
1. Read `PROMPT.md` - Comprehensive agent instructions and workflow
2. Read `WORKFLOW.md` - Step-by-step research procedures
3. Check `CHECKLIST_STATUS.md` - See which manufacturers need work
4. Review `wip/[manufacturer]/PROGRESS_TRACKER.md` - See current progress

### Core Principle
**NEVER append directly to `vehicles.json`.** Always use the isolated decade-based workflow in the `wip/` directory.

## Repository Structure

```
vehicles/
├── vehicles.json                    # Production dataset (use grep/jq, don't read directly)
├── CHECKLIST.md                     # Decade-organized model roster (37 manufacturers)
├── CHECKLIST_STATUS.md              # High-level manufacturer completion tracker
├── PROMPT.md                        # Complete agent instructions and workflow
├── WORKFLOW.md                      # Step-by-step research procedures
├── AGENTS.md                        # Agent-specific rules and guidelines
├── tracking.md                      # Generation notes, priorities
├── wip/                             # Work-in-progress organized by manufacturer
│   ├── chevrolet/
│   │   ├── PROGRESS_TRACKER.md     # Real-time progress tracking
│   │   ├── 1980s_APPENDED.json     # Archived completed decade files
│   │   ├── 1990s_APPENDED.json
│   │   └── ...
│   ├── gmc/
│   │   ├── PROGRESS_TRACKER.md
│   │   ├── 2020s_APPENDED.json
│   │   └── ...
│   └── [other manufacturers]/
├── CHEVROLET_GAP_ANALYSIS.md       # Gap analysis examples
├── GMC_PHASE1_COMPLETION_REPORT.md # Completion report examples
└── README.md                        # This file
```

## JSON Schema

Each vehicle entry in `vehicles.json` follows this schema:

### Required Fields

- **`years`**: Array of integers covering the model years sold in North America
  - Example: `[2020, 2021, 2022, 2023, 2024]`

- **`make`**: Manufacturer name (string)
  - Example: `"Chevrolet"`, `"GMC"`, `"Ford"`

- **`model`**: Model name with generation or platform code when relevant
  - Example: `"Corvette (C8)"`, `"Sierra (GMT400)"`, `"F-150 (14th generation)"`

- **`engines`**: Array of engine descriptions, including displacement, configuration, and notable output differences
  - Example: `["5.7L V8 (350 hp)", "6.2L V8 (460 hp)", "3.0L Turbo Diesel I6 (277 hp)"]`

- **`transmissions`**: Array of transmission options offered for those model years
  - Example: `["6-speed manual", "8-speed automatic", "10-speed automatic"]`

- **`region`**: Region classification
  - Options: `"American"`, `"Canadian"`, `"Mexican"`, `"Japanese import"`, `"European import"`, etc.

- **`drivetrain`**: Array of drivetrain layouts
  - Options: `["FWD"]`, `["RWD"]`, `["AWD"]`, `["4WD"]`, `["2WD", "4WD"]`, etc.

- **`body_styles`**: Array describing the body styles sold in the region
  - Example: `["2-door coupe", "2-door convertible"]`, `["Regular Cab", "Extended Cab", "Crew Cab"]`

- **`hybrid`**: Boolean flag indicating hybrid availability
  - `true` or `false`

- **`diesel`**: Boolean flag indicating diesel availability
  - `true` or `false`

- **`difficulty_modifier`**: Numeric labor multiplier; must be `>= 1.00`
  - **Guidelines**:
    - `1.0`: Standard modern vehicle
    - `1.1`: Complex service access, diesel engines, basic hybrid systems
    - `1.2`: Brass-era vehicles (1910s-1920s), turbocharged performance, medium-duty commercial
    - `1.3`: Heavy-duty commercial trucks, air brake systems, complex vintage
    - `1.4+`: High-voltage EV systems (400V+), switchable voltage platforms
  - **MUST be justified in the `notes` field**

- **`notes`**: Important service insights, configuration clarifications, and Wikipedia citation
  - Must include: Service-critical details (timing chain/belt, HV isolation, specialty tools)
  - Must include: Wikipedia source with revision date
  - Example: `"GMT400 Sierra features independent front suspension on 4WD models. Optional 6.2L Detroit Diesel requires specialized diagnostic tools. Data sourced from Wikipedia GMC Sierra article, October 11, 2025 revision."`

### Example Entry

```json
{
  "years": [2022, 2023, 2024, 2025],
  "make": "GMC",
  "model": "Hummer EV Pickup (SUT)",
  "engines": [
    "EV3X: 3 electric motors (1,000 hp)",
    "EV2X/EV2: 2 electric motors (625 hp)"
  ],
  "transmissions": ["Single-speed electric drive"],
  "region": "American",
  "drivetrain": ["AWD"],
  "body_styles": ["4-door electric pickup truck"],
  "hybrid": false,
  "diesel": false,
  "difficulty_modifier": 1.4,
  "notes": "All-electric Hummer EV features Ultium battery platform with up to 246.8 kWh total capacity. High-voltage system (400V/800V switchable) demands EV-certified technicians. CrabWalk four-wheel steering requires specialized diagnostic equipment. Data sourced from Wikipedia GMC Hummer EV article, October 11, 2025 revision."
}
```

## Contribution Rules

### Data Quality Standards

1. **Use Reliable Sources**
   - Default to Wikipedia vehicle generation pages for verification
   - Capture exact article URLs and revision dates
   - Example: "Data sourced from Wikipedia Chevrolet Corvette article, October 11, 2025 revision"

2. **Maintain Valid JSON**
   - Keep field names consistent across all entries
   - Use arrays for multi-valued fields
   - Validate with `jq empty vehicles.json` after every change

3. **Difficulty Modifiers**
   - Every `difficulty_modifier` must be at least `1.00`
   - Increase for complicated service scenarios (brass-era restorations, high-voltage EV work, commercial vehicles)
   - **ALWAYS justify the value in the `notes` field**

4. **North American Configurations Only**
   - Reflect only documented North American configurations
   - Exception: Common import variants that are well-established in the region

5. **Avoid Duplicates**
   - Create a new entry for each distinct generation instead of overwriting historic data
   - Check existing entries with `grep '"model": "Model Name"' vehicles.json` before adding
   - Each generation/platform gets its own JSON object

6. **Document Assumptions**
   - Prefer leaving fields blank over guessing when data cannot be confirmed
   - Create TODO items for ambiguous information
   - If Wikipedia is unclear, do not fabricate data

7. **Keep Tracking Files Synchronized**
   - Update `CHECKLIST.md` as you discover new historical models
   - Update `PROGRESS_TRACKER.md` in real-time as you work
   - Update `CHECKLIST_STATUS.md` only when manufacturer is fully complete
   - Keep `tracking.md` current with generation notes

## Organized Workflow (REQUIRED)

This repository uses a **decade-based isolated workflow** to prevent data corruption and maintain clear progress tracking.

### Why This Workflow Exists

- `vehicles.json` is too large to read repeatedly (>25,000 tokens)
- Research can span 100+ models per manufacturer
- Progress must be trackable without searching massive files
- Validation must occur BEFORE appending to prevent corruption

### The Five-Phase Process

**Phase 1: Gap Analysis & Verification**
- Select manufacturer from `CHECKLIST_STATUS.md`
- Create `wip/[manufacturer]/` directory
- Create `PROGRESS_TRACKER.md` with emoji status indicators
- Verify current coverage using grep/jq (don't read entire file)
- Identify missing models

**Phase 2: Decade-by-Decade Research**
- Create isolated JSON files: `wip/[manufacturer]/[decade].json`
- Research models using Wikipedia as primary source
- Document all Wikipedia URLs with revision dates
- Update `PROGRESS_TRACKER.md` in real-time
- Validate each decade file with `jq empty` before proceeding

**Phase 3: Validation & Quality Checks**
- Verify all required fields present
- Check difficulty modifiers are >= 1.00 with justification
- Ensure no duplicates with existing `vehicles.json`
- Confirm Wikipedia citations in all notes fields
- Mark decade as `⏳ READY` in PROGRESS_TRACKER.md

**Phase 4: Batch Append to vehicles.json**
- **ALWAYS backup first**: `cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)`
- Merge multiple decades at once using `jq -s '.[0] + .[1] + ...'`
- Validate merged file with `jq empty vehicles.json`
- Verify entry count matches expected total
- Archive completed files with `_APPENDED` suffix
- Update PROGRESS_TRACKER.md with `✅ APPENDED` status

**Phase 5: Manufacturer Completion**
- Create completion report (see `GMC_PHASE1_COMPLETION_REPORT.md` example)
- Update `CHECKLIST.md` status note
- Update `CHECKLIST_STATUS.md` (only when fully complete)
- Move to next manufacturer

### Progress Tracking Requirements

Every manufacturer must have a `PROGRESS_TRACKER.md` in their `wip/` directory with:
- Quick status table with emoji indicators (⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | 🔜 LATER)
- Per-decade model lists with checkboxes
- Wikipedia source URLs and revision dates
- Current `vehicles.json` count for manufacturer
- Validation checklist status
- Append status tracking

**Example status table:**
```markdown
| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 8      | ✅ 8/8 | `2020s.json` ✅ | ✅ APPENDED |
| 2010s  | 5      | ✅ 5/5 | `2010s.json` ✅ | ✅ APPENDED |
| 2000s  | 6      | 🔄 3/6 | `2000s.json` ⏳ | ❌ |
| 1990s  | 7      | ⏳ 0/7 | - | ❌ |
```

## Tool Usage Best Practices

### Large File Handling

**`vehicles.json` is too large to read directly.** Use these techniques:

```bash
# Count entries for a manufacturer
grep -c '"make": "GMC"' vehicles.json

# List all models for a manufacturer
grep -A 1 '"make": "GMC"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Search for specific model
grep '"model": "Sierra"' vehicles.json

# Extract specific manufacturer (use cautiously, can be large)
jq '[.[] | select(.make == "GMC")]' vehicles.json > gmc_entries.json
```

### JSON Validation Commands

```bash
# Validate single decade file
jq empty wip/gmc/2020s.json

# Validate production dataset
jq empty vehicles.json

# Validate and pretty-print
jq . wip/gmc/2020s.json

# Count entries in decade file
jq 'length' wip/gmc/2020s.json

# Merge decade files (Phase 4)
jq -s '.[0] + .[1] + .[2]' vehicles.json wip/gmc/1980s.json wip/gmc/1990s.json > vehicles_temp.json
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

## Common Pitfalls to Avoid

### ❌ DON'T
- Read entire `vehicles.json` file (causes token waste)
- Append directly to `vehicles.json` without the `wip/` workflow
- Research without creating `PROGRESS_TRACKER.md` (you will lose track)
- Skip validation before appending (can corrupt production dataset)
- Guess at data when Wikipedia is unclear
- Overwrite historical generations with newer data
- Skip backup before merging
- Mark manufacturer complete if any decades are pending

### ✅ DO
- Use grep/jq for targeted `vehicles.json` queries
- Create isolated decade files in `wip/` directory
- Maintain real-time `PROGRESS_TRACKER.md` updates
- Validate each decade file with `jq empty` before proceeding
- Document Wikipedia sources with revision dates
- Preserve each generation as separate JSON entry
- Backup `vehicles.json` before every merge
- Archive completed decade files with `_APPENDED` suffix
- Create completion reports for reference

## Resuming Work in New Conversation

If you're continuing work in a new conversation:

1. **Read the PROGRESS_TRACKER.md first**
   ```bash
   cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
   ```
   This shows exactly what's complete and what's pending.

2. **Check the "Appended" column**
   - `✅ APPENDED`: Decade is complete and merged
   - `⏳ READY`: Decade is validated and ready to append
   - `🔄 IN PROGRESS`: Decade research is ongoing
   - `❌`: Decade not started

3. **Identify your next action**
   - If decades show `⏳ READY`: Proceed to Phase 4 (Batch Append)
   - If decade shows `🔄 IN PROGRESS`: Continue research
   - If all show `✅ APPENDED`: Create completion report or start next manufacturer

4. **Verify context**
   ```bash
   # Check current count
   grep -c '"make": "[Manufacturer]"' vehicles.json

   # List decade files
   ls -la wip/[manufacturer]/*.json
   ```

5. **Continue with the same standards**
   - Follow the phase indicated in PROGRESS_TRACKER.md
   - Update progress tracker as you work
   - Validate before appending

## Getting Started

### For AI Agents
1. Read `PROMPT.md` for complete instructions
2. Follow the five-phase workflow exactly as documented
3. Create `wip/[manufacturer]/PROGRESS_TRACKER.md` immediately
4. Update progress tracker in real-time
5. Never skip validation or backup steps

### For Human Contributors
1. Review `CHECKLIST_STATUS.md` to find next manufacturer
2. Read `WORKFLOW.md` for step-by-step procedures
3. Check if `wip/[manufacturer]/PROGRESS_TRACKER.md` exists
4. If resuming: Check progress tracker to see what's complete
5. If starting fresh: Create working directory and progress tracker

### For Code Review
- Verify all decade files validated with `jq empty`
- Check PROGRESS_TRACKER.md for completion status
- Confirm Wikipedia citations present in all notes
- Verify difficulty modifiers are justified
- Check backup was created before merge
- Ensure no duplicate generations exist

## Example Reference Files

### Progress Tracking
- `wip/gmc/PROGRESS_TRACKER.md` - Complete example with emoji indicators
- `wip/chevrolet/PROGRESS_TRACKER.md` - Large manufacturer example

### Completion Reports
- `GMC_PHASE1_COMPLETION_REPORT.md` - Phase 1 completion documentation
- `CHEVROLET_COMPLETION_REPORT.md` - Full manufacturer completion

### Gap Analysis
- `CHEVROLET_GAP_ANALYSIS.md` - Example gap analysis workflow

### Decade Files
- `wip/gmc/2020s_APPENDED.json` - Validated and archived decade file
- `wip/gmc/1990s_APPENDED.json` - Performance vehicles example (Syclone/Typhoon)

## Project Goals

The ultimate goal is a comprehensive, validated dataset of all North American vehicles that includes:
- Complete coverage of 37 manufacturers (see `CHECKLIST_STATUS.md`)
- All model generations from 1900s to present
- Accurate powertrain specifications
- Service complexity indicators (difficulty modifiers)
- Mobile mechanic-relevant maintenance notes
- Verified Wikipedia citations for all data

This dataset powers a mobile mechanic pricing system, so **accuracy and completeness are critical**.

## Questions or Issues?

- Review `PROMPT.md` for comprehensive instructions
- Check `WORKFLOW.md` for step-by-step procedures
- Examine `wip/gmc/PROGRESS_TRACKER.md` for organization examples
- Refer to `GMC_PHASE1_COMPLETION_REPORT.md` for completion standards
- Consult `AGENTS.md` for agent-specific rules

**When in doubt, follow the workflow. Don't skip steps. Always validate.**
