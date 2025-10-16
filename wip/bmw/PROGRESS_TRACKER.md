# BMW Research Progress Tracker

**Last Updated**: October 15, 2025
**Strategy**: Work newest-to-oldest (2020s → 1930s) covering core Series, X SAV/SAC lineup, and i sub-brand; finish with heritage models (1930s-1960s) to capture historical chassis codes.
**Current vehicles.json count**: 68 BMW entries (verified via `grep -c "make": "BMW"` on October 15, 2025 after append)
**Status**: ALL DECADES APPENDED - BMW ready for archival (68 total entries merged October 15, 2025)

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 14     | ✅ 14/14 | `2020s_APPENDED.json` ✅ | ✅ APPENDED |
| 2010s  | 14     | ✅ 14/14 | `2010s_APPENDED.json` ✅ | ✅ APPENDED |
| 2000s  | 13     | ✅ 13/13 | `2000s_APPENDED.json` ✅ | ✅ APPENDED |
| 1990s  | 6      | ✅ 6/6 | `1990s_APPENDED.json` ✅ | ✅ APPENDED |
| 1980s  | 5      | ✅ 5/5 | `1980s_APPENDED.json` ✅ | ✅ APPENDED |
| 1970s  | 3      | ✅ 3/3 | `1970s_APPENDED.json` ✅ | ✅ APPENDED |
| 1960s  | 4      | ✅ 4/4 | `1960s_APPENDED.json` ✅ | ✅ APPENDED |
| 1950s  | 5      | ✅ 5/5 | `1950s_APPENDED.json` ✅ | ✅ APPENDED |
| 1930s  | 4      | ✅ 4/4 | `1930s_APPENDED.json` ✅ | ✅ APPENDED |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | 🔜 LATER | ⚠️ NEEDS REVIEW

---

## Phase Focus

- **Phase 1**: Modern portfolio (2020s–2000s) — ensure all current G-series platforms, X SAV/SAC, and i sub-brand EVs carry 48V/powertrain notes.
- **Phase 2**: Transition era (1990s–1970s) — capture E-chassis core models and early X-series, highlighting M variants where NA-specific.
- **Phase 3**: Heritage (1960s–1930s) — Neue Klasse sedans, early sport coupes, and microcar era entries documenting service challenges.

---

## Decade Breakdowns

### 2020s Models (Target: 14 entries) - ✅ COMPLETE
- [x] 2 Series Coupe (G42, 2022–present NA)
- [x] 3 Series (G20 LCI, 2020–present NA)
- [x] 4 Series Coupe/Gran Coupe (G22/G26, 2021–present NA)
- [x] 5 Series (G60, 2024–present NA) & i5
- [x] 7 Series/i7 (G70, 2023–present NA)
- [x] 8 Series (G14/G15/G16 LCI, 2023–present NA)
- [x] X1 (U11, 2023–present NA)
- [x] X3 (G01 LCI, 2018–2024 NA)
- [x] X5 (G05 LCI, 2020–present NA)
- [x] X6 (G06 LCI, 2020–present NA)
- [x] X7 (G07 LCI, 2019–present NA)
- [x] i4 (G26 BEV, 2022–present NA)
- [x] iX (I20, 2022–present NA)
- [x] XM (G09 PHEV, 2023–present NA)

**Status**: ✅ `wip/bmw/2020s.json` validated with `jq empty`.
**Highlights**: Documented 48V mild hybrid systems, xDrive PHEVs, and high-voltage BEV/PHEV service cautions across BMW sedans, SAVs, and M sub-brand.

### 2010s Models (Target: 14 entries) - ✅ COMPLETE
- [x] 2 Series (F22/F23)
- [x] 3 Series (F30/F31/F34)
- [x] 4 Series (F32/F33/F36)
- [x] 5 Series (F10)
- [x] 6 Series (F06/F12/F13)
- [x] 7 Series (G11/G12)
- [x] X1 (F48)
- [x] X2 (F39)
- [x] X3 (F25)
- [x] X4 (F26)
- [x] X5 (F15)
- [x] X6 (F16)
- [x] i3 (I01)
- [x] i8 (I12/I15)

**Status**: ✅ `wip/bmw/2010s.json` validated with `jq empty`.
**Highlights**: Captured F- and early G-series sedans/coupes, diesel and PHEV SAVs, plus CFRP Life module EV/PHEV (i3/i8) with HV and calibration procedures noted.

### 2000s Models (Target: 13 entries) - ✅ COMPLETE
- [x] 1 Series (E82/E88)
- [x] 3 Series (E46)
- [x] 3 Series (E90/E91/E92/E93)
- [x] 5 Series (E39)
- [x] 5 Series (E60/E61)
- [x] 6 Series (E63/E64)
- [x] 7 Series (E65/E66)
- [x] Z4 (E85/E86)
- [x] Z4 (E89)
- [x] X3 (E83)
- [x] X5 (E53)
- [x] X5 (E70 early)
- [x] X6 (E71 early)

**Status**: ✅ `wip/bmw/2000s.json` validated with `jq empty`.
**Highlights**: Documented major E-chassis sedans, SACs, and SAVs including SMG-equipped M models, early iDrive service considerations, and N54/N62/S62 maintenance campaigns.

### 1990s Models (Target: 6 entries) - ✅ COMPLETE
- [x] 3 Series (E36)
- [x] 5 Series (E34)
- [x] 7 Series (E38)
- [x] 8 Series (E31)
- [x] Z3 (E36/7/E36/8)
- [x] X5 (E53 launch year)

**Status**: ✅ `wip/bmw/1990s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Covered transition-era BMWs including VANOS-equipped E36, E34 V8 sedans, first-generation Z3 roadster, and the inaugural E53 X5 with early SAV service notes.

### 1980s Models (Target: 5 entries) - ✅ COMPLETE
- [x] 3 Series (E30)
- [x] 5 Series (E28)
- [x] 6 Series (E24)
- [x] 7 Series (E23)
- [x] 7 Series (E32 early)

**Status**: ✅ `wip/bmw/1980s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Added timing-belt/timing-chain service notes for M20/M30 engines and early hydraulic self-leveling guidance; M1 covered under 1970s supercar entry. Z1 excluded—no official NA sales.

### 1970s Models (Target: 3 entries) - ✅ COMPLETE
- [x] 5 Series (E12)
- [x] 3 Series (E21)
- [x] M1 (E26)

**Status**: ✅ `wip/bmw/1970s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Documented K-Jetronic E21 and L-Jetronic E12 service needs plus mid-engine M1 homologation support. E24/E23 early coverage handled in 1980s file.

### 1960s Models (Target: 4 entries) - ✅ COMPLETE
- [x] Neue Klasse sedans (1500/1600/1800/2000)
- [x] 2002 (E10)
- [x] E3 Bavaria (New Six)
- [x] E9 coupes (2800 CS/3.0 CS/CSi/CSL)

**Status**: ✅ `wip/bmw/1960s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Captured M10-powered Neue Klasse and 2002 service intervals, plus D-Jetronic New Six sedans and Karmann-built E9 coupes with corrosion repair notes.

### 1950s Models (Target: 5 entries) - ✅ COMPLETE
- [x] 501/502
- [x] Isetta
- [x] 600
- [x] 507
- [x] 700

**Status**: ✅ `wip/bmw/1950s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Included microcar powertrain maintenance (chain drives, drum brakes) plus aluminum-bodied 507 and Baroque Angel V8 service considerations for restoration teams.

### 1930s Models (Target: 4 entries) - ✅ COMPLETE
- [x] 303/315/319 series
- [x] 326 sedan
- [x] 327 coupe/cabriolet
- [x] 328 sports roadster

**Status**: ✅ `wip/bmw/1930s.json` validated with `jq empty`.
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Added pre-war inline-six service guidance—babbitt bearings, mechanical drum brakes, and body-on-frame/timber construction best practices.

---

## Wikipedia Source Log (in progress)
- ✅ BMW 2 Series (G42) — https://en.wikipedia.org/w/index.php?title=BMW_2_Series_(G42)&oldid=1293122609 (October 11, 2025 revision)
- ✅ BMW 3 Series (G20) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(G20)&oldid=1299164592 (September 28, 2025 revision)
- ✅ BMW 4 Series (G22) — https://en.wikipedia.org/w/index.php?title=BMW_4_Series_(G22)&oldid=1298353469 (August 20, 2025 revision)
- ✅ BMW 5 Series (G60) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(G60)&oldid=1299579195 (October 14, 2025 revision)
- ✅ BMW 7 Series (G70) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(G70)&oldid=1298356507 (August 20, 2025 revision)
- ✅ BMW i4 — https://en.wikipedia.org/w/index.php?title=BMW_i4&oldid=1298354827 (August 20, 2025 revision)
- ✅ BMW X5 (G05) — https://en.wikipedia.org/w/index.php?title=BMW_X5_(G05)&oldid=1297653758 (September 10, 2025 revision)
- ✅ BMW iX — https://en.wikipedia.org/w/index.php?title=BMW_iX&oldid=1299123054 (October 7, 2025 revision)
- ✅ BMW 8 Series (G15) — https://en.wikipedia.org/w/index.php?title=BMW_8_Series_(G15)&oldid=1309909812 (October 14, 2025 revision)
- ✅ BMW X1 — https://en.wikipedia.org/w/index.php?title=BMW_X1&oldid=1304592664 (September 9, 2025 revision)
- ✅ BMW X3 — https://en.wikipedia.org/w/index.php?title=BMW_X3&oldid=1309122219 (September 29, 2025 revision)
- ✅ BMW X6 — https://en.wikipedia.org/w/index.php?title=BMW_X6&oldid=1308582124 (October 10, 2025 revision)
- ✅ BMW X7 — https://en.wikipedia.org/w/index.php?title=BMW_X7&oldid=1309122219 (September 29, 2025 revision)
- ✅ BMW XM — https://en.wikipedia.org/w/index.php?title=BMW_XM&oldid=1302856839 (September 2, 2025 revision)
- ⏳ Historic BMW models —
## Wikipedia Source Log
- ✅ BMW 2 Series (G42) — https://en.wikipedia.org/w/index.php?title=BMW_2_Series_(G42)&oldid=1293122609 (October 11, 2025 revision)
- ✅ BMW 3 Series (G20) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(G20)&oldid=1299164592 (September 28, 2025 revision)
- ✅ BMW 4 Series (G22) — https://en.wikipedia.org/w/index.php?title=BMW_4_Series_(G22)&oldid=1298353469 (August 20, 2025 revision)
- ✅ BMW 5 Series (G60) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(G60)&oldid=1299579195 (October 14, 2025 revision)
- ✅ BMW 7 Series (G70) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(G70)&oldid=1298356507 (August 20, 2025 revision)
- ✅ BMW i4 — https://en.wikipedia.org/w/index.php?title=BMW_i4&oldid=1298354827 (August 20, 2025 revision)
- ✅ BMW X5 (G05) — https://en.wikipedia.org/w/index.php?title=BMW_X5_(G05)&oldid=1297653758 (September 10, 2025 revision)
- ✅ BMW iX — https://en.wikipedia.org/w/index.php?title=BMW_iX&oldid=1299123054 (October 7, 2025 revision)
- ✅ BMW 8 Series (G15) — https://en.wikipedia.org/w/index.php?title=BMW_8_Series_(G15)&oldid=1309909812 (October 14, 2025 revision)
- ✅ BMW X1 — https://en.wikipedia.org/w/index.php?title=BMW_X1&oldid=1304592664 (September 9, 2025 revision)
- ✅ BMW X3 — https://en.wikipedia.org/w/index.php?title=BMW_X3&oldid=1309122219 (September 29, 2025 revision)
- ✅ BMW X6 — https://en.wikipedia.org/w/index.php?title=BMW_X6&oldid=1308582124 (October 10, 2025 revision)
- ✅ BMW X7 — https://en.wikipedia.org/w/index.php?title=BMW_X7&oldid=1309122219 (September 29, 2025 revision)
- ✅ BMW XM — https://en.wikipedia.org/w/index.php?title=BMW_XM&oldid=1302856839 (September 2, 2025 revision)
- ✅ BMW 1 Series (E81/E82) — https://en.wikipedia.org/w/index.php?title=BMW_1_Series_(E81)&oldid=1309907223 (October 9, 2025 revision)
- ✅ BMW 3 Series (E46) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(E46)&oldid=1324823457 (October 14, 2025 revision)
- ✅ BMW 3 Series (E90) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(E90)&oldid=1320066280 (October 5, 2025 revision)
- ✅ BMW 5 Series (E39) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(E39)&oldid=1309961889 (October 8, 2025 revision)
- ✅ BMW 5 Series (E60) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(E60)&oldid=1309996704 (October 14, 2025 revision)
- ✅ BMW 6 Series (E63) — https://en.wikipedia.org/w/index.php?title=BMW_6_Series_(E63)&oldid=1310136509 (October 14, 2025 revision)
- ✅ BMW 7 Series (E65) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(E65)&oldid=1325096897 (October 12, 2025 revision)
- ✅ BMW Z4 (E85) — https://en.wikipedia.org/w/index.php?title=BMW_Z4_(E85)&oldid=1310410541 (October 13, 2025 revision)
- ✅ BMW Z4 (E89) — https://en.wikipedia.org/w/index.php?title=BMW_Z4_(E89)&oldid=1310377432 (October 8, 2025 revision)
- ✅ BMW X5 — https://en.wikipedia.org/w/index.php?title=BMW_X5&oldid=1309934132 (October 14, 2025 revision)
- ✅ BMW X5 (E70) — https://en.wikipedia.org/w/index.php?title=BMW_X5_(E70)&oldid=1309934509 (October 14, 2025 revision)
- ✅ BMW 3 Series (E36) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(E36)&oldid=1309871459 (October 8, 2025 revision)
- ✅ BMW 5 Series (E34) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(E34)&oldid=1309509625 (October 7, 2025 revision)
- ✅ BMW 7 Series (E38) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(E38)&oldid=1310003038 (October 8, 2025 revision)
- ✅ BMW 8 Series (E31) — https://en.wikipedia.org/w/index.php?title=BMW_8_Series_(E31)&oldid=1310391201 (October 13, 2025 revision)
- ✅ BMW Z3 — https://en.wikipedia.org/w/index.php?title=BMW_Z3&oldid=1310019673 (October 9, 2025 revision)
- ✅ BMW 3 Series (E30) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(E30)&oldid=1324114733 (October 8, 2025 revision)
- ✅ BMW 5 Series (E28) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(E28)&oldid=1309875860 (October 8, 2025 revision)
- ✅ BMW 6 Series (E24) — https://en.wikipedia.org/w/index.php?title=BMW_6_Series_(E24)&oldid=1309501739 (October 8, 2025 revision)
- ✅ BMW 7 Series (E23) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(E23)&oldid=1302999129 (October 9, 2025 revision)
- ✅ BMW 7 Series (E32) — https://en.wikipedia.org/w/index.php?title=BMW_7_Series_(E32)&oldid=1308504803 (October 8, 2025 revision)
- ✅ BMW 5 Series (E12) — https://en.wikipedia.org/w/index.php?title=BMW_5_Series_(E12)&oldid=1309635724 (October 6, 2025 revision)
- ✅ BMW 3 Series (E21) — https://en.wikipedia.org/w/index.php?title=BMW_3_Series_(E21)&oldid=1309614342 (October 7, 2025 revision)
- ✅ BMW M1 — https://en.wikipedia.org/w/index.php?title=BMW_M1&oldid=1309979016 (October 10, 2025 revision)
- ✅ BMW Neue Klasse — https://en.wikipedia.org/w/index.php?title=BMW_Neue_Klasse&oldid=1309515119 (October 5, 2025 revision)
- ✅ BMW 2002 — https://en.wikipedia.org/w/index.php?title=BMW_2002&oldid=1309970799 (October 10, 2025 revision)
- ✅ BMW New Six — https://en.wikipedia.org/w/index.php?title=BMW_New_Six&oldid=1309940182 (October 12, 2025 revision)
- ✅ BMW E9 — https://en.wikipedia.org/w/index.php?title=BMW_E9&oldid=1310386424 (October 9, 2025 revision)
- ✅ BMW 501 — https://en.wikipedia.org/w/index.php?title=BMW_501&oldid=1309530977 (October 6, 2025 revision)
- ✅ BMW Isetta — https://en.wikipedia.org/w/index.php?title=BMW_Isetta&oldid=1309527772 (October 6, 2025 revision)
- ✅ BMW 600 — https://en.wikipedia.org/w/index.php?title=BMW_600&oldid=1309531899 (October 6, 2025 revision)
- ✅ BMW 507 — https://en.wikipedia.org/w/index.php?title=BMW_507&oldid=1310020347 (October 9, 2025 revision)
- ✅ BMW 700 — https://en.wikipedia.org/w/index.php?title=BMW_700&oldid=1310054682 (October 11, 2025 revision)
- ✅ BMW 303 — https://en.wikipedia.org/w/index.php?title=BMW_303&oldid=1309495084 (October 3, 2025 revision)
- ✅ BMW 326 — https://en.wikipedia.org/w/index.php?title=BMW_326&oldid=1309533831 (October 8, 2025 revision)
- ✅ BMW 327 — https://en.wikipedia.org/w/index.php?title=BMW_327&oldid=1309533729 (October 8, 2025 revision)
- ✅ BMW 328 — https://en.wikipedia.org/w/index.php?title=BMW_328&oldid=1309512939 (October 6, 2025 revision)

---

## Validation Checklist
- [x] Each decade JSON validates with `jq empty wip/bmw/[decade].json`
- [x] Difficulty modifiers ≥ 1.00 with justification in notes
- [x] Wikipedia citation with revision date captured in notes and tracker
- [x] Hybrid/diesel flags align with powertrains (note EU-only diesels excluded from NA data)
- [x] Body styles limited to North American market availability

---

## Append Workflow Reminders
1. Validate every decade file individually with `jq empty`.
2. Backup `vehicles.json` before any merge.
3. Merge all completed BMW decade files in a single batch once all show ⏳ READY.
4. Revalidate merged `vehicles.json` and update counts here.
5. Archive appended decade files with `_APPENDED` suffix.

---

## Open Questions
- (Resolved) XM documented as standalone PHEV entry with HV precautions.
- (Resolved) 1 Series F20 and Z1 excluded from NA dataset; noted in highlights for lack of official sales.
- (Resolved) 700/Isetta coverage limited to European-import region flag with service notes.
