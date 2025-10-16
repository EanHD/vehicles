# Toyota Research Progress Tracker

**Last Updated**: January 17, 2025
**Strategy**: Focus on North American market models (1960s-2020s)
**Current vehicles.json count**: 2 Toyota entries (Camry XV40, RAV4 XA50)
**Status**: Starting comprehensive North American audit

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | TBD    | 🔄 IN PROGRESS | `2020s.json` | ❌ |
| 2010s  | TBD    | ⏳ TODO | `2010s.json` | ❌ |
| 2000s  | TBD    | ⏳ TODO | `2000s.json` | ❌ |
| 1990s  | TBD    | ⏳ TODO | `1990s.json` | ❌ |
| 1980s  | TBD    | ⏳ TODO | `1980s.json` | ❌ |
| 1970s  | TBD    | ⏳ TODO | `1970s.json` | ❌ |
| 1960s  | TBD    | ⏳ TODO | `1960s.json` | ❌ |
| **Toyota Total** | **TBD** | **IN PROGRESS** | - | ❌ |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE

---

## Strategy: North American Focus

**Toyota is MASSIVE globally, so focusing on:**
- Models sold in North American market
- High-volume sellers (Camry, Corolla, RAV4, Tacoma, Tundra)
- Iconic models (Supra, Land Cruiser, 4Runner)
- Hybrid pioneers (Prius)
- Key generations only (not every single year)

**Skipping:**
- Japan/Asia-only models (Century, Allion, Alphard)
- Small kei cars (Pixis, Roomy)
- Regional variants not sold in NA

---

## High Priority North American Models

### 2020s Models - 🔄 IN PROGRESS
- [ ] Camry XV80 (2025+, hybrid-only)
- [ ] Corolla (2020s updates)
- [ ] Corolla Cross (2022+)
- [ ] Crown (2023+)
- [ ] RAV4 (already have XA50, check completeness)
- [ ] RAV4 Prime PHEV (2021+)
- [ ] Highlander XU70 (2020+)
- [ ] Grand Highlander (2024+)
- [ ] Sienna XL40 (2021+, hybrid-only)
- [ ] Sequoia XK80 (2023+)
- [ ] Tacoma N400 (2024+)
- [ ] Tundra XK70 (2022+)
- [ ] Land Cruiser J250 (2024+)
- [ ] bZ4X (2023+, EV)
- [ ] GR Supra A90 (2020+)
- [ ] GR86 (2022+)
- [ ] Prius XW60 (2023+)

### 2010s Models - ⏳ TODO
- [ ] Camry XV50/XV70
- [ ] Corolla E160/E210
- [ ] Avalon XX50
- [ ] Prius generations
- [ ] RAV4 XA40 (check if exists)
- [ ] Highlander XU50
- [ ] 4Runner N280
- [ ] Tacoma N300
- [ ] Tundra XK50
- [ ] Sienna XL30
- [ ] FJ Cruiser
- [ ] Mirai
- [ ] 86/GR86 (first gen)

### 2000s Models - ⏳ TODO
- [ ] Camry XV30 (check if exists)
- [ ] Corolla E120/E140
- [ ] Yaris/Echo
- [ ] Matrix
- [ ] Avalon
- [ ] Prius generations
- [ ] RAV4 generations
- [ ] Highlander XU20/XU40
- [ ] 4Runner N210
- [ ] Tacoma N220
- [ ] Tundra XK30/XK50
- [ ] Sequoia XK30/XK60
- [ ] FJ Cruiser
- [ ] Land Cruiser 100/200

### Earlier Decades
Will research key models from 1960s-1990s after modern coverage

---

## Notes

- Toyota founded 1937 in Japan
- Entered US market 1957
- Known for reliability and hybrid technology
- Prius pioneered mass-market hybrids (1997)
- Best-selling brand globally
- Focus on practical, reliable vehicles

---

## Quick Commands

```bash
# Validate decade file
jq empty wip/toyota/2020s.json

# Count entries
grep -c '"make": "Toyota"' vehicles.json
```
