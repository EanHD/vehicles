#!/usr/bin/env python3
"""
Regenerate all cached service documents with latest template
"""

import json
import sys
from pathlib import Path

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from service_doc_generator import ServiceDocGenerator

def main():
    print("🔄 Regenerating all cached service documents...")
    print("=" * 60)
    
    # Load generator
    gen = ServiceDocGenerator()
    
    # Get all cached documents
    cache_index = gen._load_cache_index()
    
    if not cache_index:
        print("❌ No cached documents found")
        return
    
    print(f"Found {len(cache_index)} cached documents\n")
    
    # Track results
    success_count = 0
    error_count = 0
    
    # Regenerate each document
    for i, (key, doc) in enumerate(cache_index.items(), 1):
        year = doc.get('year')
        make = doc.get('make')
        model = doc.get('model')
        service = doc.get('service')
        
        print(f"[{i}/{len(cache_index)}] {year} {make} {model} - {service}")
        
        try:
            doc_path, from_cache = gen.generate(
                year=year,
                make=make,
                model=model,
                service=service,
                force_regenerate=True  # Force regenerate to use new template
            )
            
            print(f"  ✅ Regenerated: {doc_path}")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            error_count += 1
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"✅ Successfully regenerated: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📄 Total: {len(cache_index)}")

if __name__ == "__main__":
    main()
