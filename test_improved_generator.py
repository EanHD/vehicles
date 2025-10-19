#!/usr/bin/env python3
"""Test the improved service doc generator"""
import sys
sys.path.insert(0, 'tools')

from service_doc_generator import ServiceDocGenerator

# Test with a simple oil change
gen = ServiceDocGenerator()

print("Testing improved prompt with 2020 Toyota Camry - Oil Change...")
print("=" * 60)

doc_path, from_cache = gen.generate(
    year=2020,
    make="Toyota", 
    model="Camry",
    service="Oil Change",
    force_regenerate=True
)

print(f"\n{'✨' if not from_cache else '📋'} Generated: {doc_path}")
print("\nNow check the document for:")
print("  1. Parts list with realistic fluid quantities (e.g., '5 qt' not '1')")
print("  2. Specific torque values (e.g., '27 ft-lbs (37 Nm)')")  
print("  3. Detailed procedure steps with exact specifications")
print("  4. Comprehensive common issues section")
