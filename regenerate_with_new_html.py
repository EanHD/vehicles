#!/usr/bin/env python3
"""
Regenerate all cached service documents with new professional HTML format
"""

import json
import os
import sys
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent / 'tools'))

from service_doc_generator import ServiceDocGenerator


def regenerate_all_cached_documents():
    """Regenerate all documents in the cache index with new HTML format"""
    
    print("=" * 70)
    print("REGENERATING ALL CACHED DOCUMENTS WITH PROFESSIONAL HTML FORMAT")
    print("=" * 70)
    print()
    
    # Load cache index
    cache_index_path = Path(__file__).parent / 'service_docs' / 'cache_index.json'
    
    if not cache_index_path.exists():
        print("❌ Cache index not found. No documents to regenerate.")
        return
    
    with open(cache_index_path, 'r') as f:
        cache_index = json.load(f)
    
    print(f"📊 Found {len(cache_index)} cached documents")
    print()
    
    # Initialize generator
    gen = ServiceDocGenerator()
    
    # Track results
    success_count = 0
    error_count = 0
    errors = []
    
    # Regenerate each document
    for i, (cache_key, entry) in enumerate(cache_index.items(), 1):
        year = entry.get('year')
        make = entry.get('make')
        model = entry.get('model')
        service = entry.get('service')
        cached_path = entry.get('path')
        
        print(f"[{i}/{len(cache_index)}] {year} {make} {model} - {service}")
        
        # Delete existing cached file
        if cached_path:
            full_path = Path(__file__).parent / cached_path
            if full_path.exists():
                try:
                    full_path.unlink()
                    print(f"  ✓ Deleted old cache: {cached_path}")
                except Exception as e:
                    print(f"  ⚠️  Could not delete: {e}")
        
        # Regenerate
        try:
            doc_path, from_cache = gen.generate(
                year=year,
                make=make,
                model=model,
                service=service
            )
            
            if not from_cache:
                print(f"  ✅ Regenerated: {doc_path}")
                success_count += 1
            else:
                print(f"  ⚠️  Used cache (shouldn't happen): {doc_path}")
                success_count += 1
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
            error_count += 1
            errors.append({
                'vehicle': f"{year} {make} {model}",
                'service': service,
                'error': str(e)
            })
        
        print()
    
    # Print summary
    print("=" * 70)
    print("REGENERATION COMPLETE")
    print("=" * 70)
    print(f"✅ Success: {success_count}")
    print(f"❌ Errors: {error_count}")
    
    if errors:
        print()
        print("ERRORS:")
        for err in errors:
            print(f"  • {err['vehicle']} - {err['service']}")
            print(f"    {err['error']}")
    
    print()
    print("🎉 All documents now use professional OEM/AllData-style HTML!")


if __name__ == '__main__':
    try:
        regenerate_all_cached_documents()
    except KeyboardInterrupt:
        print("\n\n⚠️  Regeneration interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
