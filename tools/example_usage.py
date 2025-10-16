#!/usr/bin/env python3
"""
Example usage of Service Documentation Generator
"""

from service_doc_generator import ServiceDocGenerator

# Initialize generator (paths will default to correct locations)
gen = ServiceDocGenerator()

# Example 1: Generate a single service document
print("Example 1: Generating brake service for 2015 Ford F-150")
doc_path, from_cache = gen.generate(
    year=2015,
    make="Ford",
    model="F-150",
    service="Brake Pads Replacement (Front)"
)
print(f"✓ Generated: {doc_path} (cached: {from_cache})")

# Example 2: Generate multiple services for same vehicle
print("\nExample 2: Generating multiple services for 2020 Toyota Camry")
services = [
    "Oil Change",
    "Brake Pads Replacement (Front)",
    "Air Filter Replacement",
    "Spark Plugs Replacement"
]

for service in services:
    try:
        doc_path, from_cache = gen.generate(
            year=2020,
            make="Toyota",
            model="Camry",
            service=service
        )
        print(f"✓ {service}: {doc_path} (cached: {from_cache})")
    except Exception as e:
        print(f"✗ {service}: {e}")

# Example 3: Check cache statistics
print(f"\nCache Statistics:")
print(f"Total cached documents: {len(gen.cache_index)}")
print(f"Cache directory: {gen.cache_dir}")
