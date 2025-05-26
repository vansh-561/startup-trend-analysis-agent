"""Analysis process tab component."""

import streamlit as st
from src.workflow.graph import create_startup_analysis_workflow

def render_analysis_tab(user_topic: str, user_sector: str, start_button: bool):
    """Render the analysis process tab."""
    if start_button and user_topic and user_sector:
        # Reset session state
        st.session_state.analysis_results = {}
        st.session_state.analysis_complete = False
        
        st.write(f"🔍 **Analyzing:** {user_topic} in {user_sector} sector")
        
        # Create workflow
        app = create_startup_analysis_workflow()
        
        # Initial state
        initial_state = {
            "messages": [],
            "topic": user_topic,
            "sector": user_sector,
            "search_queries": [],
            "raw_articles": [],
            "market_data": {},
            "trend_analysis": "",
            "competitive_analysis": "",
            "investment_patterns": "",
            "opportunities": [],
            "final_report": "",
            "current_agent": "news_collector"
        }
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Run the workflow
            config = {"configurable": {"thread_id": "startup_analysis"}}
            
            step = 0
            for state in app.stream(initial_state, config):
                step += 1
                current_state = list(state.values())[0]
                
                # Update progress
                progress = min(step * 20, 100)
                progress_bar.progress(progress)
                
                # Update status
                agent = current_state.get("current_agent", "unknown")
                status_text.write(f"**Current Step:** {agent.replace('_', ' ').title()}")
                
                # Store results
                st.session_state.analysis_results = current_state
                
                if current_state.get("final_report"):
                    st.session_state.analysis_complete = True
            
            progress_bar.progress(100)
            status_text.write("✅ **Analysis Complete!**")
            
        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")
            st.info("This might be due to API rate limits. Try again in a moment.")
