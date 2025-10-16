#!/usr/bin/env python3
"""
Flask API for Service Documentation Generator
Provides web endpoints for mobile/app access
"""

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from service_doc_generator import ServiceDocGenerator
from pathlib import Path
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile app access

# Initialize generator
generator = ServiceDocGenerator()

@app.route('/')
def index():
    """API documentation"""
    return jsonify({
        "service": "Swoop Service Auto Documentation API",
        "version": "1.0",
        "endpoints": {
            "/api/service_doc": "Generate service document (GET)",
            "/api/vehicles": "Search vehicles (GET)",
            "/api/services": "List services (GET)",
            "/api/cache/stats": "Cache statistics (GET)"
        },
        "usage": {
            "generate_doc": "/api/service_doc?year=2015&make=Ford&model=F-150&service=Oil Change",
            "search_vehicles": "/api/vehicles?make=Ford&model=F-150",
            "list_services": "/api/services?category=Brakes"
        }
    })

@app.route('/api/service_doc')
def generate_service_doc():
    """
    Generate or retrieve cached service document
    
    Query params:
        year (int): Vehicle year
        make (str): Vehicle make
        model (str): Vehicle model
        service (str): Service name
        force (bool): Force regenerate (optional)
        format (str): 'html' or 'json' (default: html)
    """
    year = request.args.get('year', type=int)
    make = request.args.get('make')
    model = request.args.get('model')
    service = request.args.get('service')
    force = request.args.get('force', 'false').lower() == 'true'
    output_format = request.args.get('format', 'html').lower()
    
    # Validate required params
    if not all([year, make, model, service]):
        return jsonify({
            "error": "Missing required parameters",
            "required": ["year", "make", "model", "service"]
        }), 400
    
    try:
        # Generate document
        doc_path, from_cache = generator.generate(
            year=year,
            make=make,
            model=model,
            service=service,
            force_regenerate=force
        )
        
        if output_format == 'html':
            # Return HTML document
            return send_file(doc_path, mimetype='text/html')
        else:
            # Return JSON metadata
            return jsonify({
                "success": True,
                "document_path": str(doc_path),
                "from_cache": from_cache,
                "vehicle": {
                    "year": year,
                    "make": make,
                    "model": model
                },
                "service": service
            })
    
    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 404
    
    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

@app.route('/api/vehicles')
def search_vehicles():
    """
    Search vehicles in database
    
    Query params:
        make (str): Filter by make (optional)
        model (str): Filter by model (optional)
        year (int): Filter by year (optional)
        limit (int): Max results (default: 50)
    """
    make = request.args.get('make', '').lower()
    model = request.args.get('model', '').lower()
    year = request.args.get('year', type=int)
    limit = request.args.get('limit', 50, type=int)
    
    results = []
    
    for vehicle in generator.vehicles:
        # Apply filters
        if make and vehicle.get('make', '').lower() != make:
            continue
        if model and model not in vehicle.get('model', '').lower():
            continue
        if year and year not in vehicle.get('years', []):
            continue
        
        results.append({
            "years": vehicle.get('years', []),
            "make": vehicle.get('make'),
            "model": vehicle.get('model'),
            "engines": vehicle.get('engines', []),
            "transmissions": vehicle.get('transmissions', []),
            "difficulty": vehicle.get('difficulty_modifier', 1.0)
        })
        
        if len(results) >= limit:
            break
    
    return jsonify({
        "count": len(results),
        "limit": limit,
        "results": results
    })

@app.route('/api/services')
def list_services():
    """
    List available services
    
    Query params:
        category (str): Filter by category (optional)
        mobile (bool): Filter mobile-capable only (optional)
    """
    category = request.args.get('category', '').lower()
    mobile_only = request.args.get('mobile', 'false').lower() == 'true'
    
    results = []
    
    for service in generator.services:
        # Apply filters
        if category and service.get('category', '').lower() != category:
            continue
        if mobile_only and not service.get('mobile', False):
            continue
        
        results.append({
            "name": service.get('name'),
            "category": service.get('category'),
            "labor_hours": service.get('labor_time_hours'),
            "labor_cost": service.get('price_range_labor'),
            "parts_cost": service.get('price_range_parts'),
            "mobile": service.get('mobile', False)
        })
    
    return jsonify({
        "count": len(results),
        "results": results
    })

@app.route('/api/cache/stats')
def cache_stats():
    """Get cache statistics"""
    
    # Count by make
    by_make = {}
    by_service = {}
    
    for doc in generator.cache_index.values():
        make = doc.get('make', 'Unknown')
        service = doc.get('service', 'Unknown')
        
        by_make[make] = by_make.get(make, 0) + 1
        by_service[service] = by_service.get(service, 0) + 1
    
    return jsonify({
        "total_documents": len(generator.cache_index),
        "cache_directory": str(generator.cache_dir),
        "by_make": dict(sorted(by_make.items(), key=lambda x: x[1], reverse=True)[:10]),
        "by_service": dict(sorted(by_service.items(), key=lambda x: x[1], reverse=True)[:10])
    })

@app.route('/api/popular')
def popular_combinations():
    """Get popular vehicle/service combinations for pre-caching"""
    
    popular = [
        {"year": 2020, "make": "Ford", "model": "F-150", "service": "Oil Change"},
        {"year": 2020, "make": "Ford", "model": "F-150", "service": "Brake Pads Replacement (Front)"},
        {"year": 2019, "make": "Chevrolet", "model": "Silverado 1500", "service": "Oil Change"},
        {"year": 2020, "make": "Toyota", "model": "Camry", "service": "Oil Change"},
        {"year": 2020, "make": "Toyota", "model": "RAV4", "service": "Brake Pads Replacement (Front)"},
        {"year": 2019, "make": "Honda", "model": "Civic", "service": "Oil Change"},
        {"year": 2020, "make": "Ram", "model": "1500", "service": "Oil Change"},
    ]
    
    return jsonify({
        "count": len(popular),
        "combinations": popular,
        "note": "These are the most requested service documents. Pre-cache them for instant delivery."
    })

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Service Documentation API')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    print("🚀 Starting Swoop Service Auto Documentation API")
    print(f"📡 Listening on http://{args.host}:{args.port}")
    print(f"📋 Total vehicles: {len(generator.vehicles)}")
    print(f"🔧 Total services: {len(generator.services)}")
    print(f"💾 Cached documents: {len(generator.cache_index)}")
    print("\n✅ API ready for requests!\n")
    
    app.run(host=args.host, port=args.port, debug=args.debug)
