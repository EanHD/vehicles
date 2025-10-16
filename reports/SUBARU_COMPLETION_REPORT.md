# Subaru Historical Coverage Completion Report

**Date**: January 17, 2025  
**Manufacturer**: Subaru  
**Coverage Period**: 1970-2025 (North American market)  
**Total Entries Added**: 50 models

---

## Summary

Subaru historical coverage is now **COMPLETE** with comprehensive documentation of all models sold in the North American market from the early 1970s through 2025. This includes the iconic AWD lineup, performance WRX/STI variants, and the unique boxer engine heritage that defines Subaru.

---

## Coverage Breakdown by Decade

| Decade | Entries | Key Models |
|--------|---------|------------|
| **2020s** | 10 | Legacy 7th gen, Outback 6th gen, WRX VB, Crosstrek 3rd gen, Solterra EV, BRZ 2nd gen, Ascent |
| **2010s** | 14 | Legacy 5th/6th gen, WRX VA, Crosstrek debut, BRZ debut, Forester SJ/SK, Ascent launch |
| **2000s** | 13 | Legacy 4th gen, WRX/STI U.S. debut, Impreza GD/GG/GE, Forester SG/SH, B9 Tribeca, Baja |
| **1990s** | 6 | Legacy 1st/2nd gen, Impreza debut, Forester debut, Outback debut, SVX |
| **1980s** | 5 | Leone/GL, BRAT, Justy, XT/Alcyone, Legacy development |
| **1970s** | 2 | Leone/DL/GL, BRAT launch |

**Total**: 50 Subaru entries spanning 55 years

---

## Notable Model Highlights

### Symmetrical All-Wheel Drive Legacy
- **Leone/DL/GL** (1972-1994): Established Subaru's AWD reputation
- **Legacy** (1990-present): Seven generations of midsize sedan/wagon
- **Outback** (1995-present): Pioneered crossover-wagon segment
- **Impreza** (1993-present): Compact AWD standard-bearer
- **Forester** (1998-present): Defined compact crossover SUV
- **Crosstrek** (2013-present): Subcompact crossover success

*AWD standard on nearly all Subaru models (except BRZ)*

### Performance WRX/STI Heritage
- **WRX (GD/GG)** (2002-2007): First U.S.-market turbocharged AWD sedan
- **WRX STI (GD/GG)** (2004-2007): High-performance variant debut
- **WRX (GE/GR)** (2008-2014): Hatchback body style added
- **WRX (VA)** (2015-2021): Standalone model, separated from Impreza
- **WRX (VB)** (2022-present): 2.4L turbo boxer, no STI variant

*All performance models assigned difficulty_modifier 1.2-1.3 due to turbo complexity*

### Boxer Engine Heritage
- **EA series** (1970s-1980s): 1.4L-1.8L flat-four engines
- **EJ series** (1989-present): 1.8L-2.5L SOHC/DOHC, turbocharged variants
- **EZ series** (2000s): 3.0L-3.6L flat-six engines
- **FA/FB series** (2012+): Direct injection, improved efficiency
- **Horizontally-opposed layout**: Lower center of gravity, balanced weight distribution

### Unique & Iconic Models
- **BRAT** (1978-1987): Compact pickup with jump seats in bed
- **XT/Alcyone** (1985-1991): Wedge-shaped sports coupe with asymmetric steering
- **SVX** (1992-1996): Flat-six luxury sports coupe with unique window design
- **Baja** (2003-2006): Pickup/utility vehicle with switchback midgate
- **BRZ** (2013-present): RWD sports coupe (Toyota 86 twin)
- **Solterra** (2023-present): First battery electric Subaru (Toyota bZ4X twin)

### Three-Row SUVs
- **B9 Tribeca** (2006-2009): First attempt at midsize SUV
- **Tribeca** (2008-2014): Revised styling, continued three-row offering
- **Ascent** (2019-present): Current three-row flagship, Indiana-built

---

## Technical Considerations Documented

### Symmetrical All-Wheel Drive
- Longitudinal boxer engine layout with symmetrical drivetrain
- Improved traction, stability, and handling
- Standard on most models (BRZ is RWD exception)
- Driver-controlled center differential on performance models

### Boxer Engine Benefits
- Lower center of gravity compared to inline/V-configuration
- Balanced weight distribution (near 50/50)
- Smooth operation with inherently balanced design
- Distinctive exhaust note

### Turbocharged Performance
- WRX: 2.0L or 2.5L turbo boxer (268-310 hp)
- Intercooler, upgraded turbo systems
- Higher difficulty modifiers (1.2-1.3) reflect maintenance complexity
- Performance-oriented suspension, brakes, differentials

### Hybrid/Electric Systems
- **Crosstrek Hybrid PHEV** (2019+): 8.8 kWh battery, 17 miles electric range
- **Solterra BEV** (2023+): 72.8 kWh battery, dual-motor AWD, ~228 miles range
- Difficulty modifier 1.2-1.3 for high-voltage system service requirements

### CVT Technology
- Lineartronic CVT standard on most models (2010s+)
- Simulated gear ratios on performance models
- Smooth power delivery and improved fuel efficiency

---

## Quality Assurance

All entries include:
- ✅ Comprehensive engine specifications with boxer configuration
- ✅ Complete transmission options (manual/automatic/CVT)
- ✅ Accurate drivetrain configurations (FWD/AWD/4WD/RWD)
- ✅ Body style variations documented
- ✅ Hybrid/EV flags accurately set
- ✅ Difficulty modifiers justified (turbo, PHEV, EV)
- ✅ Wikipedia citations with December 19, 2024 revision dates
- ✅ Platform sharing documented (Toyota partnerships: BRZ, Solterra)
- ✅ Service-critical details (AWD systems, boxer engines, turbo maintenance)

---

## Data Validation

All decade files validated with `jq empty` before merge:
- ✅ 1970s.json (2 entries)
- ✅ 1980s.json (5 entries)
- ✅ 1990s.json (6 entries)
- ✅ 2000s.json (13 entries)
- ✅ 2010s.json (14 entries)
- ✅ 2020s.json (10 entries)

**Final validation**: `jq empty vehicles.json` - PASSED  
**Entry verification**: `grep -c '"make": "Subaru"' vehicles.json` - 50 entries confirmed

---

## Special Notes

### AWD Innovation
Subaru pioneered mass-market all-wheel drive systems in the 1970s with the Leone/DL/GL. The symmetrical AWD system with longitudinal boxer engine layout became Subaru's signature technology, differentiating it from competitors' transverse-based AWD systems.

### Rally Heritage
The WRX and STI models draw directly from Subaru's World Rally Championship success. Colin McRae, Petter Solberg, and other legendary drivers piloted Impreza WRCs to multiple championships, establishing Subaru's performance credentials.

### Practical Innovation
Models like the BRAT (jump seats to circumvent tariffs), Baja (switchback midgate), and Justy (early CVT adoption) demonstrate Subaru's willingness to innovate and create practical, unique vehicles.

### Toyota Collaborations
- **BRZ/86**: Joint sports car project leveraging Subaru's boxer expertise and Toyota's efficiency
- **Solterra/bZ4X**: Shared EV platform reducing development costs while maintaining brand identity

---

## Next Steps

- [x] All decades researched and validated
- [x] All entries appended to vehicles.json
- [x] vehicles.json validated successfully
- [x] Progress tracker updated
- [x] Completion report created
- [x] CHECKLIST_STATUS.md updated

---

## Files Created

- `wip/subaru/PROGRESS_TRACKER.md` - Real-time progress tracking
- `wip/subaru/1970s_APPENDED.json` - 2 archived entries
- `wip/subaru/1980s_APPENDED.json` - 5 archived entries
- `wip/subaru/1990s_APPENDED.json` - 6 archived entries
- `wip/subaru/2000s_APPENDED.json` - 13 archived entries
- `wip/subaru/2010s_APPENDED.json` - 14 archived entries
- `wip/subaru/2020s_APPENDED.json` - 10 archived entries
- `SUBARU_COMPLETION_REPORT.md` - This completion report

---

**Subaru historical coverage: COMPLETE ✅**
