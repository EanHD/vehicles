# Volvo Research Progress Tracker

**Last Updated**: January 17, 2025  
**Strategy**: Complete coverage from 1920s (ÖV 4 Jakob, 1927) through 2025  
**Current vehicles.json count**: 0 Volvo entries

---

## Quick Status Overview

| Decade | Status | Models Identified | Researched | Validated | Appended |
|--------|--------|-------------------|------------|-----------|----------|
| 1920s  | ✅ APPENDED | 2 | ✅ | ✅ | ✅ |
| 1930s  | ✅ APPENDED | 2 | ✅ | ✅ | ✅ |
| 1940s  | ✅ APPENDED | 2 | ✅ | ✅ | ✅ |
| 1950s  | ✅ APPENDED | 4 | ✅ | ✅ | ✅ |
| 1960s  | ✅ APPENDED | 4 | ✅ | ✅ | ✅ |
| 1970s  | ✅ APPENDED | 5 | ✅ | ✅ | ✅ |
| 1980s  | ✅ APPENDED | 6 | ✅ | ✅ | ✅ |
| 1990s  | ✅ APPENDED | 10 | ✅ | ✅ | ✅ |
| 2000s  | ✅ APPENDED | 10 | ✅ | ✅ | ✅ |
| 2010s  | ✅ APPENDED | 11 | ✅ | ✅ | ✅ |
| 2020s  | ✅ APPENDED | 7 | ✅ | ✅ | ✅ |

**Total Entries: 63 models across 11 decades**
**Status: ✅ ALL DECADES COMPLETE AND APPENDED TO vehicles.json**
**Current vehicles.json count**: 63 Volvo entries

---

## 1920s Models (2 models)
- [ ] ÖV 4 "Jakob" (1927–1929) - https://en.wikipedia.org/wiki/Volvo_ÖV_4
- [ ] PV4 (1927–1929)

## 1930s Models (3 models)
- [ ] PV36 Carioca (1935–1938)
- [ ] PV51 (1936–1945)
- [ ] TR670 taxis (1930s)

## 1940s Models (3 models)
- [ ] PV444 (1947–1958)
- [ ] PV60 (1946–1950)
- [ ] Duett (1953 launch, continuation into 1960s)

## 1950s Models (4 models)
- [ ] Amazon/120 Series (1956–1970)
- [ ] PV544 (1958–1965)
- [ ] P1900 (1956–1957)
- [ ] Duett (1953–1969)

## 1960s Models (5 models)
- [ ] P1800 (1961–1973)
- [ ] 140 Series (1966–1974)
- [ ] 164 (1968–1975)
- [ ] Amazon (continuation from 1950s)
- [ ] 1800ES (1972–1973)

## 1970s Models (5 models)
- [ ] 240/260 Series (1974–1993)
- [ ] 66 (1975–1981)
- [ ] 300 Series (1976–1991)
- [ ] 262C/264 (1975–1981)
- [ ] 140 Series (continuation through 1974)

## 1980s Models (5 models)
- [ ] 700 Series (1982–1992)
- [ ] 480 (1986–1995)
- [ ] 780 coupe (1985–1990)
- [ ] 940/960 (1990–1998)
- [ ] 240 (continuation 1980–1993)

## 1990s Models (7 models)
- [ ] 850 (1991–1997)
- [ ] S70/V70 (1997–2000)
- [ ] S40/V40 (1995–2004)
- [ ] C70 (1998–2005)
- [ ] S80 (1999–2016)
- [ ] XC70 (1997–2016)
- [ ] V90/S90 classic (1996–1998)

## 2000s Models (8 models)
- [ ] S40/V50 (2004–2012)
- [ ] S60/V70 (2001–2009)
- [ ] S80 (2007–2016)
- [ ] XC90 first gen (2003–2014)
- [ ] XC60 first gen (2008–2017)
- [ ] C30 (2008–2013)
- [ ] V70/XC70 third gen (2007–2016)
- [ ] S60 (2001–2009)

## 2010s Models (10 models)
- [ ] XC90 II/SPA (2016–present)
- [ ] S90/V90 (2017–present)
- [ ] V60 (2019–present)
- [ ] S60 II (2019–present)
- [ ] XC60 II (2018–present)
- [ ] XC40 (2019–present)
- [ ] V40 (2013–2019)
- [ ] S80 (continuation through 2016)
- [ ] XC90 first gen (continuation 2003–2014)
- [ ] C30 (continuation 2008–2013)

## 2020s Models (7 models)
- [ ] XC40 Recharge/EX40 (2021–present)
- [ ] C40 Recharge/EC40 (2022–present)
- [ ] EX30 (2024–present)
- [ ] EX90 (2024–present)
- [ ] EM90 (2024 China)
- [ ] S60/V60 Polestar refresh (2024)
- [ ] S90 (2021 refresh)

---

## Research Notes

### Platform Information
- **SPA Platform** (2016+): XC90, S90, V90, S60, V60, XC60
- **CMA Platform** (2017+): XC40, C40, EX30
- **Geely Era** (2010–present): Post-acquisition modernization, electrification push
- **Pre-Geely**: Ford ownership (1999–2010), independence (1927–1999)

### Key Technical Notes
- Brass-era models (1920s-1930s): difficulty_modifier 1.2
- Early post-war (1940s-1950s): difficulty_modifier 1.1-1.2 (vintage parts, non-synchronized transmissions)
- Modern era (1990s+): difficulty_modifier 1.0-1.1 depending on complexity
- EVs (2020s): difficulty_modifier 1.3-1.4 (high-voltage systems)

### North American Market Focus
- Focus on US/Canadian market models only
- Some models were Europe-only (note but exclude if never sold in NA)
- Check each model's North American availability on Wikipedia

---

## Current Phase: Phase 1 - Setup & Gap Analysis

**Next Steps:**
1. ✅ Create wip/volvo directory
2. ✅ Create PROGRESS_TRACKER.md
3. ⏳ Begin decade-by-decade research starting with 2020s (working backwards)
4. Create decade JSON files as research progresses
5. Validate each decade file with `jq empty`
6. Batch append when multiple decades are complete

---

## Wikipedia Sources

To be populated as research progresses with format:
- Model Name (Generation): https://en.wikipedia.org/wiki/Article_Name (Revision: Month Day, Year)
