# Mobile Mechanic App Integration Guide

## Overview

This guide explains how to integrate the Swoop Service Auto API into your mobile mechanic application. When a customer books a job, your tech (you) will automatically have access to professional service documentation in your dashboard.

## Integration Workflow

### 1. Customer Books Job → 2. System Generates Docs → 3. Tech Views in Dashboard

```
┌─────────────────┐
│   Customer      │
│   Books Job     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│   Mobile App Backend                │
│                                     │
│  1. Extract vehicle info            │
│  2. Map concern to service type     │
│  3. Call API to generate docs       │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│   Swoop Service Auto API            │
│                                     │
│  1. Check cache (~100ms)            │
│  2. Generate if needed (~15s)       │
│  3. Return HTML document            │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│   Tech Dashboard                    │
│                                     │
│  1. Display service documentation   │
│  2. Show torque specs, procedures   │
│  3. Enable offline caching          │
└─────────────────────────────────────┘
```

## API Endpoints Overview

### Core Endpoints for Mobile App

1. **Vehicle Search**: `/api/v1/vehicles/search?q=camry`
   - Autocomplete when customer enters vehicle info
   - Returns: year, make, model, engine options

2. **Service List**: `/api/v1/services?category=Maintenance`
   - Populate service selection dropdown
   - Returns: service names, descriptions, labor times

3. **Generate Documentation**: `POST /api/v1/documentation/generate`
   - Called when job is booked
   - Returns: doc_id, html_url, generation time

4. **Retrieve HTML**: `/api/v1/documentation/{doc_id}/html`
   - Display in WebView in tech dashboard
   - Returns: Complete HTML document

## Implementation Examples

### React Native Integration

```javascript
// services/serviceDocAPI.js
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_BASE = 'https://api.swoopservice.com'; // or your Tailscale address
const API_KEY = 'your-api-key-here';

class ServiceDocAPI {
  constructor() {
    this.headers = {
      'X-API-Key': API_KEY,
      'Content-Type': 'application/json'
    };
  }

  // Search vehicles for autocomplete
  async searchVehicles(query) {
    const response = await fetch(
      `${API_BASE}/api/v1/vehicles/search?q=${encodeURIComponent(query)}&limit=10`,
      { headers: this.headers }
    );
    
    if (!response.ok) throw new Error('Vehicle search failed');
    return await response.json();
  }

  // Get available services
  async getServices(category = null) {
    let url = `${API_BASE}/api/v1/services`;
    if (category) url += `?category=${encodeURIComponent(category)}`;
    
    const response = await fetch(url, { headers: this.headers });
    if (!response.ok) throw new Error('Services fetch failed');
    return await response.json();
  }

  // Generate service documentation for a job
  async generateServiceDoc(vehicle, service) {
    // Check local cache first
    const cacheKey = `${vehicle.year}_${vehicle.make}_${vehicle.model}_${service}`;
    const cached = await AsyncStorage.getItem(cacheKey);
    
    if (cached) {
      console.log('Using local cache');
      return JSON.parse(cached);
    }

    // Generate via API
    const response = await fetch(
      `${API_BASE}/api/v1/documentation/generate`,
      {
        method: 'POST',
        headers: this.headers,
        body: JSON.stringify({
          year: vehicle.year,
          make: vehicle.make,
          model: vehicle.model,
          service: service,
          engine: vehicle.engine,
          transmission: vehicle.transmission,
          body_style: vehicle.body_style
        })
      }
    );

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Documentation generation failed');
    }

    const data = await response.json();
    
    // Cache the result
    await AsyncStorage.setItem(cacheKey, JSON.stringify(data));
    
    return data;
  }

  // Get HTML for WebView
  getDocumentURL(docId) {
    return `${API_BASE}/api/v1/documentation/${docId}/html`;
  }

  // Get HTML headers for authenticated WebView request
  getWebViewHeaders() {
    return { 'X-API-Key': API_KEY };
  }
}

export default new ServiceDocAPI();
```

### Job Booking Component

```javascript
// screens/JobDetailsScreen.js
import React, { useState, useEffect } from 'react';
import { View, Text, Button, ActivityIndicator, Alert } from 'react-native';
import { WebView } from 'react-native-webview';
import serviceDocAPI from '../services/serviceDocAPI';

export default function JobDetailsScreen({ route, navigation }) {
  const { job } = route.params; // Job from booking system
  const [loading, setLoading] = useState(false);
  const [docURL, setDocURL] = useState(null);
  const [error, setError] = useState(null);

  // Generate documentation when component mounts
  useEffect(() => {
    generateDocumentation();
  }, []);

  const generateDocumentation = async () => {
    setLoading(true);
    setError(null);

    try {
      // Extract vehicle from job
      const vehicle = {
        year: job.vehicle.year,
        make: job.vehicle.make,
        model: job.vehicle.model,
        engine: job.vehicle.engine,
        transmission: job.vehicle.transmission,
        body_style: job.vehicle.body_style
      };

      // Generate documentation
      const result = await serviceDocAPI.generateServiceDoc(
        vehicle,
        job.serviceType
      );

      // Set URL for WebView
      const url = serviceDocAPI.getDocumentURL(result.doc_id);
      setDocURL(url);

      // Show timing info
      if (result.from_cache) {
        console.log('Document loaded from cache instantly');
      } else {
        console.log(`Document generated in ${result.generation_time}s`);
      }

    } catch (err) {
      console.error('Documentation generation failed:', err);
      setError(err.message);
      Alert.alert('Error', 'Could not load service documentation');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <ActivityIndicator size="large" />
        <Text style={{ marginTop: 10 }}>
          Loading service documentation...
        </Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Text>Error: {error}</Text>
        <Button title="Retry" onPress={generateDocumentation} />
      </View>
    );
  }

  return (
    <View style={{ flex: 1 }}>
      <View style={{ padding: 10, backgroundColor: '#f5f5f5' }}>
        <Text style={{ fontSize: 16, fontWeight: 'bold' }}>
          {job.vehicle.year} {job.vehicle.make} {job.vehicle.model}
        </Text>
        <Text style={{ fontSize: 14 }}>
          Service: {job.serviceType}
        </Text>
      </View>

      {docURL && (
        <WebView
          source={{
            uri: docURL,
            headers: serviceDocAPI.getWebViewHeaders()
          }}
          style={{ flex: 1 }}
          startInLoadingState={true}
          renderLoading={() => (
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
              <ActivityIndicator size="large" />
            </View>
          )}
        />
      )}
    </View>
  );
}
```

### Swift/iOS Integration

```swift
// ServiceDocAPI.swift
import Foundation

class ServiceDocAPI {
    private let baseURL = "https://api.swoopservice.com"
    private let apiKey = "your-api-key-here"
    
    private var headers: [String: String] {
        return [
            "X-API-Key": apiKey,
            "Content-Type": "application/json"
        ]
    }
    
    // Search vehicles
    func searchVehicles(query: String, completion: @escaping (Result<[Vehicle], Error>) -> Void) {
        let urlString = "\(baseURL)/api/v1/vehicles/search?q=\(query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")&limit=10"
        
        guard let url = URL(string: urlString) else {
            completion(.failure(NSError(domain: "InvalidURL", code: -1)))
            return
        }
        
        var request = URLRequest(url: url)
        headers.forEach { request.setValue($1, forHTTPHeaderField: $0) }
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let data = data else {
                completion(.failure(NSError(domain: "NoData", code: -1)))
                return
            }
            
            do {
                let vehicles = try JSONDecoder().decode([Vehicle].self, from: data)
                completion(.success(vehicles))
            } catch {
                completion(.failure(error))
            }
        }.resume()
    }
    
    // Generate documentation
    func generateDocumentation(
        vehicle: Vehicle,
        service: String,
        completion: @escaping (Result<ServiceDocResponse, Error>) -> Void
    ) {
        let url = URL(string: "\(baseURL)/api/v1/documentation/generate")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        headers.forEach { request.setValue($1, forHTTPHeaderField: $0) }
        
        let requestBody: [String: Any] = [
            "year": vehicle.year,
            "make": vehicle.make,
            "model": vehicle.model,
            "service": service,
            "engine": vehicle.engine ?? "",
            "transmission": vehicle.transmission ?? "",
            "body_style": vehicle.bodyStyle ?? ""
        ]
        
        request.httpBody = try? JSONSerialization.data(withJSONObject: requestBody)
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let data = data else {
                completion(.failure(NSError(domain: "NoData", code: -1)))
                return
            }
            
            do {
                let response = try JSONDecoder().decode(ServiceDocResponse.self, from: data)
                completion(.success(response))
            } catch {
                completion(.failure(error))
            }
        }.resume()
    }
    
    // Get document URL for WKWebView
    func documentURL(docId: String) -> URL {
        return URL(string: "\(baseURL)/api/v1/documentation/\(docId)/html")!
    }
    
    // Get URL request with authentication headers
    func authenticatedRequest(for docId: String) -> URLRequest {
        var request = URLRequest(url: documentURL(docId: docId))
        headers.forEach { request.setValue($1, forHTTPHeaderField: $0) }
        return request
    }
}

// Models
struct Vehicle: Codable {
    let year: Int
    let make: String
    let model: String
    let engine: String?
    let transmission: String?
    let bodyStyle: String?
    
    enum CodingKeys: String, CodingKey {
        case year, make, model, engine, transmission
        case bodyStyle = "body_style"
    }
}

struct ServiceDocResponse: Codable {
    let status: String
    let docId: String
    let fromCache: Bool
    let generationTime: Double
    let htmlUrl: String
    let metadata: DocumentMetadata
    
    enum CodingKeys: String, CodingKey {
        case status
        case docId = "doc_id"
        case fromCache = "from_cache"
        case generationTime = "generation_time"
        case htmlUrl = "html_url"
        case metadata
    }
}

struct DocumentMetadata: Codable {
    let vehicle: Vehicle
    let service: String
    let generatedAt: String
    let fileSize: Int
    
    enum CodingKeys: String, CodingKey {
        case vehicle, service
        case generatedAt = "generated_at"
        case fileSize = "file_size"
    }
}
```

### View Controller with WKWebView

```swift
// JobDetailsViewController.swift
import UIKit
import WebKit

class JobDetailsViewController: UIViewController {
    private let webView = WKWebView()
    private let loadingIndicator = UIActivityIndicatorView(style: .large)
    private let api = ServiceDocAPI()
    
    var job: Job!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupUI()
        loadServiceDocumentation()
    }
    
    private func setupUI() {
        view.backgroundColor = .white
        
        // Add web view
        webView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(webView)
        
        // Add loading indicator
        loadingIndicator.translatesAutoresizingMaskIntoConstraints = false
        loadingIndicator.hidesWhenStopped = true
        view.addSubview(loadingIndicator)
        
        NSLayoutConstraint.activate([
            webView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            
            loadingIndicator.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            loadingIndicator.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
        
        title = "\(job.vehicle.year) \(job.vehicle.make) \(job.vehicle.model)"
    }
    
    private func loadServiceDocumentation() {
        loadingIndicator.startAnimating()
        
        api.generateDocumentation(vehicle: job.vehicle, service: job.serviceType) { [weak self] result in
            DispatchQueue.main.async {
                self?.loadingIndicator.stopAnimating()
                
                switch result {
                case .success(let response):
                    print("Document \(response.fromCache ? "cached" : "generated in \(response.generationTime)s")")
                    
                    // Load HTML with authentication
                    let request = self?.api.authenticatedRequest(for: response.docId)
                    if let request = request {
                        self?.webView.load(request)
                    }
                    
                case .failure(let error):
                    print("Error: \(error)")
                    self?.showErrorAlert(error: error)
                }
            }
        }
    }
    
    private func showErrorAlert(error: Error) {
        let alert = UIAlertController(
            title: "Error",
            message: "Could not load service documentation: \(error.localizedDescription)",
            preferredStyle: .alert
        )
        alert.addAction(UIAlertAction(title: "Retry", style: .default) { _ in
            self.loadServiceDocumentation()
        })
        alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
        present(alert, animated: true)
    }
}
```

## Best Practices

### 1. Caching Strategy

**Client-Side Caching:**
```javascript
// Cache documents locally for offline access
const CACHE_DURATION = 7 * 24 * 60 * 60 * 1000; // 7 days

async function getCachedDoc(cacheKey) {
  const cached = await AsyncStorage.getItem(cacheKey);
  if (cached) {
    const { data, timestamp } = JSON.parse(cached);
    if (Date.now() - timestamp < CACHE_DURATION) {
      return data;
    }
  }
  return null;
}

async function cacheDoc(cacheKey, data) {
  await AsyncStorage.setItem(
    cacheKey,
    JSON.stringify({ data, timestamp: Date.now() })
  );
}
```

**Server-Side Caching:**
- First request: ~15 seconds (AI generation)
- Subsequent requests: < 100ms (cached)
- No need to force regenerate unless specs update

### 2. Error Handling

```javascript
try {
  const doc = await serviceDocAPI.generateServiceDoc(vehicle, service);
  // Success
} catch (error) {
  if (error.message.includes('Vehicle not found')) {
    // Handle unknown vehicle
    Alert.alert('Vehicle Not Found', 'This vehicle is not in our database.');
  } else if (error.message.includes('Service not found')) {
    // Handle unknown service
    Alert.alert('Service Not Found', 'This service type is not available.');
  } else if (error.message.includes('API key')) {
    // Handle auth error
    console.error('API authentication failed - check API key');
  } else {
    // Generic error
    Alert.alert('Error', 'Could not generate documentation. Please try again.');
  }
}
```

### 3. Loading States

Show appropriate feedback to user:

```javascript
// Generating new documentation
<ActivityIndicator />
<Text>Generating service documentation... (~15 seconds)</Text>

// Loading from cache
<ActivityIndicator />
<Text>Loading documentation...</Text>

// Document ready
<WebView source={{ uri: docURL }} />
```

### 4. Offline Support

```javascript
// Store HTML locally for offline viewing
import RNFS from 'react-native-fs';

async function downloadForOffline(docId) {
  const html = await fetch(
    `${API_BASE}/api/v1/documentation/${docId}/html`,
    { headers: { 'X-API-Key': API_KEY } }
  ).then(r => r.text());
  
  const path = `${RNFS.DocumentDirectoryPath}/${docId}.html`;
  await RNFS.writeFile(path, html, 'utf8');
  
  return path;
}

// Load offline
<WebView source={{ uri: `file://${offlinePath}` }} />
```

## Deployment Considerations

### Development (Tailscale)

```javascript
// Use your Tailscale IP for local network access
const API_BASE = 'http://your-tailscale-ip:8000';
```

### Production

1. **Deploy API** on a server with HTTPS
2. **Use environment variables** for API base URL
3. **Implement rate limiting** to prevent abuse
4. **Set up monitoring** for API health
5. **Configure CORS** to only allow your mobile app

```javascript
// Environment-based configuration
const API_BASE = __DEV__
  ? 'http://your-tailscale-ip:8000'  // Development
  : 'https://api.swoopservice.com';   // Production
```

## Testing

Test the integration with the included test script:

```bash
cd /home/eanhd/projects/vehicles
source venv/bin/activate
python test_api.py
```

Or test individual endpoints:

```bash
# Test from your mobile app network
curl -H "X-API-Key: your-key" \
  http://your-tailscale-ip:8000/api/v1/health
```

## Support

- **API Documentation**: `API_DOCUMENTATION.md`
- **Quick Start**: `API_QUICK_START.md`
- **Test Script**: `test_api.py`
- **Issues**: Check API server logs

---

**Ready to integrate?** Start with the health check endpoint and work your way through the examples above!
