# Vehicles Dataset - QWEN Agent Instructions

## 🎯 QUICK START: What To Do When You Start

**If you're resuming work or starting a new task:**

1. **Read PROGRESS_TRACKER.md FIRST**
   ```bash
   cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
   ```
   This tells you EXACTLY where we left off and what to do next.

2. **Check the status table** - Look for emoji indicators:
   - ✅ APPENDED = Done, move on
   - ⏳ READY = Validated, needs to be appended to vehicles.json
   - 🔄 IN PROGRESS = Continue research
   - ❌ = Not started yet

3. **Follow the phase** indicated in the tracker
4. **Update the tracker** as you work (real-time updates!)

## 🚨 CRITICAL RULES (Read This First!)

### NEVER Do These Things:
❌ **DO NOT** read `vehicles.json` with the Read tool (it's too large - wastes tokens)
❌ **DO NOT** append directly to `vehicles.json` without using the wip/ workflow
❌ **DO NOT** skip creating `PROGRESS_TRACKER.md` (you WILL lose track)
❌ **DO NOT** skip validation with `jq empty` before merging
❌ **DO NOT** skip backup before appending to `vehicles.json`
❌ **DO NOT** guess at data - if Wikipedia is unclear, leave it out

### ALWAYS Do These Things:
✅ **DO** use grep/jq for vehicles.json queries (not Read tool)
✅ **DO** create isolated decade files in `wip/[manufacturer]/[decade].json`
✅ **DO** maintain `PROGRESS_TRACKER.md` with real-time updates
✅ **DO** validate each decade file before proceeding
✅ **DO** backup `vehicles.json` before every merge
✅ **DO** cite Wikipedia with revision dates in notes

## 📋 The 5-Phase Workflow (Follow This Exactly)

### Phase 1: Setup & Gap Analysis
**Goal**: Figure out what needs to be researched

```bash
# Create working directory
mkdir -p wip/[manufacturer]

# Create progress tracker (REQUIRED!)
touch wip/[manufacturer]/PROGRESS_TRACKER.md
```

**Progress Tracker Must Include:**
- Status table with emojis (⏳ TODO | 🔄 IN PROGRESS | ✅ DONE)
- Per-decade model lists with checkboxes
- Wikipedia URLs with revision dates
- Current vehicles.json count for manufacturer

**Example Status Table:**
```markdown
| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 8      | ✅ 8/8 | `2020s.json` ✅ | ✅ APPENDED |
| 2010s  | 5      | 🔄 3/5 | `2010s.json` ⏳ | ❌ |
```

**Check Current Coverage** (use grep, NOT Read):
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

**STEP-BY-STEP Research Process (Do This For Each Model):**

1. **Find Wikipedia Page**
   ```bash
   # Check if model has generation-specific page
   curl -s "https://en.wikipedia.org/wiki/Ford_F-150_(fourteenth_generation)" | head -100
   ```

2. **Extract Key Info** - Look for these sections on Wikipedia:
   - **Years**: Production years for this generation
   - **Engines**: All engine options (displacement, HP, special variants)
   - **Transmissions**: All transmission options with gear counts
   - **Drivetrain**: FWD/RWD/AWD/4WD options
   - **Body styles**: All body configurations (crew cab, regular cab, etc.)
   - **Hybrid/Diesel**: Check powertrain section
   - **Platform code**: (GMT400, T1XX, etc.) - important for notes!

3. **Write JSON Entry** - Use this exact template:
   ```json
   {
     "years": [2021, 2022, 2023, 2024, 2025],
     "make": "Ford",
     "model": "F-150 (Fourteenth generation)",
     "engines": [
       "3.3L V6 (290 hp)",
       "2.7L EcoBoost V6 (325 hp)",
       "5.0L V8 (400 hp)"
     ],
     "transmissions": ["10-speed automatic"],
     "region": "American",
     "drivetrain": ["RWD", "4WD"],
     "body_styles": ["Regular Cab", "SuperCab", "SuperCrew"],
     "hybrid": false,
     "diesel": false,
     "difficulty_modifier": 1.0,
     "notes": "Fourteenth generation on T1 platform. Data sourced from Wikipedia Ford F-150 (fourteenth generation) article, December 19, 2024 revision."
   }
   ```

4. **Update PROGRESS_TRACKER.md** immediately:
   - Change `[ ]` to `[x]` for completed model
   - Add Wikipedia URL to sources section
   - Update status if needed

5. **Validate After Each Model**:
   ```bash
   jq empty wip/[manufacturer]/2020s.json
   ```
   If this shows an error, fix it BEFORE continuing!

**Common Mistakes to Avoid:**
- ❌ Forgetting commas between JSON entries
- ❌ Missing closing brackets `]` or braces `}`
- ❌ Not including all engine options
- ❌ Forgetting to cite Wikipedia in notes
- ❌ Using difficulty_modifier > 1.0 without justification

**Required Fields for EVERY Entry:**
```json
{
  "years": [2020, 2021, 2022, 2023, 2024],
  "make": "GMC",
  "model": "Sierra (T1XX)",
  "engines": ["5.3L V8 (355 hp)", "6.2L V8 (420 hp)"],
  "transmissions": ["10-speed automatic"],
  "region": "American",
  "drivetrain": ["2WD", "4WD"],
  "body_styles": ["Regular Cab", "Crew Cab"],
  "hybrid": false,
  "diesel": false,
  "difficulty_modifier": 1.0,
  "notes": "GMT T1XX platform. Data sourced from Wikipedia GMC Sierra article, December 19, 2024 revision."
}
```

**Difficulty Modifier Scale:**
- 1.0 = Standard modern vehicle
- 1.1 = Diesel, basic hybrid, complex access
- 1.2 = Brass-era (1910s-1920s), turbo performance, medium-duty commercial
- 1.3 = Heavy-duty commercial, air brakes, complex vintage
- 1.4+ = High-voltage EVs (400V+), switchable voltage platforms

**MUST justify all modifiers >= 1.1 in notes!**

### Phase 3: Validation
**Goal**: Ensure accuracy before appending

**Validation Checklist:**
- [ ] All models researched with Wikipedia citations
- [ ] JSON validates: `jq empty wip/[manufacturer]/[decade].json`
- [ ] All difficulty_modifier >= 1.00 with justification
- [ ] All required fields present
- [ ] No duplicate entries
- [ ] Hybrid/diesel flags match powertrains
- [ ] Notes include Wikipedia citation with revision date

**Mark Decade Complete:**
Update PROGRESS_TRACKER.md status to `⏳ READY`

### Phase 4: Batch Append to vehicles.json
**Goal**: Safely merge validated data

**CRITICAL: Only append after ALL target decades validated!**

```bash
# 1. BACKUP (NEVER SKIP!)
cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)

# 2. MERGE multiple decades at once
jq -s '.[0] + .[1] + .[2] + .[3] + .[4]' \
  vehicles.json \
  wip/gmc/1980s.json \
  wip/gmc/1990s.json \
  wip/gmc/2000s.json \
  wip/gmc/2010s.json \
  wip/gmc/2020s.json \
  > vehicles_temp.json

mv vehicles_temp.json vehicles.json

# 3. VALIDATE merged file
jq empty vehicles.json
# If this fails, RESTORE FROM BACKUP IMMEDIATELY!

# 4. VERIFY entry count
grep -c '"make": "GMC"' vehicles.json

# 5. ARCHIVE completed files
cd wip/gmc
for decade in 1980s 1990s 2000s 2010s 2020s; do
  mv ${decade}.json ${decade}_APPENDED.json
done

# 6. UPDATE PROGRESS_TRACKER.md
# Change ⏳ READY to ✅ APPENDED
# Update current vehicles.json count
```

### Phase 5: Manufacturer Completion
**Goal**: Finalize and document

1. Create completion report (see `GMC_PHASE1_COMPLETION_REPORT.md` example)
2. Update `CHECKLIST.md` status note
3. Update `CHECKLIST_STATUS.md` (ONLY when fully complete)
4. Move to next manufacturer

## 🔧 Essential Tool Commands

### Large File Queries (Use These, Not Read!)
```bash
# Count entries for manufacturer
grep -c '"make": "GMC"' vehicles.json

# List all models
grep -A 1 '"make": "GMC"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Search specific model
grep '"model": "Sierra"' vehicles.json

# Get year range for a model
grep -A 1 '"model": "Sierra"' vehicles.json | grep '"years":'
```

### JSON Validation
```bash
# Validate decade file
jq empty wip/gmc/2020s.json

# Count entries in decade file
jq 'length' wip/gmc/2020s.json

# Pretty-print to check formatting
jq . wip/gmc/2020s.json | head -50

# Validate production dataset
jq empty vehicles.json
```

### 🌐 Wikipedia Research with curl

**Quick Wikipedia searches without leaving terminal:**

```bash
# Search Wikipedia for a model page
curl -s "https://en.wikipedia.org/w/api.php?action=opensearch&search=Ford+F-150&limit=5&format=json" | jq

# Get Wikipedia page content (useful for checking if page exists)
curl -s "https://en.wikipedia.org/wiki/Ford_F-150" | grep -i "engine\|transmission\|drivetrain" | head -20

# Search for specific generation
curl -s "https://en.wikipedia.org/wiki/Ford_F-150" | grep -i "thirteenth generation\|fourteenth generation"

# List of vehicles by manufacturer
curl -s "https://en.wikipedia.org/wiki/List_of_Ford_vehicles" | grep -i "f-150\|ranger\|bronco" | head -30
```

**Pro Tip for Research:**
1. Use `curl` to check if Wikipedia page exists
2. Look for generation-specific pages (e.g., "Ford F-150 (thirteenth generation)")
3. Check "List of [Manufacturer] vehicles" pages first
4. Note the revision date for citation (check page footer or history)

**Example Research Workflow:**
```bash
# 1. Find the main article
curl -s "https://en.wikipedia.org/wiki/List_of_Ford_vehicles" | grep -i "f-150"

# 2. Check for generation pages
curl -s "https://en.wikipedia.org/wiki/Ford_F-150" | grep -i "generation"

# 3. Extract engine/transmission info
curl -s "https://en.wikipedia.org/wiki/Ford_F-150_(fourteenth_generation)" | grep -i "engine\|powertrain"

# 4. Document in notes with revision date
# "Data sourced from Wikipedia Ford F-150 (fourteenth generation) article, December 19, 2024 revision."
```

## 📚 Project Overview

This repository maintains a structured JSON dataset of North American vehicle makes, models, and specifications for mobile mechanic pricing. Coverage spans from brass-era vehicles (1910s) through current EVs.

### Key Files Structure
```
vehicles/
├── vehicles.json              # Production dataset (use grep/jq ONLY)
├── PROMPT.md                  # Complete workflow instructions
├── WORKFLOW.md                # Step-by-step procedures
├── AGENTS.md                  # Agent-specific rules
├── CHECKLIST.md               # Model roster per manufacturer
├── CHECKLIST_STATUS.md        # Manufacturer completion tracker
├── wip/                       # Work-in-progress by manufacturer
│   ├── gmc/
│   │   ├── PROGRESS_TRACKER.md  # Real-time progress
│   │   ├── 2020s_APPENDED.json  # Archived files
│   │   └── ...
│   └── [other manufacturers]/
└── README.md                  # Schema and contribution rules
```

### Data Schema (All Required)

- **years**: Array of integers (North American model years)
- **make**: Manufacturer name (e.g., "GMC", "Chevrolet")
- **model**: Model name with generation code (e.g., "Sierra (GMT400)")
- **engines**: Array with displacement, HP (e.g., "5.7L V8 (350 hp)")
- **transmissions**: Array with gear counts (e.g., "6-speed manual")
- **region**: "American", "Canadian", "Japanese import", etc.
- **drivetrain**: Array (["FWD"], ["RWD", "AWD"], etc.)
- **body_styles**: Array (["2-door coupe"], ["Regular Cab", "Crew Cab"])
- **hybrid**: Boolean (true/false)
- **diesel**: Boolean (true/false)
- **difficulty_modifier**: Numeric >= 1.00 (MUST justify if > 1.0)
- **notes**: Service details + Wikipedia citation with revision date

### Wikipedia Citation Format
**REQUIRED in every notes field:**
```
"Data sourced from Wikipedia [Article Name] article, December 19, 2024 revision."
```

## 🎓 Quality Standards

### Factual Accuracy
- Use **ONLY Wikipedia** as primary source
- If unclear, leave it out (don't guess!)
- Cross-reference platform-shared models (GMT400, Lambda, T1XX, etc.)
- Record exact URLs with revision dates

### JSON Integrity
- Preserve insertion order (change history)
- Ensure hybrid/diesel flags match powertrain lists
- Use arrays for ALL multi-valued fields
- Each generation = separate JSON object (never overwrite)

### Documentation Requirements
- All difficulty_modifier values need justification
- All entries cite Wikipedia with revision date
- Platform sharing documented (e.g., "GMT400 platform shared with Chevrolet Silverado")
- Service-critical details: timing chain/belt, HV battery, specialty tools

## 🚀 Complete Example: Ford F-150 Research

**Let's walk through researching ONE model completely:**

### Step 1: Setup (if new manufacturer)
```bash
mkdir -p wip/ford
touch wip/ford/PROGRESS_TRACKER.md
touch wip/ford/2020s.json
```

### Step 2: Find Wikipedia Info
```bash
# Search for the model
curl -s "https://en.wikipedia.org/wiki/Ford_F-150" | grep -i "fourteenth generation"

# Note: Found "Ford F-150 (fourteenth generation)" page exists
```

### Step 3: Research Details
Visit Wikipedia page (or use curl) and note:
- Years: 2021-2025
- Engines: 3.3L V6 (290 hp), 2.7L EcoBoost (325 hp), 5.0L V8 (400 hp), 3.5L EcoBoost (400 hp), PowerBoost hybrid (430 hp)
- Transmission: 10-speed automatic
- Drivetrain: RWD or 4WD
- Body: Regular Cab, SuperCab, SuperCrew
- Platform: T1

### Step 4: Write JSON Entry
```bash
cat > wip/ford/2020s.json << 'EOF'
[
  {
    "years": [2021, 2022, 2023, 2024, 2025],
    "make": "Ford",
    "model": "F-150 (Fourteenth generation, T1)",
    "engines": [
      "3.3L Ti-VCT V6 (290 hp)",
      "2.7L EcoBoost V6 (325 hp)",
      "5.0L Ti-VCT V8 (400 hp)",
      "3.5L EcoBoost V6 (400 hp)",
      "3.5L PowerBoost V6 hybrid (430 hp combined)"
    ],
    "transmissions": ["10-speed automatic"],
    "region": "American",
    "drivetrain": ["RWD", "4WD"],
    "body_styles": ["Regular Cab", "SuperCab", "SuperCrew"],
    "hybrid": true,
    "diesel": false,
    "difficulty_modifier": 1.1,
    "notes": "Fourteenth generation on T1 platform (2021-present). PowerBoost hybrid variant uses 3.5L EcoBoost with 35 kW electric motor and 1.5 kWh battery, difficulty modifier 1.1 for hybrid system. Aluminum body construction. Pro Power Onboard generator optional. Data sourced from Wikipedia Ford F-150 (fourteenth generation) article, December 19, 2024 revision."
  }
]
EOF
```

### Step 5: Validate
```bash
jq empty wip/ford/2020s.json
# Should output nothing if valid
# If error, fix JSON syntax
```

### Step 6: Update Progress Tracker
```bash
cat >> wip/ford/PROGRESS_TRACKER.md << 'EOF'
### 2020s Models - 🔄 IN PROGRESS
- [x] F-150 (Fourteenth generation) - https://en.wikipedia.org/wiki/Ford_F-150_(fourteenth_generation)
- [ ] Bronco (Sixth generation)
- [ ] Mustang Mach-E
- [ ] ... (other 2020s models)
EOF
```

### Step 7: Continue with More Models
Add next model to the SAME file:
```bash
# Edit wip/ford/2020s.json
# Add comma after first entry's closing }
# Add second entry
# Validate again with jq empty
```

### Step 8: Mark Decade Complete
When all 2020s models done:
```bash
jq empty wip/ford/2020s.json && echo "✅ Ready to append"
# Update tracker: change status to ⏳ READY
```

### Step 9: Repeat for Other Decades
Do 2010s, 2000s, 1990s, 1980s...

### Step 10: Batch Append When Ready
```bash
# Backup first!
cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)

# Merge all decades
jq -s '.[0] + .[1] + .[2]' \
  vehicles.json \
  wip/ford/2020s.json \
  wip/ford/2010s.json \
  > vehicles_temp.json

mv vehicles_temp.json vehicles.json

# Validate
jq empty vehicles.json

# Archive files
mv wip/ford/2020s.json wip/ford/2020s_APPENDED.json
mv wip/ford/2010s.json wip/ford/2010s_APPENDED.json
```

## 📖 Reference Files

**See these for examples:**
- `wip/gmc/PROGRESS_TRACKER.md` - Complete tracking example
- `GMC_PHASE1_COMPLETION_REPORT.md` - Completion documentation
- `CHEVROLET_GAP_ANALYSIS.md` - Gap analysis workflow
- `wip/gmc/2020s_APPENDED.json` - Validated decade file

## 🔍 Platform Sharing (Document This!)

**GM Truck Platforms:**
- GMT400 (1988-1998): Sierra/Silverado
- GMT800 (1999-2006): Sierra/Silverado, Yukon/Tahoe
- GMT900 (2007-2013): Sierra/Silverado
- K2XX (2014-2020): Sierra/Silverado, Yukon/Tahoe
- T1XX (2019-present): Current Sierra/Silverado, Yukon/Tahoe
- Lambda (2007-2016): Acadia/Traverse/Enclave
- Theta (2010-2017): Terrain/Equinox

**Cross-reference for engine/transmission consistency!**

## ⚡ Quick Decision Tree

**Just started?** → Read PROGRESS_TRACKER.md first
**Status shows ⏳ READY?** → Go to Phase 4 (Batch Append)
**Status shows 🔄 IN PROGRESS?** → Continue research for that decade
**Status shows ✅ APPENDED?** → Create completion report or start next manufacturer
**No PROGRESS_TRACKER.md exists?** → Start Phase 1 (Setup)

## 💡 Pro Tips

1. **Token Efficiency**: Never read vehicles.json - use grep/jq
2. **Stay Organized**: Update PROGRESS_TRACKER.md after EVERY model
3. **Validate Early**: Check with `jq empty` after each decade
4. **Backup Always**: Never skip the backup step
5. **Batch Appending**: Append multiple decades at once (more efficient)

## ❓ When In Doubt

1. Read `PROMPT.md` for comprehensive instructions
2. Check `WORKFLOW.md` for step-by-step procedures
3. Look at `wip/gmc/PROGRESS_TRACKER.md` for organization example
4. Follow the 5-phase workflow exactly as written
5. **Don't skip steps!**

---

**Remember: Organization prevents chaos, tracking prevents loss, validation prevents corruption, backup prevents disasters.**

**When you start work, your first command should always be:**
```bash
cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
```

**This tells you EXACTLY what to do next. Follow it!**

## 🐛 Common Problems & Solutions

### Problem: "jq parse error"
**Cause**: JSON syntax error (missing comma, bracket, etc.)

**Solution**:
```bash
# Check the file for syntax errors
jq . wip/ford/2020s.json

# Common issues:
# 1. Missing comma between entries
# 2. Extra comma after last entry
# 3. Missing quotes around strings
# 4. Unclosed brackets/braces

# Fix and validate again
jq empty wip/ford/2020s.json
```

### Problem: "Can't find Wikipedia info"
**Solution**: Try "List of [Manufacturer] vehicles" pages first
```bash
curl -s "https://en.wikipedia.org/wiki/List_of_Ford_vehicles" | grep -i "f-150"
```

### Problem: "Lost track of where I am"
**Solution**: Check tracker
```bash
cat wip/ford/PROGRESS_TRACKER.md
```

## 📝 JSON Syntax Cheat Sheet

**Valid structure:**
```json
[
  {
    "field": "value"
  },
  {
    "field": "value"  
  }
]
```

**Rules**:
1. Comma after `}` if another entry follows
2. NO comma before final `]`
3. Double quotes for strings
4. Brackets for arrays `["item1", "item2"]`
5. No quotes for numbers or booleans

## 🎯 Work Session Checklist

Every session:
1. [ ] Read PROGRESS_TRACKER.md first
2. [ ] Identify which decade to work on
3. [ ] Research one model at a time
4. [ ] Update tracker after each model
5. [ ] Validate JSON after each model
6. [ ] Mark decade ⏳ READY when complete
7. [ ] Batch append when multiple decades ready
8. [ ] Archive files with _APPENDED suffix
