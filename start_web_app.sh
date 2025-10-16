#!/bin/bash
# Swoop Service Auto - Web App Startup Script

echo "🔧 Starting Swoop Service Auto Web Application..."
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found. Are you in the correct directory?"
    echo "Please run this script from /home/eanhd/projects/vehicles/"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Virtual environment not found. Creating..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -q -r requirements.txt
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Copying .env.example to .env..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys before using the app!"
    echo "Run: nano .env"
    echo ""
    read -p "Press Enter to continue anyway (for testing) or Ctrl+C to exit..."
fi

# Test AI connections
echo ""
echo "🔍 Testing AI connections..."
python tools/ai_client.py test
if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  AI connection test failed. Please check your .env file."
    echo "The app will still start, but document generation may not work."
    echo ""
    read -p "Press Enter to continue or Ctrl+C to exit..."
fi

# Get Tailscale IP
echo ""
echo "📡 Network information:"
echo "  Local: http://localhost:8501"
if command -v tailscale &> /dev/null; then
    TAILSCALE_IP=$(tailscale ip -4 2>/dev/null)
    if [ -n "$TAILSCALE_IP" ]; then
        echo "  Tailscale: http://$TAILSCALE_IP:8501"
        echo ""
        echo "💡 Bookmark the Tailscale URL on your phone for mobile access!"
    fi
fi

echo ""
echo "🚀 Launching Streamlit app..."
echo "Press Ctrl+C to stop the server"
echo ""
echo "═══════════════════════════════════════════════════════════"

# Start Streamlit
streamlit run app.py
