"""Sidebar component for user inputs."""

import streamlit as st
from config.settings import settings

def render_sidebar():
    """Render the sidebar with input controls."""
    with st.sidebar:
        st.header("🚀 Startup Analysis")
        
        # Input fields
        user_topic = st.text_input(
            "Startup Topic/Technology:", 
            placeholder="e.g., AI healthcare, fintech"
        )
        
        user_sector = st.selectbox(
            "Industry Sector:", 
            settings.INDUSTRY_SECTORS
        )
        
        analysis_type = st.multiselect(
            "Analysis Focus:", 
            settings.ANALYSIS_TYPES,
            default=["Market Trends", "Investment Patterns"]
        )
        
        start_button = st.button(
            "🔍 Analyze Startup Trends", 
            type="primary",
            disabled=not (user_topic and user_sector)
        )
        
        st.divider()
        st.subheader("💡 Example Topics")
        
        for topic, sector in settings.EXAMPLE_TOPICS:
            if st.button(f"{topic} ({sector})", key=f"ex_{topic}"):
                user_topic = topic
                user_sector = sector
                start_button = True
        
        st.divider()
        st.info("💡 **Required API Keys:**\n- GOOGLE_API_KEY\n- TAVILY_API_KEY")
        
        return user_topic, user_sector, analysis_type, start_button
