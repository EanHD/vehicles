#!/usr/bin/env python3
"""
Script to regenerate cached service documents
"""

import sys
from pathlib import Path

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from service_doc_generator import ServiceDocGenerator

# Common vehicles and services to generate
TEST_DOCS = [
    # Toyota Camry - Oil Change
    {
        'year': 2020,
        'make': 'Toyota',
        'model': 'Camry',
        'service': 'Oil Change'
    },
    # Honda Accord - Oil Change
    {
        'year': 2019,
        'make': 'Honda',
        'model': 'Accord',
        'service': 'Oil Change'
    },
    # Ford F-150 - Oil Change
    {
        'year': 2021,
        'make': 'Ford',
        'model': 'F-150',
        'service': 'Oil Change'
    },
    # Toyota Camry - Brake Pad Replacement
    {
        'year': 2020,
        'make': 'Toyota',
        'model': 'Camry',
        'service': 'Brake Pad Replacement'
    },
    # Honda Accord - Alternator Replacement
    {
        'year': 2019,
        'make': 'Honda',
        'model': 'Accord',
        'service': 'Alternator Replacement'
    },
    # Chevrolet Silverado 1500 - Battery Replacement
    {
        'year': 2020,
        'make': 'Chevrolet',
        'model': 'Silverado 1500',
        'service': 'Battery Replacement'
    },
]

def main():
    print("=" * 80)
    print("🔧 SWOOP SERVICE AUTO - Document Regeneration")
    print("=" * 80)
    print()
    
    # Initialize generator WITHOUT diagram generation
    # (diagrams are low quality and cause issues)
    print("📦 Initializing service document generator...")
    gen = ServiceDocGenerator(enable_diagrams=False)
    print(f"✅ Loaded {len(gen.vehicles)} vehicles and {len(gen.services)} services")
    print()
    
    success_count = 0
    fail_count = 0
    
    for i, doc_spec in enumerate(TEST_DOCS, 1):
        print(f"\n[{i}/{len(TEST_DOCS)}] Generating: {doc_spec['year']} {doc_spec['make']} {doc_spec['model']} - {doc_spec['service']}")
        print("-" * 80)
        
        try:
            doc_path, from_cache = gen.generate(
                year=doc_spec['year'],
                make=doc_spec['make'],
                model=doc_spec['model'],
                service=doc_spec['service'],
                force_regenerate=True  # Force fresh generation
            )
            
            print(f"✅ SUCCESS: {doc_path}")
            success_count += 1
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            fail_count += 1
    
    print("\n" + "=" * 80)
    print(f"📊 SUMMARY")
    print("=" * 80)
    print(f"✅ Successful: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print(f"📄 Total Cache: {len(gen.cache_index)} documents")
    print()
    
    if success_count > 0:
        print("🎉 Documents successfully generated! View them in the Streamlit app.")
    
    return 0 if fail_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
