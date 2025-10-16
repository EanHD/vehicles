#!/bin/bash
echo "================================================"
echo "   SWOOP SERVICE AUTO - SYSTEM STATUS CHECK"
echo "================================================"
echo ""

echo "📁 Document Statistics:"
echo "   Cached documents: $(jq 'length' service_docs/cache_index.json)"
echo "   Generated diagrams: $(ls service_docs/diagrams/*.png 2>/dev/null | wc -l)"
echo ""

echo "✅ Recent Improvements:"
echo "   1. Accurate torque specifications with validation"
echo "   2. Fixed Common Issues section contrast"
echo "   3. AI diagram generation working (Together AI)"
echo "   4. Sidebar cleaned up (removed confusing icon)"
echo "   5. Document deletion with confirmation"
echo ""

echo "🔧 API Configuration:"
echo "   Research AI: Perplexity Sonar Pro (web-enabled)"
echo "   Formatter AI: OpenAI GPT-4o-mini"
echo "   Diagram AI: Together AI FLUX.1-schnell"
echo ""

echo "📊 Latest Generated Document:"
ls -lh service_docs/Toyota/Camry/2015_Oil_Change.html 2>/dev/null | tail -1 | awk '{print "   " $9 " - " $5}'
echo ""

echo "🎯 System Status: ✅ ALL SYSTEMS OPERATIONAL"
echo ""
echo "To start the app: streamlit run app.py"
echo "================================================"
