#!/usr/bin/env python3
"""
Swoop Service Auto - Service Documentation Web Interface
Interactive web app for generating and managing automotive service documentation
"""

import streamlit as st
import sys
from pathlib import Path
import json
import pandas as pd
from datetime import datetime
import time

# Configure page BEFORE any other Streamlit commands
st.set_page_config(
    page_title="Swoop Service Auto - Service Documentation",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent / "tools"))

# Import after page config to avoid import issues
try:
    from service_doc_generator import ServiceDocGenerator
except ImportError as e:
    st.error(f"❌ Failed to import ServiceDocGenerator: {e}")
    st.stop()

# Custom CSS for professional look with mobile responsiveness
st.markdown("""
<style>
    /* Mobile-first responsive design */
    .main-header {
        background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%);
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Responsive header text */
    @media (min-width: 768px) {
        .main-header {
            padding: 20px;
            margin-bottom: 30px;
        }
    }
    
    .stButton>button {
        width: 100%;
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 12px 10px;
        font-size: 14px;
        min-height: 44px; /* Minimum touch target for mobile */
    }
    
    @media (min-width: 768px) {
        .stButton>button {
            padding: 10px;
        }
    }
    
    .stButton>button:hover {
        background-color: #0d47a1;
    }
    
    .info-box {
        background-color: #e3f2fd;
        color: #1a237e;
        padding: 12px;
        border-radius: 5px;
        border-left: 4px solid #1a73e8;
        margin-bottom: 10px;
        font-size: 14px;
    }
    
    @media (min-width: 768px) {
        .info-box {
            padding: 15px;
        }
    }
    
    .success-box {
        background-color: #e8f5e9;
        padding: 12px;
        border-radius: 5px;
        border-left: 4px solid #34a853;
        font-size: 14px;
    }
    
    @media (min-width: 768px) {
        .success-box {
            padding: 15px;
        }
    }
    
    .warning-box {
        background-color: #fff3e0;
        padding: 12px;
        border-radius: 5px;
        border-left: 4px solid #fbbc04;
        font-size: 14px;
    }
    
    @media (min-width: 768px) {
        .warning-box {
            padding: 15px;
        }
    }
    
    .stat-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 10px;
    }
    
    @media (min-width: 768px) {
        .stat-card {
            padding: 20px;
        }
    }
    
    .stat-value {
        font-size: 24px;
        font-weight: bold;
        color: #1a73e8;
    }
    
    @media (min-width: 768px) {
        .stat-value {
            font-size: 32px;
        }
    }
    
    .stat-label {
        font-size: 12px;
        color: #666;
        margin-top: 5px;
    }
    
    @media (min-width: 768px) {
        .stat-label {
            font-size: 14px;
        }
    }
    
    /* Fix for chat messages visibility - improved contrast */
    .stChatMessage {
        background-color: #ffffff !important;
        border: 2px solid #d0d0d0 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        margin-bottom: 10px !important;
        color: #1a1a1a !important;
        font-size: 14px !important;
    }
    
    @media (min-width: 768px) {
        .stChatMessage {
            padding: 14px !important;
            margin-bottom: 12px !important;
        }
    }
    
    .stChatMessage[data-testid="user-message"] {
        background-color: #e3f2fd !important;
        border: 2px solid #1a73e8 !important;
        border-left: 5px solid #1a73e8 !important;
        color: #1a237e !important;
    }
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #e8f5e9 !important;
        border: 2px solid #34a853 !important;
        border-left: 5px solid #34a853 !important;
        color: #1b5e20 !important;
    }
    /* Ensure all chat message content is visible with proper contrast */
    .stChatMessage p, .stChatMessage div, .stChatMessage span, .stChatMessage li {
        color: inherit !important;
    }
    /* User message text */
    [data-testid="user-message"] p {
        color: #0d47a1 !important;
        font-weight: 500 !important;
    }
    /* Assistant message text */
    [data-testid="assistant-message"] p {
        color: #1b5e20 !important;
        font-weight: 400 !important;
    }
    /* Chat input styling */
    .stChatInput {
        border: 2px solid #1a73e8 !important;
        border-radius: 8px !important;
    }
    
    /* Mobile-friendly selectbox and input fields */
    .stSelectbox, .stTextInput, .stNumberInput {
        font-size: 16px !important; /* Prevents zoom on iOS */
    }
    
    /* Better mobile sidebar */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            width: 85vw !important;
        }
        
        /* Sidebar content padding */
        [data-testid="stSidebar"] > div:first-child {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    
    /* Mobile-friendly tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        overflow-x: auto;
        white-space: nowrap;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 10px 12px;
        font-size: 14px;
    }
    
    /* Improve touch targets for mobile */
    @media (max-width: 768px) {
        .stRadio > label, .stCheckbox > label {
            min-height: 44px;
            display: flex;
            align-items: center;
        }
    }
    
    /* Better mobile table display */
    @media (max-width: 768px) {
        .dataframe {
            font-size: 12px;
            overflow-x: auto;
        }
    }
    
    /* Fix expander for mobile */
    .streamlit-expanderHeader {
        font-size: 14px;
        padding: 10px;
    }
    
    /* Viewport meta improvements */
    html {
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generator' not in st.session_state:
    st.session_state.generator = None
if 'last_doc' not in st.session_state:
    st.session_state.last_doc = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'show_preview_doc' not in st.session_state:
    st.session_state.show_preview_doc = False
if 'show_preview' not in st.session_state:
    st.session_state.show_preview = None
if 'delete_confirm' not in st.session_state:
    st.session_state.delete_confirm = None

# Initialize generator with diagram generation toggle
@st.cache_resource
def get_generator(enable_diagrams=False):
    """Get or create service doc generator with diagram support"""
    return ServiceDocGenerator(enable_diagrams=enable_diagrams)

def main():
    # Header
    st.markdown("""
        <div class="main-header">
            <h1>🔧 Swoop Service Auto</h1>
            <p>Professional Automotive Service Documentation System</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("### 🔧 Swoop Service Auto")
        st.markdown("---")
        
        page = st.radio(
            "Navigation",
            ["🔍 Generate Service Doc", "📚 Browse Cache", "💬 AI Assistant", "📊 Statistics", "⚙️ Settings"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick stats in sidebar
        try:
            gen = get_generator()
            # Reload cache index to show current count
            gen.cache_index = gen._load_cache_index()
            st.markdown("### 📊 Quick Stats")
            st.metric("🚗 Vehicles in DB", f"{len(gen.vehicles):,}")
            st.metric("🔧 Services Available", f"{len(gen.services):,}")
            st.metric("📄 Cached Documents", f"{len(gen.cache_index):,}")
        except Exception as e:
            st.error(f"Error loading generator: {e}")
    
    # Main content based on page selection
    if page == "🔍 Generate Service Doc":
        generate_service_doc_page()
    elif page == "📚 Browse Cache":
        browse_cache_page()
    elif page == "💬 AI Assistant":
        ai_assistant_page()
    elif page == "📊 Statistics":
        statistics_page()
    elif page == "⚙️ Settings":
        settings_page()

def generate_service_doc_page():
    """Page for generating service documentation"""
    st.header("🔍 Generate Service Documentation")
    
    try:
        gen = get_generator()
        
        # Create three columns for input
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("1️⃣ Select Vehicle")
            
            # Get unique makes
            makes = sorted(list(set([v['make'] for v in gen.vehicles])))
            selected_make = st.selectbox("Make", [""] + makes, key="make_select")
            
            if selected_make:
                # Filter models by make
                models = sorted(list(set([
                    v['model'].split('(')[0].strip() 
                    for v in gen.vehicles 
                    if v['make'] == selected_make
                ])))
                selected_model = st.selectbox("Model", [""] + models, key="model_select")
                
                if selected_model:
                    # Filter years by make and model
                    years = []
                    for v in gen.vehicles:
                        if v['make'] == selected_make and selected_model in v['model']:
                            years.extend(v['years'])
                    years = sorted(list(set(years)), reverse=True)
                    selected_year = st.selectbox("Year", [""] + years, key="year_select")
                else:
                    selected_year = None
            else:
                selected_model = None
                selected_year = None
        
        with col2:
            st.subheader("2️⃣ Vehicle Details")
            
            if selected_make and selected_model and selected_year:
                # Find vehicle in database
                vehicle = None
                for v in gen.vehicles:
                    if (v['make'] == selected_make and 
                        selected_model in v['model'] and 
                        selected_year in v['years']):
                        vehicle = v
                        break
                
                if vehicle:
                    st.markdown(f"**Model:** {vehicle['model']}")
                    
                    if vehicle.get('engines'):
                        engine_choice = st.selectbox("Engine", vehicle['engines'], key="engine_select")
                    
                    if vehicle.get('transmissions'):
                        trans_choice = st.selectbox("Transmission", vehicle['transmissions'], key="trans_select")
                    
                    st.markdown(f"**Body Styles:** {', '.join(vehicle.get('body_styles', ['N/A']))}")
                    st.markdown(f"**Drivetrain:** {', '.join(vehicle.get('drivetrain', ['N/A']))}")
                    
                    if vehicle.get('difficulty_modifier', 1.0) > 1.0:
                        st.warning(f"⚠️ Complexity: {vehicle['difficulty_modifier']}x (above standard)")
                    else:
                        st.success(f"✅ Complexity: {vehicle['difficulty_modifier']}x (standard)")
                else:
                    st.error("Vehicle not found in database")
            else:
                st.info("👈 Select make, model, and year first")
        
        with col3:
            st.subheader("3️⃣ Select Service")
            
            # Helper function to get service name (handles both schemas)
            def get_service_name(s):
                return s.get('service_name') or s.get('name', 'Unknown')
            
            # Group services by category
            categories = sorted(list(set([s['category'] for s in gen.services])))
            selected_category = st.selectbox("Category", ["All"] + categories, key="category_select")
            
            # Filter services
            if selected_category == "All":
                services = gen.services
            else:
                services = [s for s in gen.services if s['category'] == selected_category]
            
            service_names = sorted([get_service_name(s) for s in services])
            selected_service = st.selectbox("Service", [""] + service_names, key="service_select")
            
            if selected_service:
                service = next((s for s in gen.services if get_service_name(s) == selected_service), None)
                if service:
                    labor = service.get('labor_time_hours') or service.get('est_labor_hours', 0)
                    st.markdown(f"**Labor:** {labor} hrs")
                    
                    if 'price_range_labor' in service:
                        st.markdown(f"**Cost:** ${service['price_range_labor'][0]}-${service['price_range_labor'][1]}")
                    elif 'labor_rate_local' in service:
                        st.markdown(f"**Rate:** ${service['labor_rate_local']}/hr")
                    
                    if service.get('mobile') or service.get('can_do_mobile'):
                        st.success("✅ Mobile service available")
        
        # Generation options
        st.markdown("---")
        col_opt1, col_opt2, col_opt3 = st.columns(3)
        
        with col_opt1:
            force_regen = st.checkbox("Force regenerate (don't use cache)", value=False)
        
        with col_opt2:
            enable_diagrams = st.checkbox("🎨 Generate AI diagrams", value=False, 
                                         help="Generate technical diagrams using AI (requires API key, costs ~$0.005/diagram)")
        
        with col_opt3:
            if st.session_state.last_doc:
                if st.button("📄 View Last Doc"):
                    st.session_state.show_last = True
        
        # Generate button
        st.markdown("---")
        
        if selected_make and selected_model and selected_year and selected_service:
            col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
            with col_btn2:
                if st.button("⚡ Generate Service Documentation", type="primary", use_container_width=True):
                    generate_documentation(gen, selected_year, selected_make, selected_model, 
                                         selected_service, force_regen, enable_diagrams)
        else:
            st.warning("⚠️ Please complete all selections above to generate documentation")
        
        # Show last generated document if exists
        if st.session_state.get('show_last') and st.session_state.last_doc:
            display_document(st.session_state.last_doc)
    
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.exception(e)

def generate_documentation(gen, year, make, model, service, force_regen, enable_diagrams=False):
    """Generate service documentation with optional diagram generation"""
    
    # If diagrams are requested, recreate generator with diagrams enabled
    if enable_diagrams:
        with st.spinner("🎨 Initializing diagram generator..."):
            try:
                gen = ServiceDocGenerator(enable_diagrams=True)
                st.info("✅ Diagram generation enabled")
            except Exception as e:
                st.warning(f"⚠️ Could not enable diagrams: {e}")
                enable_diagrams = False
    
    with st.spinner(f"🔍 Generating documentation for {year} {make} {model} - {service}..."):
        try:
            start_time = time.time()
            doc_path, from_cache = gen.generate(
                year=year,
                make=make,
                model=model,
                service=service,
                force_regenerate=force_regen
            )
            elapsed = time.time() - start_time
            
            st.session_state.last_doc = {
                'path': doc_path,
                'from_cache': from_cache,
                'year': year,
                'make': make,
                'model': model,
                'service': service,
                'generated_at': datetime.now(),
                'elapsed_time': elapsed
            }
            st.session_state.show_last = True
            
            if from_cache:
                st.success(f"✅ Retrieved from cache in {elapsed:.2f}s")
            else:
                st.success(f"✨ Generated new documentation in {elapsed:.1f}s")
            
            st.rerun()
        
        except Exception as e:
            st.error(f"❌ Generation failed: {e}")
            st.exception(e)

def display_document(doc_info):
    """Display generated document"""
    st.markdown("---")
    st.subheader("📄 Generated Document")
    
    # Document info
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"**Vehicle:** {doc_info['year']} {doc_info['make']} {doc_info['model']}")
    with col2:
        st.markdown(f"**Service:** {doc_info['service']}")
    with col3:
        status = "📋 From Cache" if doc_info['from_cache'] else "✨ Newly Generated"
        st.markdown(f"**Status:** {status}")
    with col4:
        st.markdown(f"**Time:** {doc_info['elapsed_time']:.2f}s")
    
    # Read HTML content once
    with open(doc_info['path'], 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Action buttons
    col_act1, col_act2, col_act3 = st.columns(3)
    
    with col_act1:
        if st.button("👁️ Preview Document", use_container_width=True):
            st.session_state.show_preview_doc = True
    
    with col_act2:
        # Download button
        filename = f"{doc_info['year']}_{doc_info['make']}_{doc_info['model']}_{doc_info['service']}.html".replace(' ', '_')
        st.download_button(
            label="⬇️ Download HTML",
            data=html_content.encode(),
            file_name=filename,
            mime="text/html",
            use_container_width=True
        )
    
    with col_act3:
        if st.button("📱 Open in Browser", use_container_width=True):
            import webbrowser
            import os
            # Get absolute path
            abs_path = os.path.abspath(doc_info['path'])
            # Open in default browser
            webbrowser.open(f"file://{abs_path}", new=2)
            st.success("✅ Opened in browser")
    
    # Show preview if button was clicked - OUTSIDE of columns for full width
    if st.session_state.get('show_preview_doc', False):
        st.markdown("---")
        st.subheader("📄 Document Preview")
        st.components.v1.html(html_content, height=1200, scrolling=True)

def browse_cache_page():
    """Page for browsing cached documents"""
    st.header("📚 Browse Cached Documents")
    
    try:
        gen = get_generator()
        
        # Reload cache index to ensure we have latest
        gen.cache_index = gen._load_cache_index()
        
        if not gen.cache_index:
            st.warning("No cached documents yet. Generate some documentation first!")
            return
        
        # Convert cache index to DataFrame
        cache_data = []
        for key, doc in gen.cache_index.items():
            # Verify file still exists before adding to list
            doc_path = Path(doc.get('path', ''))
            
            # Handle both absolute and relative paths
            if not doc_path.is_absolute():
                # Convert relative path to absolute using project root
                project_root = Path(__file__).parent
                doc_path = project_root / doc_path
            
            if doc_path.exists():
                cache_data.append({
                    'Year': doc.get('year'),
                    'Make': doc.get('make'),
                    'Model': doc.get('model'),
                    'Service': doc.get('service'),
                    'Generated': doc.get('generated', 'Unknown'),
                    'Difficulty': doc.get('vehicle_difficulty', 1.0),
                    'Path': str(doc_path)  # Store absolute path for display
                })
        
        if not cache_data:
            st.warning("No cached documents found. Generate some documentation first!")
            return
        
        df = pd.DataFrame(cache_data)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            makes = ['All'] + sorted(df['Make'].unique().tolist())
            filter_make = st.selectbox("Filter by Make", makes)
        
        with col2:
            services = ['All'] + sorted(df['Service'].unique().tolist())
            filter_service = st.selectbox("Filter by Service", services)
        
        with col3:
            st.metric("Total Cached", len(df))
        
        # Apply filters
        if filter_make != 'All':
            df = df[df['Make'] == filter_make]
        if filter_service != 'All':
            df = df[df['Service'] == filter_service]
        
        # Display table
        st.dataframe(
            df[['Year', 'Make', 'Model', 'Service', 'Generated', 'Difficulty']],
            use_container_width=True,
            hide_index=True
        )
        
        # Selection for viewing
        if len(df) > 0:
            st.markdown("---")
            selected_idx = st.selectbox(
                "Select a document to view",
                range(len(df)),
                format_func=lambda i: f"{df.iloc[i]['Year']} {df.iloc[i]['Make']} {df.iloc[i]['Model']} - {df.iloc[i]['Service']}"
            )
            
            col_btn1, col_btn2 = st.columns([1, 1])
            
            with col_btn1:
                if st.button("👁️ View Selected Document", use_container_width=True):
                    st.session_state.show_preview = selected_idx
            
            with col_btn2:
                if st.button("🗑️ Delete Selected Document", type="secondary", use_container_width=True):
                    st.session_state.delete_confirm = selected_idx
            
            # Show preview if button was clicked - OUTSIDE columns for full width
            if st.session_state.get('show_preview') == selected_idx:
                st.markdown("---")
                st.subheader("📄 Document Preview")
                selected_row = df.iloc[selected_idx]
                doc_path = Path(selected_row['Path'])
                
                if doc_path.exists():
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                    # Full width preview with larger height
                    st.components.v1.html(html_content, height=1200, scrolling=True)
                else:
                    st.error("❌ Document file not found. The file may have been deleted manually.")
                    # Clean up cache index
                    for key, doc in list(gen.cache_index.items()):
                        if doc.get('path') == str(doc_path):
                            del gen.cache_index[key]
                            gen._save_cache_index()
                            break
            
            # Delete confirmation dialog
            if st.session_state.get('delete_confirm') == selected_idx:
                selected_row = df.iloc[selected_idx]
                st.markdown("---")
                st.warning(f"⚠️ **Are you sure you want to delete:**\n\n{selected_row['Year']} {selected_row['Make']} {selected_row['Model']} - {selected_row['Service']}")
                
                col_yes, col_no = st.columns(2)
                with col_yes:
                    if st.button("✅ Yes, Delete", type="primary", use_container_width=True):
                        doc_path = Path(selected_row['Path'])
                        try:
                            if doc_path.exists():
                                doc_path.unlink()
                            # Find and remove from cache index
                            for key, doc in list(gen.cache_index.items()):
                                if doc.get('path') == str(doc_path):
                                    del gen.cache_index[key]
                                    break
                            gen._save_cache_index()
                            st.success("✅ Document deleted successfully!")
                            st.session_state.delete_confirm = None
                            st.session_state.show_preview = None
                            st.cache_resource.clear()  # Clear cache to reload generator
                            time.sleep(0.5)
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error deleting document: {e}")
                
                with col_no:
                    if st.button("❌ Cancel", use_container_width=True):
                        st.session_state.delete_confirm = None
                        st.rerun()
    
    except Exception as e:
        st.error(f"Error: {e}")
        st.exception(e)

def ai_assistant_page():
    """Interactive AI assistant for service questions"""
    st.header("💬 AI Service Assistant")
    
    st.markdown("""
        <div class="info-box">
            <b>💡 How to use:</b><br>
            Ask questions about specific vehicles and services. The AI will provide detailed answers
            and can update your service documentation with new information.
        </div>
    """, unsafe_allow_html=True)
    
    # Chat interface
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for msg in st.session_state.chat_history:
        if msg['role'] == 'user':
            st.chat_message("user").write(msg['content'])
        else:
            st.chat_message("assistant").write(msg['content'])
    
    # Chat input
    user_input = st.chat_input("Ask a question about vehicle service...")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # Generate response
        try:
            gen = get_generator()
            
            # Build context from last document if available
            context = ""
            if st.session_state.last_doc:
                context = f"\nContext: Current document is for {st.session_state.last_doc['year']} {st.session_state.last_doc['make']} {st.session_state.last_doc['model']} - {st.session_state.last_doc['service']}"
            
            prompt = f"{user_input}{context}"
            
            with st.spinner("Thinking..."):
                response = gen.research_ai.chat(
                    prompt,
                    system_message="You are an expert automotive technician. Provide detailed, accurate answers about vehicle service and repair."
                )
            
            # Add assistant response to history
            st.session_state.chat_history.append({
                'role': 'assistant',
                'content': response
            })
            
            st.rerun()
        
        except Exception as e:
            st.error(f"Error: {e}")

def statistics_page():
    """Statistics and analytics page"""
    st.header("📊 System Statistics")
    
    try:
        gen = get_generator()
        
        # Top stats
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
                <div class="stat-card">
                    <div class="stat-value">{:,}</div>
                    <div class="stat-label">Vehicles in Database</div>
                </div>
            """.format(len(gen.vehicles)), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="stat-card">
                    <div class="stat-value">{}</div>
                    <div class="stat-label">Services Available</div>
                </div>
            """.format(len(gen.services)), unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div class="stat-card">
                    <div class="stat-value">{}</div>
                    <div class="stat-label">Cached Documents</div>
                </div>
            """.format(len(gen.cache_index)), unsafe_allow_html=True)
        
        with col4:
            makes = len(set([v['make'] for v in gen.vehicles]))
            st.markdown("""
                <div class="stat-card">
                    <div class="stat-value">{}</div>
                    <div class="stat-label">Manufacturers</div>
                </div>
            """.format(makes), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Charts
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.subheader("Top 10 Manufacturers by Vehicle Count")
            make_counts = {}
            for v in gen.vehicles:
                make = v['make']
                make_counts[make] = make_counts.get(make, 0) + 1
            
            top_makes = dict(sorted(make_counts.items(), key=lambda x: x[1], reverse=True)[:10])
            st.bar_chart(top_makes)
        
        with col_chart2:
            st.subheader("Services by Category")
            category_counts = {}
            for s in gen.services:
                cat = s['category']
                category_counts[cat] = category_counts.get(cat, 0) + 1
            
            st.bar_chart(category_counts)
        
        # Cache statistics
        if gen.cache_index:
            st.markdown("---")
            st.subheader("📋 Cache Statistics")
            
            col_cache1, col_cache2 = st.columns(2)
            
            with col_cache1:
                st.markdown("**Most Cached Makes:**")
                make_cache = {}
                for doc in gen.cache_index.values():
                    make = doc.get('make', 'Unknown')
                    make_cache[make] = make_cache.get(make, 0) + 1
                
                for make, count in sorted(make_cache.items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"- {make}: {count} documents")
            
            with col_cache2:
                st.markdown("**Most Cached Services:**")
                service_cache = {}
                for doc in gen.cache_index.values():
                    service = doc.get('service', 'Unknown')
                    service_cache[service] = service_cache.get(service, 0) + 1
                
                for service, count in sorted(service_cache.items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"- {service}: {count} documents")
    
    except Exception as e:
        st.error(f"Error: {e}")
        st.exception(e)

def settings_page():
    """Settings and configuration page"""
    st.header("⚙️ Settings")
    
    # What's New section
    with st.expander("✨ What's New - January 17, 2025", expanded=True):
        st.markdown("""
        ### Recent Improvements
        
        ✅ **Better HTML Styling**
        - More professional appearance with rounded corners
        - Improved readability and contrast
        - Sleeker design appropriate for mechanics
        
        ✅ **Cache Deletion Feature**
        - Delete cached documents from Browse Cache page
        - Confirmation dialog to prevent accidents
        
        ✅ **AI Diagram Support**
        - Together AI integration ready (~$0.005/diagram)
        - Technical diagrams embedded in service docs
        - Optional feature - enable per generation
        
        📖 See `IMPROVEMENTS_COMPLETED.md` for full details
        """)
    
    st.markdown("---")
    
    try:
        gen = get_generator()
        
        # AI Configuration
        st.subheader("🤖 AI Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Research AI**")
            st.info(f"Provider: {gen.research_ai.provider}")
            st.info(f"Model: {gen.research_ai.model}")
            st.info(f"Temperature: {gen.research_ai.temperature}")
            st.info(f"Max Tokens: {gen.research_ai.max_tokens}")
        
        with col2:
            st.markdown("**Formatter AI**")
            st.info(f"Provider: {gen.formatter_ai.provider}")
            st.info(f"Model: {gen.formatter_ai.model}")
            st.info(f"Temperature: {gen.formatter_ai.temperature}")
            st.info(f"Max Tokens: {gen.formatter_ai.max_tokens}")
        
        st.markdown("---")
        
        # Database paths
        st.subheader("📁 Database Paths")
        st.text(f"Vehicles DB: {gen.vehicles_db}")
        st.text(f"Services DB: {gen.services_db}")
        st.text(f"Cache Directory: {gen.cache_dir}")
        
        st.markdown("---")
        
        # Cache management
        st.subheader("🗄️ Cache Management")
        
        col_cache1, col_cache2, col_cache3 = st.columns(3)
        
        with col_cache1:
            st.metric("Cached Documents", len(gen.cache_index))
        
        with col_cache2:
            # Estimate cache size
            cache_size_mb = sum(
                Path(doc['path']).stat().st_size 
                for doc in gen.cache_index.values() 
                if Path(doc['path']).exists()
            ) / (1024 * 1024)
            st.metric("Cache Size", f"{cache_size_mb:.1f} MB")
        
        with col_cache3:
            if st.button("🔄 Refresh Cache Index"):
                st.rerun()
        
        st.markdown("---")
        
        # System info
        st.subheader("ℹ️ System Information")
        st.text(f"Python: {sys.version.split()[0]}")
        st.text(f"Streamlit: {st.__version__}")
        st.text(f"Working Directory: {Path.cwd()}")
    
    except Exception as e:
        st.error(f"Error: {e}")
        st.exception(e)

if __name__ == "__main__":
    main()
