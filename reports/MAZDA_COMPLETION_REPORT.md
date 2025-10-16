# Mazda Historical Coverage Completion Report

**Date**: January 17, 2025  
**Manufacturer**: Mazda  
**Coverage Period**: 1970-2025 (North American market)  
**Total Entries Added**: 73 models

---

## Summary

Mazda historical coverage is now **COMPLETE** with comprehensive documentation of all models sold in the North American market from 1970 through 2025. This includes the iconic rotary-engined sports cars, the revolutionary MX-5 Miata, and the modern SkyActiv-era crossovers and sedans.

---

## Coverage Breakdown by Decade

| Decade | Entries | Key Models |
|--------|---------|------------|
| **2020s** | 10 | Mazda3 BP, CX-30, CX-50, CX-70, CX-90, MX-30 EV, MX-5 ND refresh |
| **2010s** | 17 | SkyActiv introduction, CX-5, CX-3, CX-9 TC, Mazda3 BM/BN, MX-5 ND |
| **2000s** | 16 | Mazda3 debut, Mazda6, RX-8, CX-7, CX-9, Tribute, Zoom-Zoom era |
| **1990s** | 11 | MX-5 Miata NA/NB, RX-7 FD, Millenia, Protegé, MPV LW |
| **1980s** | 10 | RX-7 SA/FB/FC, 626 GC/GD, 323/GLC, MX-6, MPV LV launch |
| **1970s** | 9 | RX-2, RX-3, RX-4, RX-7 SA, GLC, B-Series, 808, Cosmo |

**Total**: 73 Mazda entries spanning 55 years

---

## Notable Model Highlights

### Rotary-Engined Vehicles (Wankel Engine)
- **RX-2** (1971-1978): 12A rotary, compact sedan/coupe
- **RX-3** (1972-1978): 12A rotary, sports coupe, racing success
- **RX-4** (1974-1978): 13B rotary debut, midsize sedan
- **RX-7 SA/FB** (1978-1985): First-generation sports car, 12A rotary
- **RX-7 FC** (1986-1989): Second-generation, 13B turbo available
- **RX-7 FD** (1993-1995 NA): Third-generation, sequential twin-turbo
- **RX-8** (2004-2011): Renesis rotary, freestyle doors
- **Cosmo** (1976-1979): Luxury rotary coupe

*All rotary models assigned difficulty_modifier 1.3-1.4 due to specialized maintenance requirements*

### MX-5 Miata Legacy
- **NA** (1989-1997): Revolutionary affordable roadster, 1.6L/1.8L
- **NB** (1998-2005): Refined second generation
- **NC** (2006-2015): Larger third generation, PRHT available
- **ND** (2016-2025): Fourth generation with SkyActiv, RF variant

### Ford Partnership Vehicles
- **B-Series** (1970s-2009): Compact pickup based on Ford Ranger
- **Tribute** (2001-2011): Compact SUV based on Ford Escape platform
- Shared platforms and powertrains with Ford Motor Company

### SkyActiv Technology Era (2012+)
- Introduction of high-efficiency SkyActiv-G engines
- SkyActiv-Drive transmissions
- Improved fuel economy and emissions
- Models: Mazda3, Mazda6, CX-3, CX-5, CX-9, CX-30

### Recent Platform Evolution
- **Large Product Group** (2024+): Inline-six RWD-based architecture
- **CX-70/CX-90**: 3.3L turbo I6, PHEV variants
- Return to longitudinal engine layout and rear-wheel-drive roots

---

## Technical Considerations Documented

### Rotary Engine Complexity
- Apex seal maintenance and replacement
- Oil consumption monitoring (by design)
- Specialized compression testing procedures
- Lower fuel efficiency compared to piston engines
- Higher difficulty modifiers (1.3-1.4) reflect specialized knowledge requirements

### SkyActiv Technology
- High-compression naturally aspirated engines
- Optimized transmissions for efficiency
- Lightweight body construction
- Advanced engine management systems

### Hybrid/Electric Systems
- **Tribute Hybrid** (2007-2011): Ford partnership hybrid system
- **CX-70/CX-90 PHEV** (2024+): 2.5L I4 + electric motor, 17.8 kWh battery
- **MX-30 EV** (2022-2023): 35.5 kWh battery, limited California availability

---

## Quality Assurance

All entries include:
- ✅ Comprehensive engine specifications with power outputs
- ✅ Complete transmission options (manual/automatic)
- ✅ Accurate drivetrain configurations (FWD/RWD/AWD/4WD)
- ✅ Body style variations (sedan, coupe, hatchback, crossover, etc.)
- ✅ Hybrid/diesel flags accurately set
- ✅ Difficulty modifiers justified in notes (rotary engines, PHEV systems)
- ✅ Wikipedia citations with December 19, 2024 revision dates
- ✅ Platform sharing documented (Ford partnerships)
- ✅ Service-critical details (rotary maintenance, hybrid systems)

---

## Data Validation

All decade files validated with `jq empty` before merge:
- ✅ 1970s.json (9 entries)
- ✅ 1980s.json (10 entries)
- ✅ 1990s.json (11 entries)
- ✅ 2000s.json (16 entries)
- ✅ 2010s.json (17 entries)
- ✅ 2020s.json (10 entries)

**Final validation**: `jq empty vehicles.json` - PASSED  
**Entry verification**: `grep -c '"make": "Mazda"' vehicles.json` - 73 entries confirmed

---

## Special Notes

### Rotary Engine Heritage
Mazda's commitment to Wankel rotary engine technology is unique among mainstream manufacturers. From the RX-2 in 1971 through the RX-8's discontinuation in 2011, Mazda produced numerous rotary-powered vehicles that require specialized maintenance knowledge.

### MX-5 Miata Impact
The 1989 launch of the MX-5 Miata is credited with single-handedly reviving the affordable sports car market. Four generations spanning 35+ years demonstrate the model's enduring appeal.

### SkyActiv Philosophy
Mazda's SkyActiv technology (launched 2012) represents a comprehensive approach to vehicle efficiency without relying heavily on electrification, focusing instead on optimizing traditional internal combustion engines.

### Current Direction
Recent models (CX-70, CX-90) mark Mazda's return to inline-six engines and RWD-based platforms, differentiating from competitors' widespread adoption of transverse four-cylinder crossovers.

---

## Next Steps

- [x] All decades researched and validated
- [x] All entries appended to vehicles.json
- [x] vehicles.json validated successfully
- [x] Progress tracker updated
- [x] Completion report created
- [ ] Update CHECKLIST_STATUS.md
- [ ] Update CHECKLIST.md with completion note

---

## Files Created

- `wip/mazda/PROGRESS_TRACKER.md` - Real-time progress tracking
- `wip/mazda/1970s_APPENDED.json` - 9 archived entries
- `wip/mazda/1980s_APPENDED.json` - 10 archived entries
- `wip/mazda/1990s_APPENDED.json` - 11 archived entries
- `wip/mazda/2000s_APPENDED.json` - 16 archived entries
- `wip/mazda/2010s_APPENDED.json` - 17 archived entries
- `wip/mazda/2020s_APPENDED.json` - 10 archived entries
- `MAZDA_COMPLETION_REPORT.md` - This completion report

---

**Mazda historical coverage: COMPLETE ✅**
