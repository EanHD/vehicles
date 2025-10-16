# Vehicle Dataset Research Workflow

**Last Updated**: October 11, 2025

## Purpose
This workflow ensures systematic, organized completion of the North American vehicle dataset with minimal token waste, clear progress tracking, and no gaps in coverage.

## Directory Structure

```
vehicles/
├── vehicles.json                 # Main production dataset
├── CHECKLIST.md                  # Decade-organized model roster per manufacturer
├── CHECKLIST_STATUS.md          # High-level manufacturer completion tracker
├── tracking.md                   # Generation notes and research priorities
├── CHEVROLET_GAP_ANALYSIS.md   # Example gap analysis file
├── wip/                          # Work-in-progress JSON files by manufacturer
│   ├── chevrolet/
│   │   ├── 1910s.json
│   │   ├── 1920s.json
│   │   ├── 1930s.json
│   │   └── ...
│   ├── gmc/
│   ├── buick/
│   └── ...
└── README.md                     # Schema and contribution rules
```

## Step-by-Step Workflow

### Phase 1: Gap Analysis
**Goal**: Identify exactly which models are missing from vehicles.json

1. **Select Target Manufacturer**
   - Review `CHECKLIST_STATUS.md` to find the current manufacturer
   - If marked complete but unverified, start with gap analysis
   - If incomplete, proceed with gap analysis

2. **Create Gap Analysis File**
   ```bash
   touch [MANUFACTURER]_GAP_ANALYSIS.md
   ```
   - List all models from CHECKLIST.md organized by decade
   - Use checkboxes [ ] for tracking
   - Cross-reference with vehicles.json to mark present models [x]

3. **Automated Gap Check** (recommended)
   ```bash
   # Extract all models for a manufacturer from vehicles.json
   grep -A 1 '"make": "Chevrolet"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq > chevrolet_in_json.txt

   # Compare against CHECKLIST.md manually or with scripts
   ```

4. **Identify Missing Models**
   - Create a prioritized list of models to research
   - Group by decade for organized research

### Phase 2: Decade-by-Decade Research

**Goal**: Research and document missing models in isolated JSON files

1. **Create Decade File**
   ```bash
   touch wip/[manufacturer]/[decade].json
   ```
   - Example: `wip/chevrolet/1950s.json`

2. **Research Requirements**
   - **Primary Source**: Wikipedia vehicle generation pages
   - **Capture**: Exact article URL and revision date
   - **Required Fields**: years, make, model, engines, transmissions, region, drivetrain, body_styles, hybrid, diesel, difficulty_modifier, notes

3. **JSON Format** (array of objects)
   ```json
   [
     {
       "years": [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962],
       "make": "Chevrolet",
       "model": "Corvette (C1)",
       "engines": ["235 cu in I6 (150 hp)", "265 cu in V8 (195 hp)", "283 cu in V8 (230-290 hp)"],
       "transmissions": ["2-speed Powerglide automatic", "3-speed manual", "4-speed manual"],
       "region": "American",
       "drivetrain": ["RWD"],
       "body_styles": ["2-door convertible", "2-door coupe (1963)"],
       "hybrid": false,
       "diesel": false,
       "difficulty_modifier": 1.2,
       "notes": "C1 Corvettes featured hand-laid fiberglass bodies, solid rear axles, and were initially powered by inline-six engines before switching to V8s in 1955. Data sourced from Wikipedia Chevrolet Corvette article, October 10, 2025 revision."
     }
   ]
   ```

4. **Difficulty Modifier Guidelines**
   - `1.0`: Standard modern vehicle
   - `1.1-1.3`: Brass-era vehicles (1910s-1920s), complex service access
   - `1.2-1.5`: High-voltage EV systems, complex hybrid systems
   - `1.1-1.2`: Specialty tools required, unusual configurations
   - **Always document rationale in notes field**

5. **Mark Progress**
   - Update `[MANUFACTURER]_GAP_ANALYSIS.md` as you complete models
   - Use `[x]` to mark researched models
   - Add `[WIP-1950s]` tag to indicate which decade file contains the entry

### Phase 3: Validation

**Goal**: Ensure accuracy and JSON validity before appending

1. **Validate Decade JSON**
   ```bash
   jq empty wip/chevrolet/1950s.json
   ```
   - Must pass without errors

2. **Peer Review Checklist**
   - [ ] All required fields present
   - [ ] Years array is complete and accurate
   - [ ] Engines include displacement and notable HP differences
   - [ ] Transmissions include gear counts
   - [ ] difficulty_modifier >= 1.00
   - [ ] Notes include Wikipedia citation with revision date
   - [ ] Body styles reflect North American market only
   - [ ] No duplicate entries with existing vehicles.json

3. **Mark Decade Complete**
   - Update gap analysis: `[COMPLETE-1950s]`
   - Update tracking.md if needed

### Phase 4: Append to vehicles.json

**Goal**: Integrate validated decade data into production dataset

1. **Backup Current vehicles.json**
   ```bash
   cp vehicles.json vehicles.json.backup
   ```

2. **Append Decade Data**
   ```bash
   # Remove closing bracket from vehicles.json
   # Append comma and decade JSON content
   # Add closing bracket back
   # OR use jq to merge arrays:
   jq -s '.[0] + .[1]' vehicles.json wip/chevrolet/1950s.json > vehicles_merged.json
   mv vehicles_merged.json vehicles.json
   ```

3. **Validate Merged File**
   ```bash
   jq empty vehicles.json
   ```

4. **Archive Completed Decade File**
   ```bash
   mv wip/chevrolet/1950s.json wip/chevrolet/1950s_APPENDED.json
   ```

### Phase 5: Manufacturer Completion

**Goal**: Finalize manufacturer and move to next

1. **Final Verification**
   - Confirm all decades have been researched and appended
   - Update `[MANUFACTURER]_GAP_ANALYSIS.md` with completion status
   - Ensure CHECKLIST.md status note is current

2. **Mark Complete in CHECKLIST_STATUS.md**
   ```markdown
   - [x] Chevrolet — historical model roster audited and `CHECKLIST.md` updated
   ```

3. **Archive Gap Analysis**
   ```bash
   mv CHEVROLET_GAP_ANALYSIS.md wip/chevrolet/GAP_ANALYSIS_COMPLETE.md
   ```

4. **Commit Progress**
   - Git commit with clear message indicating completion
   - Example: "Complete Chevrolet historical dataset - 171 models verified"

5. **Move to Next Manufacturer**
   - Update CHECKLIST_STATUS.md with next target
   - Create gap analysis for next manufacturer
   - Repeat workflow

## Best Practices

### Token Efficiency
- **Don't** read entire vehicles.json repeatedly
- **Do** use grep/jq for targeted searches
- **Don't** lose track of progress
- **Do** update gap analysis files frequently
- **Don't** research the same model twice
- **Do** mark WIP status clearly

### Quality Standards
- Verify data against Wikipedia primary source
- Document any ambiguities in notes
- Prefer leaving fields blank over guessing
- Use consistent naming conventions for generations
- Scale difficulty_modifier with clear justification

### Organization
- One manufacturer at a time
- One decade at a time within manufacturer
- Clear file naming: `wip/[manufacturer]/[decade].json`
- Archive completed files with `_APPENDED` suffix
- Keep gap analysis updated in real-time

## Quick Reference Commands

```bash
# Validate JSON
jq empty [file].json

# Count entries for manufacturer
grep -c '"make": "Chevrolet"' vehicles.json

# List all models for manufacturer
grep -A 1 '"make": "Chevrolet"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Merge JSON arrays
jq -s '.[0] + .[1]' vehicles.json wip/chevrolet/1950s.json > vehicles_merged.json

# Check for duplicates
jq '[.[] | {make, model, years}] | group_by(.make + .model) | map(select(length > 1))' vehicles.json
```

## Progress Tracking Files

- **CHECKLIST.md**: Decade lists of all models per manufacturer
- **CHECKLIST_STATUS.md**: High-level manufacturer completion checkboxes
- **[MANUFACTURER]_GAP_ANALYSIS.md**: Detailed gap analysis per manufacturer
- **tracking.md**: Generation notes, hybrid/diesel matrix, priorities
- **wip/[manufacturer]/**: Decade JSON files for work in progress

## Collaboration Notes

When multiple people are working:
1. Check gap analysis files for WIP tags before starting research
2. Mark your assigned decade immediately: `[WIP-1960s - @username]`
3. Commit decade files frequently to avoid conflicts
4. Don't append to vehicles.json until decade is peer-reviewed
5. Communicate in gap analysis file using markdown comments
