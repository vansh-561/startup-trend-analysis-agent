"""Report tab component for displaying final analysis report."""

import streamlit as st
from src.utils.helpers import create_analysis_data, generate_filename, format_json_export

def render_report_tab(user_topic: str, user_sector: str):
    """Render the final report tab."""
    if st.session_state.analysis_complete and st.session_state.analysis_results.get("final_report"):
        st.markdown(st.session_state.analysis_results["final_report"])
        
        # Download button
        report_filename = generate_filename(user_topic, "md")
        st.download_button(
            label="📄 Download Report",
            data=st.session_state.analysis_results["final_report"],
            file_name=report_filename,
            mime="text/markdown"
        )
        
        # JSON export
        analysis_data = create_analysis_data(user_topic, user_sector, st.session_state.analysis_results)
        
        st.download_button(
            label="📊 Download Data (JSON)",
            data=format_json_export(analysis_data),
            file_name=generate_filename(user_topic, "json"),
            mime="application/json"
        )
    
    elif not st.session_state.analysis_complete:
        st.info("👆 Start an analysis from the sidebar to see results here")
    else:
        st.warning("No report available. Please try running the analysis again.")
