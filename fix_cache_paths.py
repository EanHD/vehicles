#!/usr/bin/env python3
"""
Fix cache_index.json to use relative paths instead of absolute paths
This makes the app portable across different deployment environments
"""

import json
from pathlib import Path

def fix_cache_paths():
    """Convert all absolute paths in cache_index.json to relative paths"""
    
    project_root = Path(__file__).parent
    cache_index_path = project_root / "service_docs" / "cache_index.json"
    
    if not cache_index_path.exists():
        print("❌ cache_index.json not found")
        return
    
    # Load cache index
    with open(cache_index_path, 'r') as f:
        cache_index = json.load(f)
    
    print(f"📋 Found {len(cache_index)} cached documents")
    
    # Convert paths
    updated_count = 0
    for key, doc in cache_index.items():
        path = Path(doc['path'])
        
        # If path is absolute, make it relative
        if path.is_absolute():
            try:
                relative_path = path.relative_to(project_root)
                doc['path'] = str(relative_path)
                updated_count += 1
                print(f"  ✓ Converted: {path.name}")
            except ValueError:
                print(f"  ⚠️  Could not convert: {path}")
    
    # Save updated index
    with open(cache_index_path, 'w') as f:
        json.dump(cache_index, f, indent=2)
    
    print(f"\n✅ Updated {updated_count} paths to be relative")
    print(f"💾 Saved to: {cache_index_path}")

if __name__ == "__main__":
    fix_cache_paths()
