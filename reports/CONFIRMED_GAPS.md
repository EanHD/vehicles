# Confirmed Dataset Gaps - Real-World Field Vehicles
**Date**: January 17, 2025
**Purpose**: Definitive list of missing vehicles that mechanics commonly encounter

## Critical Gaps Found

### 1. RAM TRUCKS - MISSING HISTORICAL GENERATIONS ⚠️ HIGH PRIORITY
**What's Missing**:
- **Dakota First Generation (1987-1996)**: Extremely common midsize truck
- **Dakota Third Generation (2005-2011)**: Final generation, still on roads
- **Ram 1500 Third Generation (2002-2008 DR/DH)**: Pre-brand split, very common
- **Ram 1500 Second Generation (1994-2001 BR/BE)**: Club Cab era, still serviced
- **Ramcharger (1974-1993)**: Full-size SUV based on Ram chassis
- **Ram Van/Wagon B-series (1970s-2003)**: Common commercial vehicle

**Current Coverage**: Only 2010s-2020s (7 entries total)
**Field Impact**: CRITICAL - These trucks are everywhere

### 2. TOYOTA - MISSING GENERATION
- **Sequoia Second Generation (XK60, 2008-2022)**: Gap between first and third gen
  - Current coverage: First gen (2001-2007), Third gen (2023+)
  - Missing: 14-year production run of popular full-size SUV

### 3. FORD - MISSING MODEL
- **EcoSport (2018-2022)**: Subcompact crossover sold in North America
  - Brazilian-built, then Indian-built
  - Discontinued 2022 but still common in service

### 4. MERCEDES-BENZ - MISSING COMMERCIAL VEHICLES
- **Sprinter (2019+ VS30/W907 generation)**: Ubiquitous commercial van
- **Metris (2016-2023 W447)**: Midsize commercial van, very common

### 5. DODGE - ADDITIONAL DAKOTA GENERATIONS
- **Dakota First Generation (1987-1996)**: Original compact truck
- **Dakota Third Generation (2005-2011)**: Final generation before Ram brand split
- **Current**: Only Second Generation (1997-2004) is in dataset

### 6. MINOR GAPS TO VERIFY
- **GMC Savana** - Check if all generations match Chevrolet Express
- **Ram 1500 Classic** - Verify if older DS platform continuation is documented
- **Honda Odyssey** - Verify all 5 generations are present (1995-2025)
- **Toyota Sienna** - Verify all 4 generations present (1998-2025)
- **Toyota Highlander** - Verify all 4 generations present (2001-2025)

## Gap Analysis Results

### Already Complete ✅
- Ford Transit ✓
- Chevrolet Express ✓
- Nissan NV series ✓
- Honda Ridgeline (all gens) ✓
- Honda Passport (both gens) ✓
- Toyota 4Runner (4 generations) ✓
- Chevrolet Bolt EUV ✓
- Ford Edge (3 generations) ✓

## Priority Order for Additions

### TIER 1 - Immediate (High Service Frequency)
1. **Ram Historical Trucks (1990s-2000s)** - 6 missing models
2. **Toyota Sequoia 2nd Gen** - 1 missing generation
3. **Mercedes Sprinter/Metris** - 2 missing commercial vehicles

### TIER 2 - Important
4. **Dodge Dakota 1st & 3rd Gen** - 2 missing generations
5. **Ford EcoSport** - 1 missing model
6. **Ram Ramcharger** - 1 missing SUV
7. **Ram Van B-series** - 1 missing commercial vehicle

### TIER 3 - Verification Pass
8. Verify Honda Odyssey generations (1st-5th)
9. Verify Toyota Sienna generations (1st-4th)
10. Verify Toyota Highlander generations (1st-4th)

## Implementation Plan

### Step 1: RAM TRUCKS (Highest Impact)
Create `wip/ram_additions/` directory for historical coverage:
- Research 1990s Ram models (Dakota 1st gen, Ram 1500 2nd gen)
- Research 2000s Ram models (Dakota 3rd gen, Ram 1500 3rd gen)
- Research Ram SUVs (Ramcharger)
- Research Ram Vans (B-series)

### Step 2: TOYOTA SEQUOIA
Add to existing `wip/toyota/` or create supplemental file:
- Research 2nd generation XK60 (2008-2022)

### Step 3: MERCEDES COMMERCIAL
Create `wip/mercedes_additions/` for commercial vehicles:
- Research Sprinter 2019+ generation
- Research Metris 2016-2023

### Step 4: REMAINING GAPS
- Ford EcoSport research
- Dodge Dakota 1st/3rd generation research
- Verification pass on Honda/Toyota SUV/van lineups

## Estimated Additions
- **Ram additions**: ~8-10 entries
- **Toyota Sequoia**: 1 entry
- **Mercedes commercial**: 2 entries
- **Dodge Dakota**: 2 entries
- **Ford EcoSport**: 1 entry
- **Total estimated**: 14-16 new entries

This will significantly improve real-world coverage for mobile mechanic operations.
