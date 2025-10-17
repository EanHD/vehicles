#!/usr/bin/env python3
"""
Test QA function on existing service documents
"""

import re
from pathlib import Path

# Copy audit function from app.py (to avoid streamlit import)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF]")

def audit_html(doc_html: str) -> list[str]:
    """Audit HTML document for quality and completeness"""
    issues = []
    
    # 1) Exactly one <h1>
    h1_count = len(re.findall(r"<h1\b", doc_html, re.I))
    if h1_count != 1:
        issues.append(f"Document must contain exactly one <h1> (found {h1_count}).")
    
    # 2) Required section IDs (anchor targets) - core sections only
    # Note: fluids, variants, and reference-diagrams are optional (only rendered if data exists)
    required_core = ["overview", "safety", "steps", "torque-specifications",
                     "parts", "consumables", "tools", "troubleshooting", "provenance"]
    for sec in required_core:
        if f'id="{sec}"' not in doc_html:
            issues.append(f"Missing required section id='{sec}'.")
    
    # Optional sections - warn if missing but don't fail
    optional = ["fluids", "variants", "reference-diagrams"]
    missing_optional = [sec for sec in optional if f'id="{sec}"' not in doc_html]
    
    # 3) Check for actual emojis (exclude warning symbol ⚠ which is acceptable)
    # Remove warning symbol before checking
    doc_html_no_warning = doc_html.replace("⚠", "").replace("⚡", "").replace("✓", "").replace("✗", "")
    if EMOJI_RE.search(doc_html_no_warning):
        emojis_found = EMOJI_RE.findall(doc_html_no_warning)
        issues.append(f"Emojis detected in document output ({len(emojis_found)} found); remove for professional tone.")
    
    # 4) Torque table present (if section exists)
    if 'id="torque-specifications"' in doc_html:
        # Find the torque section
        parts = doc_html.split('id="torque-specifications"')
        if len(parts) > 1:
            # Get content until next section
            next_section_idx = parts[1].find('<section')
            torque_content = parts[1][:next_section_idx] if next_section_idx > 0 else parts[1]
            if "<table" not in torque_content:
                issues.append("Torque specifications section exists but no table found.")
    
    # 5) Twin-unit spot check (ft-lb/in-lb with metric Nm in parentheses)
    if 'id="torque-specifications"' in doc_html and "<table" in doc_html:
        # Look for torque values with dual units
        twin = re.search(r"\b\d+\s*(ft-?lbs?|in-?lbs?)\s*\(\s*\d+\s*Nm\s*\)", doc_html, re.I)
        if not twin:
            # More lenient check - just look for Nm somewhere in torque section
            parts = doc_html.split('id="torque-specifications"')
            if len(parts) > 1:
                next_section_idx = parts[1].find('<section')
                torque_content = parts[1][:next_section_idx] if next_section_idx > 0 else parts[1]
                if "Nm" not in torque_content and "N·m" not in torque_content:
                    issues.append("Torque values should include metric units (Nm) alongside imperial units.")
    
    # 6) Duplicate IDs
    ids = re.findall(r'id="([^"]+)"', doc_html)
    dups = [i for i in set(ids) if ids.count(i) > 1]
    if dups:
        issues.append("Duplicate element IDs: " + ", ".join(sorted(dups)))
    
    # 7) Print CSS presence (basic check)
    if "@media print" not in doc_html:
        issues.append("Missing @media print rules; print layout may be suboptimal.")
    
    # 8) Info: Optional sections status
    if missing_optional:
        # This is info, not an issue
        pass  # Don't report as issue, these are truly optional
    
    return issues


if __name__ == "__main__":
    service_docs = Path("service_docs")
    
    print("🔍 Testing QA on all cached service documents...\n")
    
    all_docs = list(service_docs.rglob("*.html"))
    
    passed = 0
    failed = 0
    
    for doc_path in sorted(all_docs):
        with open(doc_path, 'r') as f:
            html = f.read()
        
        issues = audit_html(html)
        
        # Get relative path for display
        rel_path = doc_path.relative_to(service_docs)
        
        if issues:
            print(f"❌ {rel_path}")
            for issue in issues:
                print(f"   • {issue}")
            print()
            failed += 1
        else:
            print(f"✅ {rel_path}")
            passed += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {passed} passed, {failed} failed out of {len(all_docs)} total")
    print(f"{'='*60}")
