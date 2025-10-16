# Vehicle Dataset Agent Rules

## Critical Workflow Requirements

**BEFORE doing any research or appending data, you MUST:**
1. Read `PROMPT.md` for complete workflow instructions
2. Create or update `wip/[manufacturer]/PROGRESS_TRACKER.md`
3. Use the decade-based isolated workflow (NEVER append directly to vehicles.json)
4. Validate with `jq empty` before every merge

## Core Principles

### Organization is Mandatory
- `vehicles.json` is too large to read directly (>25,000 tokens)
- All research must happen in `wip/[manufacturer]/[decade].json` files
- Progress must be tracked in `PROGRESS_TRACKER.md` with emoji indicators
- Validation must occur BEFORE appending to production dataset

### Quality AND Efficiency
- Use **only factual data verified against Wikipedia** (primary source)
- If information is ambiguous or missing, **leave it out** rather than guessing
- Every `difficulty_modifier` must have justification in notes
- Each generation gets its own JSON object (do not overwrite historical data)
- **Speed matters**: Batch WebFetch calls, streamline notes, validate in parallel
- **Concise ≠ incomplete**: Short technical notes are preferred over verbose explanations

## Data Collection Rules

### Primary Source Requirements
- Always source vehicle information from Wikipedia vehicle generation pages
- Cite the exact article URL in notes field
- Include revision date in citation (e.g., "October 11, 2025 revision")
- Example: "Data sourced from Wikipedia GMC Hummer EV article, October 11, 2025 revision."

### Required Fields for Every Entry
Capture ALL of the following for each North American generation:

1. **years**: Array of integers
   - Example: `[2020, 2021, 2022, 2023, 2024]`
   - Include ONLY North American model years

2. **make**: Manufacturer name
   - Example: `"GMC"`, `"Chevrolet"`, `"Ford"`

3. **model**: Model name with generation/platform code when relevant
   - Example: `"Sierra (GMT400)"`, `"Corvette (C8)"`, `"F-150 (14th generation)"`
   - Include generation identifier for clarity

4. **engines**: Array of engine descriptions
   - Include displacement, code (if available), and notable output differences
   - Example: `["5.7L V8 (350 hp)", "6.2L V8 (460 hp)", "3.0L Turbo Diesel I6 (277 hp)"]`
   - For EVs: `["EV3X: 3 electric motors (1,000 hp)"]`

5. **transmissions**: Array of transmission options
   - Include gear counts and codes where available
   - Example: `["6-speed manual", "8-speed automatic", "10-speed automatic"]`
   - For EVs: `["Single-speed electric drive"]`

6. **region**: Region classification
   - Options: `"American"`, `"Canadian"`, `"Mexican"`, `"Japanese import"`, `"European import"`

7. **drivetrain**: Array of drivetrain layouts
   - Options: `["FWD"]`, `["RWD"]`, `["AWD"]`, `["4WD"]`, `["2WD", "4WD"]`
   - Use array format even for single option

8. **body_styles**: Array of body styles sold in North America
   - Example: `["2-door coupe", "2-door convertible"]`
   - Example: `["Regular Cab", "Extended Cab", "Crew Cab"]`

9. **hybrid**: Boolean flag
   - `true` if hybrid option available, otherwise `false`

10. **diesel**: Boolean flag
    - `true` if diesel option available, otherwise `false`

11. **difficulty_modifier**: Numeric (must be >= 1.00)
    - See difficulty modifier guidelines below
    - **MUST be justified in notes field**

12. **notes**: Service insights and Wikipedia citation
    - Service-critical details (timing chain/belt, HV battery, specialty tools, air brakes)
    - Platform sharing documentation (GMT400, Lambda, etc.)
    - Wikipedia citation with revision date (REQUIRED)

### Difficulty Modifier Guidelines

**Scale the modifier based on service complexity, ALWAYS document rationale:**

- **1.0**: Standard modern vehicle
  - Conventional engines, standard transmissions
  - Readily available parts and tools
  - Example: 2020 Chevrolet Malibu, 2020 Hyundai Sonata

- **1.1**: Moderate complexity
  - Complex service access
  - Diesel engines (moderate complexity)
  - Basic hybrid systems (non-PHEV)
  - Example: GMC Sierra HD with Duramax diesel, Hyundai Elantra Hybrid

- **1.2**: Elevated complexity
  - Brass-era vehicles (1910s-1920s) with fragile construction
  - Turbocharged performance vehicles requiring specialized knowledge
  - Medium-duty commercial trucks with air brakes
  - Vintage vehicles (1940s-1960s) with 6-volt electrical, points ignition
  - Example: GMC Syclone, Jeep CJ-5 (1950s)

- **1.3**: High complexity
  - Heavy-duty commercial trucks
  - Air brake systems requiring commercial certification
  - Complex vintage vehicles with obsolete tooling
  - **Plug-in hybrids (PHEVs)** with high-voltage charging systems
  - **Battery EVs with standard voltage (up to 400V)**
  - Example: GMC Brigadier, Hyundai Tucson PHEV, Hyundai Kona Electric

- **1.4+**: Very high complexity
  - **High-voltage EV systems (800V)**
  - Switchable voltage platforms (400V/800V)
  - Advanced driver assistance requiring specialized calibration
  - WWII-era military vehicles with historical preservation requirements
  - Example: GMC Hummer EV (1.4), Hyundai Ioniq 5 (1.4), Jeep Willys MB (1.4)

**CRITICAL**: Every difficulty_modifier >= 1.1 MUST have justification in notes explaining why standard complexity (1.0) is insufficient.

**Streamlined justification examples**:
- **1.1**: "Basic hybrid system with lithium-ion battery."
- **1.3**: "PHEV with 13.8 kWh high-voltage battery requires PHEV-certified technicians."
- **1.4**: "800V architecture with 233 kW DC fast charging requires EV-certified technicians for high-voltage system."

## Organized Workflow (MANDATORY)

### Phase 1: Setup & Verification
1. **Create Working Directory**
   ```bash
   mkdir -p wip/[manufacturer]
   ```

2. **Create PROGRESS_TRACKER.md** (REQUIRED)
   - Use emoji status indicators: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | 🔜 LATER
   - Include status table showing decade completion
   - Track Wikipedia sources with URLs and revision dates
   - Document current vehicles.json count
   - See `wip/gmc/PROGRESS_TRACKER.md` for reference

3. **Verify Current Coverage** (use grep, NOT Read tool)
   ```bash
   # Count existing entries
   grep -c '"make": "[Manufacturer]"' vehicles.json

   # List existing models
   grep -A 1 '"make": "[Manufacturer]"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq
   ```

### Phase 2: Decade-by-Decade Research
1. **Create Decade File**
   ```bash
   touch wip/[manufacturer]/[decade].json
   ```
   - Format: JSON array of objects
   - Example: `wip/gmc/2020s.json`

2. **Research Models for the Decade**
   - Find Wikipedia generation-specific pages
   - Record exact URLs and revision dates in PROGRESS_TRACKER.md
   - Capture all required fields (see above)
   - Update PROGRESS_TRACKER.md in real-time as models complete

3. **Validate Decade File** (REQUIRED before proceeding)
   ```bash
   jq empty wip/[manufacturer]/[decade].json
   ```
   - Must pass with no errors
   - Fix syntax issues immediately

4. **Update Progress Tracker**
   - Mark models `[x]` as researched
   - Update decade status (⏳ → 🔄 → ✅)
   - Mark decade as `⏳ READY` when all models complete

### Phase 3: Validation Checklist
Before marking any decade as READY, verify:
- [ ] All models researched with Wikipedia citations
- [ ] JSON validates with `jq empty wip/[manufacturer]/[decade].json`
- [ ] All difficulty_modifier >= 1.00 with justification in notes
- [ ] All required fields present (years, engines, transmissions, etc.)
- [ ] No duplicate entries within decade file
- [ ] Hybrid/diesel flags match captured powertrains
- [ ] Body styles reflect North American market only
- [ ] Notes include Wikipedia citation with revision date
- [ ] Platform sharing documented where relevant (GMT400, Lambda, etc.)

### Phase 4: Batch Append to vehicles.json
**CRITICAL**: Only append after ALL target decades are validated

1. **Pre-Append Verification**
   - All decade files show ✅ COMPLETE in PROGRESS_TRACKER.md
   - All decade files validate individually
   - PROGRESS_TRACKER.md shows accurate counts

2. **Backup Production Dataset** (NEVER SKIP)
   ```bash
   cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)
   ```

3. **Merge Decades**
   ```bash
   # Merge all validated decades at once
   jq -s '.[0] + .[1] + .[2] + .[3] + .[4]' \
     vehicles.json \
     wip/[manufacturer]/1980s.json \
     wip/[manufacturer]/1990s.json \
     wip/[manufacturer]/2000s.json \
     wip/[manufacturer]/2010s.json \
     wip/[manufacturer]/2020s.json \
     > vehicles_temp.json

   mv vehicles_temp.json vehicles.json
   ```

4. **Validate Merged File** (CRITICAL)
   ```bash
   jq empty vehicles.json
   # If this fails, restore from backup IMMEDIATELY
   ```

5. **Verify Entry Count**
   ```bash
   grep -c '"make": "[Manufacturer]"' vehicles.json
   # Compare against expected count in PROGRESS_TRACKER.md
   ```

6. **Archive Completed Decade Files**
   ```bash
   cd wip/[manufacturer]
   for decade in 1980s 1990s 2000s 2010s 2020s; do
     mv ${decade}.json ${decade}_APPENDED.json
   done
   ```

7. **Update PROGRESS_TRACKER.md**
   - Change `⏳ READY` to `✅ APPENDED`
   - Update "Current vehicles.json count"
   - Add append date/timestamp

### Phase 5: Completion Documentation
1. **Create Completion Report** (recommended)
   - Document coverage by decade
   - List difficulty modifiers applied
   - Note platform sharing
   - Track Wikipedia sources
   - Example: `GMC_PHASE1_COMPLETION_REPORT.md`

2. **Update Tracking Files**
   - Update `CHECKLIST.md` status note
   - Update `CHECKLIST_STATUS.md` (ONLY when fully complete)

## Tool Usage Best Practices

### Large File Handling
**NEVER use Read tool on vehicles.json.** Use these techniques instead:

```bash
# Count entries for a manufacturer
grep -c '"make": "GMC"' vehicles.json

# List all models for a manufacturer
grep -A 1 '"make": "GMC"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Search for specific model
grep '"model": "Sierra"' vehicles.json

# Extract manufacturer's entries (use cautiously, can be large)
jq '[.[] | select(.make == "GMC")]' vehicles.json > gmc_entries.json
```

### JSON Validation
```bash
# Validate decade file
jq empty wip/gmc/2020s.json

# Count entries in decade file
jq 'length' wip/gmc/2020s.json

# Pretty-print for review
jq . wip/gmc/2020s.json

# Validate production dataset
jq empty vehicles.json
```

### Progress Tracking
**Maintain PROGRESS_TRACKER.md with:**
- Status table with emoji indicators
- Per-decade model lists with checkboxes
- Wikipedia URLs and revision dates
- Current vehicles.json count
- Validation status
- Append status

Example table:
```markdown
| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 8      | ✅ 8/8 | `2020s.json` ✅ | ✅ APPENDED |
| 2010s  | 5      | ✅ 5/5 | `2010s.json` ✅ | ⏳ READY |
| 2000s  | 6      | 🔄 3/6 | `2000s.json` ⏳ | ❌ |
```

## Data Quality Standards

### Factual Accuracy
- Use **ONLY Wikipedia** as primary source for this workflow
- If information cannot be confirmed, create TODO note instead of guessing
- Cross-reference platform-shared models for consistency (GMT400, Lambda, T1XX, etc.)
- Record exact URLs with revision dates

### JSON Integrity
- Preserve vehicles.json insertion order (change history clarity)
- Ensure hybrid/diesel flags align with powertrain lists
- Use arrays for ALL multi-valued fields
- Each generation gets separate JSON object (never overwrite)

### Documentation Standards
- All difficulty_modifier values must have justification
- All entries must cite Wikipedia with revision date
- Platform sharing must be documented
- Service-critical details required: timing chain/belt, HV battery, specialty tools, air brakes

### Validation Requirements
- After each decade file: `jq empty wip/[manufacturer]/[decade].json`
- After merging: `jq empty vehicles.json`
- If validation fails, restore from backup immediately
- Verify entry counts match expected totals

## Common Pitfalls (AVOID THESE)

### ❌ NEVER
- Read entire vehicles.json with Read tool (token waste)
- Append directly to vehicles.json without wip/ workflow
- Research without creating PROGRESS_TRACKER.md (you will lose track)
- Skip validation before appending (can corrupt dataset)
- Guess at data when Wikipedia is unclear
- Overwrite historical generations with newer data
- Skip backup before merging to vehicles.json
- Mark manufacturer complete in CHECKLIST_STATUS.md if any decades pending

### ✅ ALWAYS
- Use grep/jq for targeted vehicles.json queries
- Create isolated decade files in wip/ directory
- Maintain real-time PROGRESS_TRACKER.md updates
- Validate each decade file before proceeding
- Document Wikipedia sources with revision dates
- Preserve each generation as separate JSON entry
- Backup vehicles.json before every merge
- Archive completed decade files with `_APPENDED` suffix

## Platform Sharing Documentation

Many vehicles share platforms. Document this in notes field:

**GM Truck Platforms (Chevrolet/GMC):**
- GMT400 (1988-1998): Sierra/Silverado, full-size pickups
- GMT800 (1999-2006): Sierra/Silverado, Yukon/Tahoe
- GMT900 (2007-2013): Sierra/Silverado light-duty
- K2XX (2014-2020): Sierra/Silverado, Yukon/Tahoe
- T1XX (2019-present): Current Sierra/Silverado, Yukon/Tahoe
- GMT355 (2004-2012): Canyon/Colorado midsize
- GMT360 (2002-2009): Envoy/TrailBlazer SUV
- Lambda (2007-2016): Acadia/Traverse/Enclave crossovers
- Theta (2010-2017): Terrain/Equinox compact crossovers

**Cross-reference these platforms for engine/transmission consistency.**

## Resuming Work in New Conversation

If you're starting a new conversation and continuing work:

1. **Read PROGRESS_TRACKER.md FIRST**
   ```bash
   cat wip/[manufacturer]/PROGRESS_TRACKER.md
   ```
   This shows exactly what's complete and what's pending.

2. **Check Append Status**
   - `✅ APPENDED`: Decade merged to vehicles.json
   - `⏳ READY`: Validated and ready to append
   - `🔄 IN PROGRESS`: Research ongoing
   - `❌`: Not started

3. **Identify Next Action**
   - If `⏳ READY`: Proceed to Phase 4 (Batch Append)
   - If `🔄 IN PROGRESS`: Continue research for that decade
   - If `✅ APPENDED`: Create completion report or start next manufacturer

4. **Verify Context**
   ```bash
   grep -c '"make": "[Manufacturer]"' vehicles.json
   ls -la wip/[manufacturer]/*.json
   ```

5. **Continue with Same Standards**
   - Follow phase indicated in PROGRESS_TRACKER.md
   - Update progress tracker as you work
   - Validate before appending

## Special Vehicle Categories

### Brass-Era Vehicles (1910s-1920s)
- Use concise, era-appropriate field values
- Difficulty modifier typically 1.2-1.3 due to fragile construction and obsolete tooling
- Document restoration complexity in notes

### Electric Vehicles (EVs)
- Difficulty modifier 1.4+ for high-voltage systems (400V+)
- Document battery platform (Ultium, MEB, etc.)
- Note voltage specifications in notes
- Specify EV-certified technician requirements

### Commercial Trucks
- Medium-duty (C-Series, TopKick): difficulty 1.2
- Heavy-duty (Brigadier, General): difficulty 1.3
- Document air brake systems and commercial requirements
- Note weight ratings and chassis configurations

### Performance Vehicles
- Turbocharged/supercharged: difficulty 1.1-1.2
- Document specialty tuning requirements
- Note performance-oriented service knowledge needs
- Example: GMC Syclone/Typhoon (1.1)

## Update Synchronization Requirements

As you progress, keep these files synchronized:

1. **PROGRESS_TRACKER.md** - Real-time updates as you work
2. **CHECKLIST.md** - Add newly discovered models immediately
3. **vehicles.json** - Only via Phase 4 batch append workflow
4. **CHECKLIST_STATUS.md** - Only when manufacturer fully complete
5. **tracking.md** - Update with generation notes when relevant

## Final Checklist Before Marking Complete

Before marking any manufacturer complete in CHECKLIST_STATUS.md:

- [ ] All decades researched (1910s-2020s or documented phases)
- [ ] All decade files validated and appended
- [ ] PROGRESS_TRACKER.md shows all ✅ APPENDED
- [ ] vehicles.json validates successfully
- [ ] Entry count matches expected total
- [ ] Completion report created
- [ ] CHECKLIST.md status updated
- [ ] All Wikipedia sources documented

**If ANY decade is pending, leave CHECKLIST_STATUS.md unchecked and document what remains.**

## Remember

- **Organization prevents chaos** - Use the wip/ directory workflow
- **Tracking prevents loss** - Update PROGRESS_TRACKER.md constantly
- **Validation prevents corruption** - Check with jq before every merge
- **Backup prevents disasters** - Always backup before appending
- **Documentation prevents confusion** - Cite Wikipedia with revision dates

**When in doubt, follow PROMPT.md. Don't skip steps. Always validate.**
