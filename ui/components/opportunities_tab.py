"""Opportunities tab component for displaying identified opportunities."""

import streamlit as st

def render_opportunities_tab():
    """Render the opportunities tab."""
    if st.session_state.analysis_results.get("opportunities"):
        st.subheader("🎯 Identified Opportunities")
        
        for i, opp in enumerate(st.session_state.analysis_results["opportunities"], 1):
            with st.container():
                st.write(f"**{i}. {opp.get('type', 'Opportunity')}**")
                st.write(opp.get('description', 'No description available'))
                st.write(f"*Confidence: {opp.get('confidence', 'Unknown')}*")
                st.divider()
    
    elif not st.session_state.analysis_complete:
        st.info("👆 Start an analysis to see opportunities here")
