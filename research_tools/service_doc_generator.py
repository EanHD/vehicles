#!/usr/bin/env python3
"""
service_doc_generator.py - AI-Powered Service Documentation Generator
Swoop Service Auto - Professional Repair Information Database

DEPRECATED: Use /tools/service_doc_generator.py instead
This file is kept for backwards compatibility

Usage:
    python service_doc_generator.py <year> <make> <model> <service_name>
    
Example:
    python service_doc_generator.py 2020 Chevrolet "Silverado 1500" "Brake Pads Replacement (Front)"
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
from ai_client import AIClient


class ServiceDocGenerator:
    """Generate and cache professional service documentation using AI research"""
    
    def __init__(self, vehicles_db=None, services_db=None, cache_dir=None):
        # Get project root (parent of research_tools directory)
        project_root = Path(__file__).parent.parent
        
        # Set default paths relative to project root
        if vehicles_db is None:
            vehicles_db = str(project_root / "data" / "vehicles.json")
        if services_db is None:
            services_db = str(project_root / "data" / "services.json")
        if cache_dir is None:
            cache_dir = str(project_root / "service_docs")
            
        self.vehicles = self.load_json(vehicles_db)
        self.services = self.load_json(services_db)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        
        # Initialize AI client (using research AI)
        self.client = AIClient(purpose="research")
    
    def load_json(self, filepath):
        """Load JSON file"""
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def find_vehicle(self, year, make, model):
        """Find matching vehicle in database"""
        # Try exact match first
        for vehicle in self.vehicles:
            if (year in vehicle['years'] and 
                vehicle['make'].lower() == make.lower() and
                vehicle['model'].lower() == model.lower()):
                return vehicle
        
        # Try partial match (model name might include generation code)
        for vehicle in self.vehicles:
            if (year in vehicle['years'] and 
                vehicle['make'].lower() == make.lower() and
                model.lower() in vehicle['model'].lower()):
                return vehicle
        
        return None
    
    def find_service(self, service_name):
        """Find matching service in catalog"""
        # Try exact match
        for service in self.services:
            if service['name'].lower() == service_name.lower():
                return service
        
        # Try partial match
        for service in self.services:
            if service_name.lower() in service['name'].lower():
                return service
        
        return None
    
    def get_cache_path(self, year, make, model, service_name):
        """Generate cache file path"""
        make_dir = self.cache_dir / make.lower().replace(' ', '_')
        make_dir.mkdir(exist_ok=True)
        
        model_dir = make_dir / f"{model.lower().replace(' ', '_').replace('/', '_')}_{year}"
        model_dir.mkdir(exist_ok=True)
        
        filename = f"{service_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace(',', '')}.json"
        return model_dir / filename
    
    def check_cache(self, year, make, model, service_name):
        """Check if documentation exists in cache"""
        cache_path = self.get_cache_path(year, make, model, service_name)
        if cache_path.exists():
            with open(cache_path, 'r') as f:
                return json.load(f)
        return None
    
    def research_with_ai(self, vehicle, service, context=""):
        """Use Claude to research and generate documentation"""
        
        engines_str = ", ".join(vehicle['engines']) if vehicle['engines'] else 'Unknown'
        transmissions_str = ", ".join(vehicle['transmissions']) if vehicle['transmissions'] else 'Unknown'
        
        prompt = f"""You are an expert automotive technician with decades of experience and access to factory service manuals. Generate comprehensive, professional service documentation for the following:

**Vehicle Information:**
- Year: {vehicle['years'][0]} (production years: {vehicle['years'][0]}-{vehicle['years'][-1]})
- Make: {vehicle['make']}
- Model: {vehicle['model']}
- Engine Options: {engines_str}
- Transmission Options: {transmissions_str}
- Drivetrain: {', '.join(vehicle['drivetrain'])}
- Body Styles: {', '.join(vehicle['body_styles'])}
- Difficulty Modifier: {vehicle['difficulty_modifier']}
- Technical Notes: {vehicle.get('notes', 'N/A')}

**Service Request:**
- Service Name: {service['name']}
- Category: {service['category']}
- Estimated Labor Time: {service['labor_time_hours']} hours
- Mobile Suitable: {service['mobile']}
- Required Parts: {', '.join(service.get('parts_required', []))}
- Service Notes: {service.get('notes', 'N/A')}

{context}

Please generate COMPLETE service documentation in JSON format with the following structure:

{{
  "vehicle": {{
    "year": {vehicle['years'][0]},
    "make": "{vehicle['make']}",
    "model": "{vehicle['model']}",
    "engine": "{vehicle['engines'][0] if vehicle['engines'] else 'Various'}",
    "generation": "Extract from notes or research",
    "difficulty_modifier": {vehicle['difficulty_modifier']}
  }},
  "service": {{
    "name": "{service['name']}",
    "category": "{service['category']}",
    "estimated_time": "{service['labor_time_hours']} hours",
    "difficulty": "Easy/Moderate/Hard",
    "mobile_suitable": {str(service['mobile']).lower()}
  }},
  "procedure": {{
    "preparation": ["Step 1", "Step 2", "..."],
    "steps": [
      {{
        "step": 1,
        "description": "Detailed description",
        "torque_spec": "XX ft-lbs (YY Nm)" or null,
        "tools": ["Tool 1", "Tool 2"],
        "notes": "Important notes",
        "warnings": ["Warning 1"] or null,
        "inspection_points": ["Check 1"] or null
      }}
    ],
    "completion": ["Final step 1", "Final step 2", "..."]
  }},
  "specifications": {{
    "torque_specs": {{"fastener_name": "XX ft-lbs (YY Nm)"}},
    "fluid_specs": {{"fluid_type": "Specification"}},
    "measurements": {{"component": "measurement"}}
  }},
  "parts_list": {{
    "required": [
      {{
        "name": "Part Name",
        "part_numbers": {{
          "oem": "OEM Part Number",
          "aftermarket": ["Aftermarket 1", "Aftermarket 2"]
        }},
        "estimated_cost": "$XX-$YY"
      }}
    ],
    "optional": []
  }},
  "tools_required": {{
    "basic": ["Tool 1", "Tool 2"],
    "specialized": ["Special Tool 1"],
    "optional": ["Optional Tool 1"]
  }},
  "safety_warnings": [
    "⚠️ Critical safety warning 1",
    "⚠️ Critical safety warning 2"
  ],
  "common_issues": [
    {{
      "issue": "Description of common problem",
      "solution": "How to fix it"
    }}
  ],
  "diagnostic_notes": {{
    "symptoms": ["Symptom 1", "Symptom 2"],
    "inspection_points": ["What to check 1", "What to check 2"]
  }}
}}

**CRITICAL REQUIREMENTS:**
1. Provide SPECIFIC torque values with both imperial and metric units
2. Include OEM part numbers where possible (research from vehicle generation)
3. List ALL safety warnings relevant to this procedure
4. Include common failure points and troubleshooting tips
5. Specify fluid types/grades where applicable (DOT 3 vs DOT 4, 5W-30 vs 10W-30, etc.)
6. Include inspection points for wear assessment
7. Note any special tools or equipment needed
8. Provide step-by-step procedure that a mobile mechanic can follow
9. Include diagnostic symptoms that indicate this service is needed

**Research Guidelines:**
- Use factory service manual specifications when available
- Cross-reference automotive forums for common issues on this generation
- Include both OEM and quality aftermarket part options
- Specify any generation-specific quirks or procedures
- Note if procedure differs between engine options
- Include TSB (Technical Service Bulletin) information if relevant

Output ONLY valid JSON. Do not include markdown formatting or explanations outside the JSON structure."""

        print(f"🤖 Sending research request to AI...")
        print(f"   Using {self.client.provider} ({self.client.model})")
        
        system_message = "You are an expert automotive technician. Provide accurate, specific technical information."
        
        response = self.client.chat(prompt, system_message=system_message)
        
        return response
    
    def generate_documentation(self, year, make, model, service_name, force_refresh=False):
        """Generate service documentation (checks cache first)"""
        
        # Check cache unless force refresh
        if not force_refresh:
            cached = self.check_cache(year, make, model, service_name)
            if cached:
                print(f"✅ Found cached documentation for {year} {make} {model} - {service_name}")
                print(f"📁 Cache location: {self.get_cache_path(year, make, model, service_name)}")
                return cached
        
        # Find vehicle and service
        vehicle = self.find_vehicle(year, make, model)
        if not vehicle:
            raise ValueError(f"Vehicle not found in database: {year} {make} {model}\n"
                           f"Hint: Check vehicles.json or try a different model name")
        
        service = self.find_service(service_name)
        if not service:
            raise ValueError(f"Service not found in catalog: {service_name}\n"
                           f"Hint: Check services.json for available services")
        
        print(f"\n{'='*80}")
        print(f"🔍 RESEARCHING SERVICE DOCUMENTATION")
        print(f"{'='*80}")
        print(f"Vehicle: {year} {make} {vehicle['model']}")
        print(f"Service: {service['name']}")
        print(f"Estimated Labor: {service['labor_time_hours']} hours")
        print(f"{'='*80}\n")
        
        # Research with AI
        ai_response = self.research_with_ai(vehicle, service)
        
        # Parse AI response
        try:
            # Try to extract JSON using AI client helper
            doc = self.client.extract_json(ai_response)
            
            if not doc:
                raise ValueError("Could not parse AI response as JSON")
                
        except (json.JSONDecodeError, ValueError) as e:
            print(f"⚠️  Warning: Could not parse AI response as JSON: {e}")
            print(f"Creating structured fallback document...")
            
            # Fallback: structure the raw response
            doc = {
                "vehicle": {
                    "year": year,
                    "make": make,
                    "model": vehicle['model'],
                    "engine": vehicle['engines'][0] if vehicle['engines'] else "Various",
                    "difficulty_modifier": vehicle['difficulty_modifier']
                },
                "service": {
                    "name": service_name,
                    "category": service['category'],
                    "estimated_time": f"{service['labor_time_hours']} hours",
                    "mobile_suitable": service['mobile']
                },
                "raw_research": ai_response,
                "parse_error": str(e),
                "metadata": {
                    "note": "AI response could not be parsed as JSON. Manual formatting may be required."
                }
            }
        
        # Add comprehensive metadata
        if 'metadata' not in doc:
            doc['metadata'] = {}
        
        doc['metadata'].update({
            "generated_date": datetime.utcnow().isoformat() + "Z",
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "generator_version": "1.0.0",
            "ai_model": f"{self.client.provider}:{self.client.model}",
            "vehicle_database_version": f"{len(self.vehicles)} entries",
            "service_catalog_version": f"{len(self.services)} services",
            "confidence_level": "AI-Generated",
            "review_status": "Pending human verification",
            "verified_by": None,
            "verification_date": None
        })
        
        # Save to cache
        cache_path = self.get_cache_path(year, make, model, service_name)
        with open(cache_path, 'w') as f:
            json.dump(doc, f, indent=2)
        
        print(f"\n{'='*80}")
        print(f"✅ DOCUMENTATION GENERATED SUCCESSFULLY")
        print(f"{'='*80}")
        print(f"📁 Cached at: {cache_path}")
        print(f"📊 File size: {cache_path.stat().st_size / 1024:.1f} KB")
        print(f"🔄 Future lookups will be instant (cached)")
        print(f"{'='*80}\n")
        
        return doc


def print_documentation_summary(doc):
    """Print a human-readable summary of the documentation"""
    print("\n" + "="*80)
    print("📋 SERVICE DOCUMENTATION SUMMARY")
    print("="*80)
    
    # Vehicle info
    if 'vehicle' in doc:
        v = doc['vehicle']
        print(f"\n🚗 VEHICLE:")
        print(f"   {v.get('year', 'N/A')} {v.get('make', 'N/A')} {v.get('model', 'N/A')}")
        print(f"   Engine: {v.get('engine', 'N/A')}")
        if 'generation' in v:
            print(f"   Generation: {v['generation']}")
        print(f"   Difficulty: {v.get('difficulty_modifier', 'N/A')}")
    
    # Service info
    if 'service' in doc:
        s = doc['service']
        print(f"\n🔧 SERVICE:")
        print(f"   Name: {s.get('name', 'N/A')}")
        print(f"   Category: {s.get('category', 'N/A')}")
        print(f"   Estimated Time: {s.get('estimated_time', 'N/A')}")
        print(f"   Difficulty: {s.get('difficulty', 'N/A')}")
        print(f"   Mobile Suitable: {'Yes' if s.get('mobile_suitable') else 'No'}")
    
    # Procedure steps count
    if 'procedure' in doc and 'steps' in doc['procedure']:
        print(f"\n📝 PROCEDURE:")
        print(f"   Preparation steps: {len(doc['procedure'].get('preparation', []))}")
        print(f"   Main steps: {len(doc['procedure']['steps'])}")
        print(f"   Completion steps: {len(doc['procedure'].get('completion', []))}")
    
    # Torque specs count
    if 'specifications' in doc and 'torque_specs' in doc['specifications']:
        print(f"\n🔩 TORQUE SPECIFICATIONS:")
        for name, spec in doc['specifications']['torque_specs'].items():
            print(f"   {name}: {spec}")
    
    # Required tools
    if 'tools_required' in doc:
        t = doc['tools_required']
        total_tools = len(t.get('basic', [])) + len(t.get('specialized', []))
        print(f"\n🛠️  TOOLS REQUIRED:")
        print(f"   Basic tools: {len(t.get('basic', []))}")
        print(f"   Specialized tools: {len(t.get('specialized', []))}")
    
    # Parts count
    if 'parts_list' in doc:
        p = doc['parts_list']
        print(f"\n🔩 PARTS LIST:")
        print(f"   Required parts: {len(p.get('required', []))}")
        print(f"   Optional parts: {len(p.get('optional', []))}")
    
    # Safety warnings
    if 'safety_warnings' in doc:
        print(f"\n⚠️  SAFETY WARNINGS: {len(doc['safety_warnings'])} critical warnings")
    
    # Common issues
    if 'common_issues' in doc:
        print(f"\n🔍 COMMON ISSUES: {len(doc['common_issues'])} known problems documented")
    
    # Metadata
    if 'metadata' in doc:
        m = doc['metadata']
        print(f"\n📊 METADATA:")
        print(f"   Generated: {m.get('generated_date', 'N/A')}")
        print(f"   AI Model: {m.get('ai_model', 'N/A')}")
        print(f"   Review Status: {m.get('review_status', 'N/A')}")
    
    print("\n" + "="*80 + "\n")


# Command-line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 5:
        print("="*80)
        print("SERVICE DOCUMENTATION GENERATOR")
        print("Swoop Service Auto - Professional Repair Information")
        print("="*80)
        print("\nUsage:")
        print("  python service_doc_generator.py <year> <make> <model> <service_name> [--refresh]")
        print("\nExamples:")
        print('  python service_doc_generator.py 2020 Chevrolet "Silverado 1500" "Brake Pads Replacement (Front)"')
        print('  python service_doc_generator.py 2022 Toyota Camry "Oil and Filter Change"')
        print('  python service_doc_generator.py 2019 Ford "F-150" "Alternator Replacement" --refresh')
        print("\nOptions:")
        print("  --refresh    Force regeneration even if cached version exists")
        print("\nConfiguration:")
        print("  Configure AI provider in .env file (RESEARCH_AI_PROVIDER)")
        print("\n" + "="*80)
        sys.exit(1)
    
    year = int(sys.argv[1])
    make = sys.argv[2]
    model = sys.argv[3]
    service_name = sys.argv[4]
    force_refresh = '--refresh' in sys.argv
    
    try:
        generator = ServiceDocGenerator()
        
        doc = generator.generate_documentation(
            year, 
            make, 
            model, 
            service_name,
            force_refresh=force_refresh
        )
        
        # Print summary
        print_documentation_summary(doc)
        
        # Print full JSON if requested
        if '--full' in sys.argv or '--json' in sys.argv:
            print("="*80)
            print("FULL JSON OUTPUT")
            print("="*80)
            print(json.dumps(doc, indent=2))
            print("="*80)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")
        sys.exit(1)
