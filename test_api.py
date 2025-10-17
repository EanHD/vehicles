#!/usr/bin/env python3
"""
Test script for Swoop Service Auto REST API
Run this to verify all API endpoints are working correctly
"""

import requests
import json
import time
from pprint import pprint

# Configuration
API_BASE = "http://localhost:8000"
API_KEY = "swoop-dev-key-change-in-production"  # Should match your .env file

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

def test_root():
    """Test root endpoint"""
    print("\n🔍 Testing: GET /")
    response = requests.get(f"{API_BASE}/")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        pprint(response.json())
        print("✅ Root endpoint OK")
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_health():
    """Test health check endpoint"""
    print("\n🔍 Testing: GET /api/v1/health")
    response = requests.get(f"{API_BASE}/api/v1/health")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        pprint(data)
        print(f"✅ Health check OK - {data['database_stats']['total_vehicles']} vehicles, {data['database_stats']['total_services']} services")
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_list_makes():
    """Test list makes endpoint"""
    print("\n🔍 Testing: GET /api/v1/vehicles/makes")
    response = requests.get(f"{API_BASE}/api/v1/vehicles/makes", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        makes = response.json()
        print(f"✅ Found {len(makes)} makes")
        print(f"Sample: {makes[:5]}")
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_search_vehicles():
    """Test vehicle search"""
    print("\n🔍 Testing: GET /api/v1/vehicles/search?q=camry")
    response = requests.get(
        f"{API_BASE}/api/v1/vehicles/search?q=camry&limit=5",
        headers=headers
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        vehicles = response.json()
        print(f"✅ Found {len(vehicles)} results")
        if vehicles:
            print("Sample:")
            pprint(vehicles[0])
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_list_services():
    """Test list services endpoint"""
    print("\n🔍 Testing: GET /api/v1/services")
    response = requests.get(f"{API_BASE}/api/v1/services", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        services = response.json()
        print(f"✅ Found {len(services)} services")
        if services:
            print("Sample:")
            pprint(services[0])
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_generate_documentation():
    """Test documentation generation"""
    print("\n🔍 Testing: POST /api/v1/documentation/generate")
    
    request_data = {
        "year": 2015,
        "make": "Toyota",
        "model": "Camry",
        "service": "Engine Oil and Filter Change",
        "engine": "2.5L 4-Cyl"
    }
    
    print(f"Request: {json.dumps(request_data, indent=2)}")
    
    start_time = time.time()
    response = requests.post(
        f"{API_BASE}/api/v1/documentation/generate",
        headers=headers,
        json=request_data
    )
    elapsed = time.time() - start_time
    
    print(f"Status: {response.status_code}")
    print(f"Time: {elapsed:.2f}s")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Documentation generated")
        print(f"   Doc ID: {data['doc_id']}")
        print(f"   From cache: {data['from_cache']}")
        print(f"   Generation time: {data['generation_time']:.2f}s")
        print(f"   HTML URL: {data['html_url']}")
        return data['doc_id']
    else:
        print(f"❌ Failed: {response.text}")
        return None

def test_get_html(doc_id):
    """Test retrieving HTML documentation"""
    print(f"\n🔍 Testing: GET /api/v1/documentation/{doc_id}/html")
    response = requests.get(
        f"{API_BASE}/api/v1/documentation/{doc_id}/html",
        headers=headers
    )
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        html_size = len(response.text)
        print(f"✅ HTML retrieved: {html_size} bytes")
        
        # Check if HTML contains expected sections
        html = response.text.lower()
        sections = ['overview', 'safety', 'steps', 'torque']
        found = [s for s in sections if s in html]
        print(f"   Sections found: {found}")
        
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_list_cached():
    """Test list cached documents"""
    print("\n🔍 Testing: GET /api/v1/documentation")
    response = requests.get(
        f"{API_BASE}/api/v1/documentation?limit=5",
        headers=headers
    )
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        docs = response.json()
        print(f"✅ Found {len(docs)} cached documents")
        if docs:
            print("Sample:")
            pprint(docs[0])
        return True
    else:
        print(f"❌ Failed: {response.text}")
        return False

def test_invalid_auth():
    """Test authentication failure"""
    print("\n🔍 Testing: Invalid API key")
    bad_headers = {
        "X-API-Key": "invalid-key",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{API_BASE}/api/v1/vehicles/makes", headers=bad_headers)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 401:
        print(f"✅ Authentication correctly rejected invalid key")
        return True
    else:
        print(f"❌ Should have returned 401, got {response.status_code}")
        return False

def run_all_tests():
    """Run all API tests"""
    print("="*70)
    print("Swoop Service Auto API Test Suite")
    print("="*70)
    print(f"API Base: {API_BASE}")
    print(f"API Key: {API_KEY[:20]}...")
    
    results = {}
    
    # Basic tests (no auth required)
    results['root'] = test_root()
    results['health'] = test_health()
    
    # Authenticated tests
    results['list_makes'] = test_list_makes()
    results['search_vehicles'] = test_search_vehicles()
    results['list_services'] = test_list_services()
    
    # Documentation generation (may take ~15 seconds if not cached)
    doc_id = test_generate_documentation()
    if doc_id:
        results['generate_doc'] = True
        results['get_html'] = test_get_html(doc_id)
    else:
        results['generate_doc'] = False
        results['get_html'] = False
    
    # Cache management
    results['list_cached'] = test_list_cached()
    
    # Security test
    results['invalid_auth'] = test_invalid_auth()
    
    # Summary
    print("\n" + "="*70)
    print("Test Summary")
    print("="*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test, result in results.items():
        status = "✅" if result else "❌"
        print(f"{status} {test}")
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! API is fully operational.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Check output above.")
        return 1

if __name__ == "__main__":
    try:
        exit_code = run_all_tests()
        exit(exit_code)
    except requests.exceptions.ConnectionError:
        print("\n❌ Could not connect to API server.")
        print("   Make sure the API is running: ./start_api.sh")
        exit(1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
        exit(130)
