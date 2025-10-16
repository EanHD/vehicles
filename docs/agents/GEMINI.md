# GEMINI Agent Instructions - Vehicle Dataset

## 🎯 START HERE: First Command to Run

**Every time you begin work or resume a task:**

```bash
cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
```

**This single file tells you:**
- ✅ What's already done
- 🔄 What's in progress
- ⏳ What's ready to append
- ❌ What hasn't been started
- 📍 Exactly which phase to continue

**Don't guess. Don't explore. Read this file first!**

## 🚨 STOP! Read These Rules Before Doing ANYTHING

### ❌ NEVER Do This:
- **DON'T** use Read tool on `vehicles.json` (too large, wastes tokens)
- **DON'T** append directly to `vehicles.json` (corrupts data)
- **DON'T** work without `PROGRESS_TRACKER.md` (you'll lose track)
- **DON'T** skip `jq empty` validation (catches errors)
- **DON'T** skip backup before merging (no safety net)
- **DON'T** guess data (if Wikipedia unclear, omit it)

### ✅ ALWAYS Do This:
- **DO** use grep/jq for `vehicles.json` queries (fast, efficient)
- **DO** work in `wip/[manufacturer]/[decade].json` files (organized)
- **DO** update `PROGRESS_TRACKER.md` constantly (stay organized)
- **DO** validate with `jq empty` after each file (catch errors early)
- **DO** backup before appending (safety first)
- **DO** cite Wikipedia with dates (quality standard)

## 📋 The Complete 5-Phase Workflow

### Phase 1: Setup & Planning
**What**: Create workspace and figure out what needs research

**Commands:**
```bash
# Create manufacturer directory
mkdir -p wip/[manufacturer]

# Create progress tracker (MANDATORY!)
touch wip/[manufacturer]/PROGRESS_TRACKER.md
```

**PROGRESS_TRACKER.md Must Have:**
1. **Status table** with emoji indicators
2. **Per-decade model lists** with checkboxes [ ] and [x]
3. **Wikipedia URLs** with revision dates
4. **Current count** of entries in vehicles.json

**Status Table Example:**
```markdown
| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 8      | ✅ 8/8 | `2020s.json` ✅ | ✅ APPENDED |
| 2010s  | 5      | 🔄 3/5 | `2010s.json` ⏳ | ❌ |
| 2000s  | 6      | ⏳ 0/6 | - | ❌ |
```

**Emoji Legend:**
- ⏳ = TODO (not started)
- 🔄 = IN PROGRESS (actively researching)
- ✅ = DONE (complete and validated)
- 🔜 = LATER (planned for future phase)

**Check Current Coverage:**
```bash
# Count existing entries (use grep, NOT Read!)
grep -c '"make": "Buick"' vehicles.json

# List existing models
grep -A 1 '"make": "Buick"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq
```

### Phase 2: Research Models Decade-by-Decade
**What**: Create isolated JSON files for each decade

**Commands:**
```bash
# Create decade file
touch wip/buick/2020s.json
```

**For EVERY Model, Capture These Fields:**

```json
{
  "years": [2020, 2021, 2022, 2023, 2024],
  "make": "Buick",
  "model": "Enclave (C1XX)",
  "engines": ["3.6L V6 (310 hp)"],
  "transmissions": ["9-speed automatic"],
  "region": "American",
  "drivetrain": ["FWD", "AWD"],
  "body_styles": ["5-door crossover SUV"],
  "hybrid": false,
  "diesel": false,
  "difficulty_modifier": 1.0,
  "notes": "Second-generation Enclave on C1XX platform. Data sourced from Wikipedia Buick Enclave article, December 19, 2024 revision."
}
```

**Field Requirements:**
- **years**: Array of integers (North American model years only)
- **make**: Manufacturer name
- **model**: Name + generation code (e.g., "Corvette (C8)")
- **engines**: Displacement + HP (e.g., "5.3L V8 (355 hp)")
- **transmissions**: Gear counts + codes (e.g., "10-speed automatic")
- **region**: "American", "Canadian", "Japanese import", etc.
- **drivetrain**: Array format: ["FWD"], ["RWD", "AWD"], etc.
- **body_styles**: Array (e.g., ["2-door coupe", "2-door convertible"])
- **hybrid**: Boolean (true/false)
- **diesel**: Boolean (true/false)
- **difficulty_modifier**: Number >= 1.00 (see scale below)
- **notes**: Service details + Wikipedia citation (REQUIRED)

**Difficulty Modifier Scale:**
```
1.0  = Standard modern vehicle
1.1  = Diesel, basic hybrid, complex service access
1.2  = Brass-era (1910s-1920s), turbo, medium-duty commercial
1.3  = Heavy-duty commercial, air brakes, complex vintage
1.4+ = High-voltage EVs (400V+), switchable voltage platforms
```

**IMPORTANT**: All modifiers >= 1.1 MUST have justification in notes!

**Research Process:**
1. Find Wikipedia generation-specific page
2. Capture all fields (don't skip any!)
3. Update PROGRESS_TRACKER.md in real-time
4. Validate: `jq empty wip/buick/2020s.json`

### Phase 3: Validation Before Appending
**What**: Double-check everything before merging

**Validation Checklist (per decade):**
- [ ] All models researched with Wikipedia citations
- [ ] JSON validates: `jq empty wip/[manufacturer]/[decade].json`
- [ ] All difficulty_modifier >= 1.00 with justification in notes
- [ ] All required fields present
- [ ] No duplicate entries
- [ ] Hybrid/diesel flags match powertrains listed
- [ ] Notes include Wikipedia citation with revision date
- [ ] Platform sharing documented where relevant

**When Complete:**
Update PROGRESS_TRACKER.md status to `⏳ READY`

### Phase 4: Batch Append to vehicles.json
**What**: Safely merge validated decades into production dataset

**⚠️ CRITICAL: Only append after ALL target decades are validated!**

**Step-by-Step Commands:**

```bash
# STEP 1: BACKUP (NEVER SKIP THIS!)
cp vehicles.json vehicles.json.backup_$(date +%Y%m%d_%H%M%S)

# STEP 2: MERGE multiple decades at once
jq -s '.[0] + .[1] + .[2] + .[3] + .[4]' \
  vehicles.json \
  wip/buick/1980s.json \
  wip/buick/1990s.json \
  wip/buick/2000s.json \
  wip/buick/2010s.json \
  wip/buick/2020s.json \
  > vehicles_temp.json

mv vehicles_temp.json vehicles.json

# STEP 3: VALIDATE merged file (CRITICAL!)
jq empty vehicles.json
# ⚠️ If this fails, RESTORE FROM BACKUP IMMEDIATELY:
# mv vehicles.json.backup_[timestamp] vehicles.json

# STEP 4: VERIFY entry count
grep -c '"make": "Buick"' vehicles.json
# Compare this number to expected count in PROGRESS_TRACKER.md

# STEP 5: ARCHIVE completed decade files
cd wip/buick
for decade in 1980s 1990s 2000s 2010s 2020s; do
  mv ${decade}.json ${decade}_APPENDED.json
done

# STEP 6: UPDATE PROGRESS_TRACKER.md
# Change ⏳ READY to ✅ APPENDED for all merged decades
# Update "Current vehicles.json count" with new total
# Add append date/timestamp
```

### Phase 5: Manufacturer Completion
**What**: Document completion and move to next manufacturer

**Steps:**
1. Create completion report (see `GMC_PHASE1_COMPLETION_REPORT.md` for example)
2. Update `CHECKLIST.md` status note with completion date
3. Update `CHECKLIST_STATUS.md` (ONLY when manufacturer is 100% complete)
4. Move to next manufacturer

## 🔧 Essential Commands Reference

### Querying vehicles.json (Use These, Not Read!)

```bash
# Count entries for a manufacturer
grep -c '"make": "Buick"' vehicles.json

# List all models for a manufacturer
grep -A 1 '"make": "Buick"' vehicles.json | grep '"model":' | sed 's/.*"model": "\([^"]*\)".*/\1/' | sort | uniq

# Search for specific model
grep '"model": "Enclave"' vehicles.json

# Extract all entries for manufacturer (use cautiously)
jq '[.[] | select(.make == "Buick")]' vehicles.json > buick_entries.json
```

### JSON Validation

```bash
# Validate decade file
jq empty wip/buick/2020s.json

# Count entries in decade file
jq 'length' wip/buick/2020s.json

# Pretty-print for review
jq . wip/buick/2020s.json

# Validate production dataset
jq empty vehicles.json
```

## 📚 Project Structure

```
vehicles/
├── vehicles.json                    # Production dataset (grep/jq ONLY!)
├── PROMPT.md                        # Complete workflow documentation
├── WORKFLOW.md                      # Step-by-step procedures
├── AGENTS.md                        # Agent-specific rules
├── README.md                        # Schema and contribution rules
├── CHECKLIST.md                     # Model roster per manufacturer
├── CHECKLIST_STATUS.md              # Manufacturer completion tracker
├── services.json                    # Mobile mechanic service catalog
├── wip/                             # Work-in-progress by manufacturer
│   ├── gmc/
│   │   ├── PROGRESS_TRACKER.md     # Real-time progress tracking
│   │   ├── 2020s_APPENDED.json     # Archived completed files
│   │   ├── 2010s_APPENDED.json
│   │   └── ...
│   ├── buick/
│   │   ├── PROGRESS_TRACKER.md
│   │   └── ...
│   └── [other manufacturers]/
├── GMC_PHASE1_COMPLETION_REPORT.md  # Example completion report
└── CHEVROLET_GAP_ANALYSIS.md        # Example gap analysis
```

## 🎓 Quality Standards

### Data Accuracy
- **Primary Source**: Wikipedia ONLY
- **If Unclear**: Leave it out (don't guess!)
- **Platform Sharing**: Cross-reference (GMT400, Lambda, T1XX, etc.)
- **Citations**: Record URLs with revision dates

### JSON Integrity
- **Order**: Preserve insertion order (maintains change history)
- **Flags**: Ensure hybrid/diesel flags match powertrain arrays
- **Arrays**: Use arrays for ALL multi-valued fields
- **Generations**: Each generation = separate object (never overwrite)

### Documentation
- **Difficulty Modifiers**: All values >= 1.1 need justification
- **Wikipedia Citations**: REQUIRED in every notes field
- **Platform Sharing**: Document shared platforms
- **Service Details**: Include timing chain/belt, HV battery, specialty tools

**Wikipedia Citation Format:**
```
"Data sourced from Wikipedia [Article Name] article, December 19, 2024 revision."
```

## 🚀 Example Walkthrough: Starting Buick

```bash
# 1. SETUP
mkdir -p wip/buick
touch wip/buick/PROGRESS_TRACKER.md

# 2. CHECK CURRENT COVERAGE
grep -c '"make": "Buick"' vehicles.json
# Output: 0 (not started yet)

# 3. CREATE PROGRESS TRACKER
# Add status table, model lists, etc.

# 4. START WITH 2020s
touch wip/buick/2020s.json
# Research Encore, Encore GX, Envision, Enclave

# 5. UPDATE TRACKER AS YOU GO
# Mark each model [x] when complete

# 6. VALIDATE
jq empty wip/buick/2020s.json
# ✅ Passes

# 7. MARK DECADE READY
# Update tracker: 2020s status = ⏳ READY

# 8. REPEAT for 2010s, 2000s, etc.

# 9. BATCH APPEND when all decades ready
# Follow Phase 4 steps
```

## 📖 Reference Files (Learn From These!)

- **wip/gmc/PROGRESS_TRACKER.md** - Perfect tracking example
- **GMC_PHASE1_COMPLETION_REPORT.md** - How to document completion
- **CHEVROLET_GAP_ANALYSIS.md** - Gap analysis workflow
- **wip/gmc/2020s_APPENDED.json** - Validated decade file example

## 🔍 Platform Sharing Reference

**Document platform sharing in notes field!**

**GM Platforms:**
- **GMT400** (1988-1998): Sierra/Silverado pickups
- **GMT800** (1999-2006): Sierra/Silverado, Yukon/Tahoe
- **GMT900** (2007-2013): Sierra/Silverado light-duty
- **K2XX** (2014-2020): Sierra/Silverado, Yukon/Tahoe
- **T1XX** (2019-present): Current Sierra/Silverado, Yukon/Tahoe
- **Lambda** (2007-2016): Acadia/Traverse/Enclave crossovers
- **Theta** (2010-2017): Terrain/Equinox compact crossovers
- **C1XX** (2018-present): Traverse/Enclave/XT6

**Cross-reference for engine/transmission consistency!**

## ⚡ Quick Decision Tree

**Starting fresh?**
→ Read PROGRESS_TRACKER.md first (or create if doesn't exist)

**Tracker shows ⏳ READY?**
→ Go to Phase 4 (Batch Append)

**Tracker shows 🔄 IN PROGRESS?**
→ Continue research for that decade

**Tracker shows ✅ APPENDED?**
→ Create completion report or start next manufacturer

**No PROGRESS_TRACKER.md?**
→ Start Phase 1 (Setup & Planning)

## 💡 Pro Tips for Success

1. **Token Efficiency**: NEVER read vehicles.json - always use grep/jq
2. **Stay Organized**: Update PROGRESS_TRACKER.md after EVERY model
3. **Validate Early**: Run `jq empty` after each decade, not just at the end
4. **Always Backup**: Never skip the backup step - it saves you from disasters
5. **Batch Smartly**: Append multiple decades at once (Phase 1: 1980s-2020s, Phase 2: 1910s-1970s)
6. **Real-Time Updates**: Don't wait to update tracker - do it as you work
7. **Check Examples**: Look at wip/gmc/ for organization patterns

## ❓ When You're Stuck

1. **Read PROMPT.md** - Comprehensive workflow instructions
2. **Check WORKFLOW.md** - Detailed step-by-step procedures
3. **Look at wip/gmc/PROGRESS_TRACKER.md** - Perfect example
4. **Follow the 5 phases** - They're designed to prevent problems
5. **Don't skip steps** - Each step has a purpose

## 🎯 Special Vehicle Categories

### Brass-Era (1910s-1920s)
- Difficulty: 1.2-1.3 (fragile, obsolete tooling)
- Use era-appropriate field values
- Document restoration complexity

### Electric Vehicles (EVs)
- Difficulty: 1.4+ (high-voltage 400V+)
- Document battery platform (Ultium, MEB, etc.)
- Note voltage specifications
- Specify EV-certified technician requirements

### Commercial Trucks
- Medium-duty: 1.2 (air brakes, commercial cert needed)
- Heavy-duty: 1.3 (advanced air systems, weight ratings)
- Document configurations and requirements

### Performance Vehicles
- Turbocharged/supercharged: 1.1-1.2
- Document specialty tuning needs
- Note performance-oriented service knowledge

## 📊 Success Metrics

**You know you're doing it right when:**
- ✅ PROGRESS_TRACKER.md is always up-to-date
- ✅ Every decade file validates with `jq empty`
- ✅ No data corruption in vehicles.json
- ✅ Every entry has Wikipedia citation
- ✅ Backup exists before every merge
- ✅ Entry counts match expectations
- ✅ Platform sharing documented
- ✅ Difficulty modifiers justified

## 🔐 Safety Checklist

**Before EVERY append to vehicles.json:**
- [ ] All decade files validated individually
- [ ] Backup created with timestamp
- [ ] PROGRESS_TRACKER.md shows ⏳ READY status
- [ ] Entry counts calculated and documented
- [ ] jq merge command double-checked
- [ ] Ready to restore from backup if needed

---

## 🎬 Your First Action Every Time

```bash
cat wip/[current_manufacturer]/PROGRESS_TRACKER.md
```

**This one command tells you everything you need to know.**

**No PROGRESS_TRACKER.md?** Create it first thing!

**Remember:**
- **Organization prevents chaos**
- **Tracking prevents loss**
- **Validation prevents corruption**
- **Backup prevents disasters**

**Now go build the best vehicle dataset ever! 🚗🔧**
