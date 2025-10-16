#!/usr/bin/env python3
"""
Batch generator for popular vehicle/service combinations
Pre-generate documentation for high-volume services to build cache
"""

import sys
from pathlib import Path
from service_doc_generator import ServiceDocGenerator
import time
from typing import List, Tuple

# Define popular vehicle/service combinations
POPULAR_VEHICLES = [
    # Ford F-Series (most popular trucks)
    (2020, "Ford", "F-150"),
    (2019, "Ford", "F-150"),
    (2018, "Ford", "F-150"),
    (2015, "Ford", "F-150"),
    (2021, "Ford", "F-150"),
    
    # Chevrolet Silverado
    (2020, "Chevrolet", "Silverado 1500"),
    (2019, "Chevrolet", "Silverado 1500"),
    (2015, "Chevrolet", "Silverado 1500"),
    
    # Ram Trucks
    (2020, "Ram", "1500"),
    (2019, "Ram", "1500"),
    
    # Toyota Camry (popular sedan)
    (2020, "Toyota", "Camry"),
    (2019, "Toyota", "Camry"),
    (2018, "Toyota", "Camry"),
    
    # Honda Civic
    (2020, "Honda", "Civic"),
    (2019, "Honda", "Civic"),
    
    # Toyota RAV4 (popular SUV)
    (2020, "Toyota", "RAV4"),
    (2019, "Toyota", "RAV4"),
    
    # Honda CR-V
    (2020, "Honda", "CR-V"),
    (2019, "Honda", "CR-V"),
]

POPULAR_SERVICES = [
    "Oil Change",
    "Brake Pads Replacement (Front)",
    "Brake Pads Replacement (Rear)",
    "Air Filter Replacement",
    "Cabin Air Filter Replacement",
    "Battery Replacement",
    "Spark Plugs Replacement",
    "Tire Rotation",
    "Wiper Blades Replacement",
    "Coolant Flush",
]

def batch_generate(
    vehicles: List[Tuple[int, str, str]],
    services: List[str],
    max_documents: int = 100,
    delay_seconds: float = 2.0
):
    """
    Generate documents in batch mode
    
    Args:
        vehicles: List of (year, make, model) tuples
        services: List of service names
        max_documents: Maximum documents to generate (to control costs)
        delay_seconds: Delay between API calls (be nice to API)
    """
    gen = ServiceDocGenerator()
    
    print(f"🔍 Using {gen.research_ai.provider} ({gen.research_ai.model}) for research")
    print(f"📝 Using {gen.formatter_ai.provider} ({gen.formatter_ai.model}) for formatting")
    print()
    
    generated_count = 0
    cached_count = 0
    error_count = 0
    total_combos = len(vehicles) * len(services)
    
    print(f"🚀 Starting batch generation")
    print(f"Vehicles: {len(vehicles)}")
    print(f"Services: {len(services)}")
    print(f"Total combinations: {total_combos}")
    print(f"Max documents to generate: {max_documents}")
    print("-" * 60)
    
    start_time = time.time()
    
    for year, make, model in vehicles:
        for service in services:
            # Check if we've hit the limit
            if generated_count >= max_documents:
                print(f"\n✋ Reached maximum document limit ({max_documents})")
                break
            
            try:
                doc_path, from_cache = gen.generate(
                    year=year,
                    make=make,
                    model=model,
                    service=service
                )
                
                if from_cache:
                    cached_count += 1
                    print(f"📋 [{cached_count + generated_count}/{total_combos}] CACHED: {year} {make} {model} - {service}")
                else:
                    generated_count += 1
                    print(f"✨ [{cached_count + generated_count}/{total_combos}] GENERATED: {year} {make} {model} - {service}")
                    
                    # Delay between generations to avoid rate limits
                    if delay_seconds > 0:
                        time.sleep(delay_seconds)
                
            except Exception as e:
                error_count += 1
                print(f"❌ [{cached_count + generated_count + error_count}/{total_combos}] ERROR: {year} {make} {model} - {service}: {e}")
        
        # Break outer loop too
        if generated_count >= max_documents:
            break
    
    elapsed_time = time.time() - start_time
    
    print("\n" + "=" * 60)
    print("📊 Batch Generation Summary")
    print("=" * 60)
    print(f"Total processed: {cached_count + generated_count + error_count}/{total_combos}")
    print(f"✨ Newly generated: {generated_count}")
    print(f"📋 From cache: {cached_count}")
    print(f"❌ Errors: {error_count}")
    print(f"⏱️  Time elapsed: {elapsed_time:.1f} seconds")
    print(f"⚡ Average per doc: {elapsed_time / max(1, generated_count):.1f} seconds")
    print(f"💰 Estimated cost: ${generated_count * 0.05:.2f} (at $0.05/doc)")
    print("=" * 60)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch generate service documentation')
    parser.add_argument('--max', type=int, default=100, help='Maximum documents to generate')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between API calls (seconds)')
    
    args = parser.parse_args()
    
    batch_generate(
        vehicles=POPULAR_VEHICLES,
        services=POPULAR_SERVICES,
        max_documents=args.max,
        delay_seconds=args.delay
    )
