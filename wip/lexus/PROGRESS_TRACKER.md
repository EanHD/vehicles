# Lexus Research Progress Tracker

**Last Updated**: January 17, 2025
**Strategy**: Complete coverage from brand inception (1989) through 2025
**Current vehicles.json count**: 0 Lexus entries

---

## Quick Status Overview

| Decade | Models | Status | JSON File | Appended |
|--------|--------|--------|-----------|----------|
| 2020s  | TBD    | ⏳ TODO | `2020s.json` | ❌ |
| 2010s  | TBD    | ⏳ TODO | `2010s.json` | ❌ |
| 2000s  | TBD    | ⏳ TODO | `2000s.json` | ❌ |
| 1990s  | TBD    | ⏳ TODO | `1990s.json` | ❌ |
| **Total** | **TBD** | **0/TBD** | - | ❌ |

**Legend**: ⏳ TODO | 🔄 IN PROGRESS | ✅ DONE | ⚠️ NEEDS REVIEW

---

## Lexus Brand Overview

- **Founded**: 1989 (Toyota's luxury division)
- **First Model**: LS 400 (1989)
- **Market Position**: Premium/luxury brand competing with Mercedes, BMW, Audi
- **Key Models**: LS (flagship sedan), RX (luxury crossover), ES (mid-size sedan), IS (compact sport sedan), GX/LX (luxury SUVs)

---

## High Priority Models

1. **RX** - Best-selling luxury crossover, multiple generations
2. **ES** - Popular luxury sedan
3. **LS** - Flagship luxury sedan
4. **NX** - Compact luxury crossover
5. **IS** - Sport sedan
6. **GX/LX** - Body-on-frame luxury SUVs

---

## Notes

- **Hybrid Availability**: Lexus is a hybrid pioneer (RX 400h in 2005)
- **Regional Differences**: Some models Japan/Asia only
- **Platform Sharing**: Many share Toyota platforms (ES/Camry, RX/Highlander, etc.)
- **Performance**: F Sport and F variants available on many models
- **North American Focus**: Only include models sold in NA market

---

## Quick Commands

```bash
# Check current progress
cat wip/lexus/PROGRESS_TRACKER.md | grep "Status:"

# Validate a decade file
jq empty wip/lexus/2020s.json

# Count Lexus entries in vehicles.json
grep -c '"make": "Lexus"' vehicles.json
```
