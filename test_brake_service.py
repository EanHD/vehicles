#!/usr/bin/env python3
"""Test brake service generation"""
import sys
sys.path.insert(0, 'tools')
from service_doc_generator import ServiceDocGenerator

gen = ServiceDocGenerator()
print("Testing brake pad replacement...")
print("=" * 60)

doc_path, from_cache = gen.generate(
    year=2019,
    make="Honda",
    model="Accord",
    service="Brake Pads Replacement (Front)",
    force_regenerate=True
)

print(f"\n✨ Generated: {doc_path}")
print("\nChecking for proper handling of non-fluid service...")
