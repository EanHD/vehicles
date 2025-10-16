# Genesis Research Progress Tracker

**Last Updated**: October 15, 2025
**Strategy**: Start with active Genesis brand lineup (2020s), then backfill 2010s launch models and 2000s precursor programs
**Current vehicles.json count**: 11 Genesis entries (verified via `grep -c \"make\": \"Genesis\"` on October 15, 2025 after append)

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | 5      | ✅ 5/5 | `2020s_APPENDED.json` ✅ | ✅ APPENDED |
| 2010s  | 4      | ✅ 4/4 | `2010s_APPENDED.json` ✅ | ✅ APPENDED |
| 2000s  | 2      | ✅ 2/2 | `2000s_APPENDED.json` ✅ | ✅ APPENDED |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | 🔜 LATER | ⚠️ NEEDS REVIEW

---

## Phase Focus

- **Phase 1**: Document current Genesis brand crossovers and sedans (GV80, GV70, GV60, G80, G90, G70) covering North American engine/driveline offerings.
- **Phase 2**: Capture launch-era Genesis brand transitions (2015-2019) and remaining Hyundai-badged precursor models sold in North America.

---

## Decade Breakdowns

### 2020s Models (Target: 5 entries) - ✅ COMPLETE
- [x] GV80 (JX1, 2021–present NA)
- [x] GV70 (JK1, 2022–present NA)
- [x] GV60 (JW1, 2023–present NA EV)
- [x] G80 (RG3, 2021 refresh onward)
- [x] G90 (RS4, 2023–present NA)

**Status**: ✅ Validated with `jq empty wip/genesis/2020s.json`
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Captured Electrified G80/GV70 high-voltage specs, GV80 Coupe mild-hybrid update, and 2024 OLED interior refresh notes.

---

### 2010s Models (Target: 4 entries) - ✅ COMPLETE
- [x] G70 (IK, 2019–2021 NA launch years)
- [x] G80 (DH/RG3 early launch 2017–2020)
- [x] G90 (HI/RS2 2017–2022 NA)
- [x] Genesis Coupe (BK2 final 2013–2016 NA availability)

**Status**: ✅ Validated with `jq empty wip/genesis/2010s.json`
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Documented manual-transmission G70, DH Sport twin-turbo features, and long-wheelbase G90 service requirements.

---

### 2000s Models (Target: 2 entries) - ✅ COMPLETE
- [x] Hyundai Genesis Sedan (BH, 2009–2014 NA)
- [x] Hyundai Genesis Coupe (BK1, 2010–2012 NA)

**Status**: ✅ Validated with `jq empty wip/genesis/2000s.json`
**Appended**: ✅ Added to vehicles.json on October 15, 2025
**Highlights**: Clarified Hyundai-era branding, ZF/Aisin transmission fluids, and transition to in-house 8-speed.

---

## Wikipedia Source Log
- ✅ Genesis GV80 — https://en.wikipedia.org/w/index.php?title=Genesis_GV80&oldid=1292623392 (May 27, 2025 revision)
- ✅ Genesis GV70 — https://en.wikipedia.org/w/index.php?title=Genesis_GV70&oldid=1296072003 (August 12, 2025 revision)
- ✅ Genesis GV60 — https://en.wikipedia.org/w/index.php?title=Genesis_GV60&oldid=1295239047 (August 6, 2025 revision)
- ✅ Genesis G80 — https://en.wikipedia.org/w/index.php?title=Genesis_G80&oldid=1297765176 (September 22, 2025 revision)
- ✅ Genesis G90 — https://en.wikipedia.org/w/index.php?title=Genesis_G90&oldid=1296939263 (September 13, 2025 revision)
- ✅ Genesis G70 — https://en.wikipedia.org/w/index.php?title=Genesis_G70&oldid=1296351662 (August 28, 2025 revision)
- ✅ Hyundai Genesis Coupe — https://en.wikipedia.org/w/index.php?title=Hyundai_Genesis_Coupe&oldid=1295031940 (August 4, 2025 revision)
- ✅ Hyundai Genesis — https://en.wikipedia.org/w/index.php?title=Hyundai_Genesis&oldid=1294939912 (August 1, 2025 revision)

---

## Validation Checklist
- [x] Each decade JSON validates with `jq empty wip/genesis/[decade].json`
- [x] Difficulty modifiers ≥ 1.00 with justification in notes
- [x] Wikipedia citation with revision date captured in notes and tracker
- [x] Hybrid/diesel flags align with powertrains; EV entries flagged appropriately
- [x] Body styles limited to North American offerings

---

## Append Workflow Reminders
1. Validate every decade file individually with `jq empty`.
2. Backup `vehicles.json` before any merge.
3. Merge all completed decade files in a single batch once all show ⏳ READY.
4. Revalidate merged `vehicles.json` and update counts in this tracker.
5. Archive appended decade files with `_APPENDED` suffix.

---

## Open Questions
- (Resolved Oct 15, 2025) Electrified GV70/G80 captured within respective entries with limited-state availability notes.
- (Resolved Oct 15, 2025) GV60 trims consolidated under single JW1 generation entry for North America.
