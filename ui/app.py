"""Main Streamlit application."""

import streamlit as st
from config.settings import settings
from .components.sidebar import render_sidebar
from .components.analysis_tab import render_analysis_tab
from .components.report_tab import render_report_tab
from .components.market_data_tab import render_market_data_tab
from .components.opportunities_tab import render_opportunities_tab

def check_api_keys():
    """Check if required API keys are available."""
    if not settings.GOOGLE_API_KEY:
        st.error("Please set your GOOGLE_API_KEY environment variable")
        st.stop()
    
    if not settings.TAVILY_API_KEY:
        st.error("Please set your TAVILY_API_KEY environment variable")
        st.stop()

def initialize_session_state():
    """Initialize Streamlit session state."""
    if "analysis_results" not in st.session_state:
        st.session_state.analysis_results = {}
    if "analysis_complete" not in st.session_state:
        st.session_state.analysis_complete = False

def render_header():
    """Render the application header."""
    st.title("🚀 AI Startup Trend Analysis Agent")
    st.subheader("Powered by Google Gemini 2.0 Flash, Tavily Search & LangGraph")
    st.markdown("**Discover emerging startup opportunities, market trends, and investment patterns**")

def render_footer():
    """Render the application footer."""
    st.markdown("---")
    st.markdown("Built with 🚀 Google Gemini 2.0 Flash, 🌐 Tavily Search, 🦜 LangChain, 📊 LangGraph, and 🎨 Streamlit")

def main():
    """Main application function."""
    # Page configuration
    st.set_page_config(
        page_title="🚀 AI Startup Trend Analysis Agent",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Check API keys
    check_api_keys()
    
    # Initialize session state
    initialize_session_state()
    
    # Render header
    render_header()
    
    # Render sidebar and get inputs
    user_topic, user_sector, analysis_type, start_button = render_sidebar()
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Analysis Process", 
        "📄 Final Report", 
        "📊 Market Data", 
        "💡 Opportunities"
    ])
    
    # Render tabs
    with tab1:
        render_analysis_tab(user_topic, user_sector, start_button)
    
    with tab2:
        render_report_tab(user_topic, user_sector)
    
    with tab3:
        render_market_data_tab()
    
    with tab4:
        render_opportunities_tab()
    
    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
