#!/usr/bin/env python3
"""
torque_spec_finder.py - Research torque specifications for vehicle components
Swoop Service Auto - Quick Torque Spec Lookup

Usage:
    python torque_spec_finder.py <year> <make> <model> <component>
    
Example:
    python torque_spec_finder.py 2020 Ford "F-150" "cylinder head"
    python torque_spec_finder.py 2018 Honda Civic "wheel lug nuts"
"""

import os
import json
import sys
from pathlib import Path

# Add tools directory to path for ai_client import
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
from ai_client import AIClient


class TorqueSpecFinder:
    """Research and retrieve torque specifications using AI"""
    
    def __init__(self):
        self.client = AIClient(purpose="research")
    
    def find_torque_specs(self, year, make, model, component):
        """Research torque specifications for specific component"""
        
        prompt = f"""You are an expert automotive technician with access to factory service manuals. 
Find torque specifications for the following:

Vehicle: {year} {make} {model}
Component: {component}

Please provide comprehensive torque specifications in JSON format:

{{
  "vehicle": {{
    "year": {year},
    "make": "{make}",
    "model": "{model}",
    "component": "{component}"
  }},
  "torque_specifications": [
    {{
      "fastener": "Fastener name/description",
      "torque_imperial": "XX ft-lbs",
      "torque_metric": "YY Nm",
      "thread_size": "M10x1.5 or 1/2-20 UNF",
      "tightening_notes": "Clean threads, apply threadlocker, etc.",
      "warnings": ["Warning if applicable"]
    }}
  ],
  "tightening_sequence": {{
    "pattern": "Description of pattern (star, spiral, inside-out, etc.)",
    "steps": [
      "Step 1: Torque all bolts to XX ft-lbs",
      "Step 2: Torque to final spec YY ft-lbs",
      "Step 3: Additional turn method if applicable"
    ],
    "diagram_notes": "Visual pattern description (e.g., 1-3-5-2-4-6)"
  }},
  "special_requirements": {{
    "threadlocker": "Blue (medium) or Red (permanent) or None",
    "thread_sealant": "Required or Not required",
    "lubrication": "Clean/dry or Oil threads or Anti-seize",
    "torque_angle": "Torque-to-yield specification if applicable",
    "special_tools": ["Special tools needed"]
  }},
  "common_issues": [
    {{
      "problem": "Description of common problem",
      "cause": "Why it happens",
      "prevention": "How to avoid it"
    }}
  ],
  "research_sources": [
    "Factory service manual specification",
    "Trusted automotive source"
  ],
  "confidence": "High/Medium/Low"
}}

**CRITICAL REQUIREMENTS:**
1. Provide EXACT torque values from factory specifications
2. Include BOTH imperial (ft-lbs) and metric (Nm) measurements
3. Specify tightening sequence for multi-bolt components (heads, oil pan, etc.)
4. Note any torque-to-yield bolts (must be replaced)
5. Indicate if threadlocker, sealant, or lubrication is required
6. Include thread size where relevant
7. Warn about aluminum vs. steel threads
8. Note any special tightening procedures (angle torque, etc.)

**Research Guidelines:**
- Prioritize factory service manual specifications
- If multiple engine options exist, specify which engine
- Include model year range where specs are valid
- Note if specs changed between generations
- Cite sources for verification

Output ONLY valid JSON."""

        print(f"🔍 Researching torque specs for {year} {make} {model} - {component}...")
        print(f"   Using {self.client.provider} ({self.client.model})")
        
        system_message = "You are an expert automotive technician. Always provide accurate, specific torque specifications with citations."
        
        response = self.client.chat(prompt, system_message=system_message)
        
        return response
    
    def parse_and_display(self, response_text):
        """Parse JSON response and display in readable format"""
        # Try to parse JSON using AI client helper
        data = self.client.extract_json(response_text)
        
        if not data:
            print(f"\n⚠️  Could not parse JSON response")
            print("\nRaw response:")
            print("="*80)
            print(response_text)
            print("="*80)
            return None
            # Display formatted output
            print("\n" + "="*80)
            print("🔩 TORQUE SPECIFICATIONS")
            print("="*80)
            
            # Vehicle info
            if 'vehicle' in data:
                v = data['vehicle']
                print(f"\n🚗 VEHICLE: {v['year']} {v['make']} {v['model']}")
                print(f"📍 COMPONENT: {v['component']}")
            
            # Torque specs
            if 'torque_specifications' in data:
                print(f"\n⚙️  TORQUE VALUES:")
                for spec in data['torque_specifications']:
                    print(f"\n   {spec['fastener']}:")
                    print(f"      Imperial: {spec.get('torque_imperial', 'N/A')}")
                    print(f"      Metric:   {spec.get('torque_metric', 'N/A')}")
                    if 'thread_size' in spec:
                        print(f"      Thread:   {spec['thread_size']}")
                    if 'tightening_notes' in spec:
                        print(f"      Notes:    {spec['tightening_notes']}")
                    if 'warnings' in spec and spec['warnings']:
                        print(f"      ⚠️  {', '.join(spec['warnings'])}")
            
            # Tightening sequence
            if 'tightening_sequence' in data:
                seq = data['tightening_sequence']
                print(f"\n🔄 TIGHTENING SEQUENCE:")
                if 'pattern' in seq:
                    print(f"   Pattern: {seq['pattern']}")
                if 'diagram_notes' in seq:
                    print(f"   Diagram: {seq['diagram_notes']}")
                if 'steps' in seq:
                    print(f"   Steps:")
                    for step in seq['steps']:
                        print(f"      • {step}")
            
            # Special requirements
            if 'special_requirements' in data:
                req = data['special_requirements']
                print(f"\n🛠️  SPECIAL REQUIREMENTS:")
                if req.get('threadlocker'):
                    print(f"   Threadlocker: {req['threadlocker']}")
                if req.get('thread_sealant'):
                    print(f"   Thread Sealant: {req['thread_sealant']}")
                if req.get('lubrication'):
                    print(f"   Lubrication: {req['lubrication']}")
                if req.get('torque_angle'):
                    print(f"   Torque-to-Yield: {req['torque_angle']}")
                if req.get('special_tools'):
                    print(f"   Special Tools: {', '.join(req['special_tools'])}")
            
            # Common issues
            if 'common_issues' in data and data['common_issues']:
                print(f"\n⚠️  COMMON ISSUES:")
                for issue in data['common_issues']:
                    print(f"\n   Problem: {issue['problem']}")
                    print(f"   Cause: {issue['cause']}")
                    print(f"   Prevention: {issue['prevention']}")
            
            # Sources and confidence
            if 'research_sources' in data:
                print(f"\n📚 SOURCES:")
                for source in data['research_sources']:
                    print(f"   • {source}")
            
            if 'confidence' in data:
                print(f"\n✅ CONFIDENCE LEVEL: {data['confidence']}")
            
            print("\n" + "="*80 + "\n")
            
            return data


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 5:
        print("="*80)
        print("TORQUE SPECIFICATION FINDER")
        print("Swoop Service Auto - Quick Torque Spec Lookup")
        print("="*80)
        print("\nUsage:")
        print("  python torque_spec_finder.py <year> <make> <model> <component>")
        print("\nExamples:")
        print('  python torque_spec_finder.py 2020 Ford "F-150" "cylinder head"')
        print('  python torque_spec_finder.py 2018 Honda Civic "wheel lug nuts"')
        print('  python torque_spec_finder.py 2022 Toyota Camry "oil drain plug"')
        print('  python torque_spec_finder.py 2019 Chevrolet Silverado "intake manifold"')
        print("\nCommon Components:")
        print("  • cylinder head       • intake manifold      • exhaust manifold")
        print("  • oil pan             • valve cover          • timing cover")
        print("  • wheel lug nuts      • caliper bolts        • suspension bolts")
        print("  • spark plugs         • oil drain plug       • transmission pan")
        print("\nConfiguration:")
        print("  Configure AI provider in .env file (RESEARCH_AI_PROVIDER)")
        print("\n" + "="*80)
        sys.exit(1)
    
    year = int(sys.argv[1])
    make = sys.argv[2]
    model = sys.argv[3]
    component = sys.argv[4]
    
    try:
        finder = TorqueSpecFinder()
        response = finder.find_torque_specs(year, make, model, component)
        data = finder.parse_and_display(response)
        
        # Save to JSON if requested
        if '--save' in sys.argv and data:
            filename = f"torque_specs_{make}_{model}_{year}_{component}.json".lower().replace(' ', '_')
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Saved to: {filename}")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")
        sys.exit(1)
