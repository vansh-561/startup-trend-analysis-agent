"""Market data tab component for displaying market analysis data."""

import streamlit as st

def render_market_data_tab():
    """Render the market data tab."""
    if st.session_state.analysis_results.get("market_data"):
        market_data = st.session_state.analysis_results["market_data"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sector", market_data.get("sector", "N/A"))
            st.metric("Articles Analyzed", market_data.get("articles_analyzed", 0))
        
        with col2:
            st.metric("Analysis Date", market_data.get("analysis_date", "N/A")[:10])
        
        if st.session_state.analysis_results.get("raw_articles"):
            st.subheader("📰 Source Articles")
            for i, article in enumerate(st.session_state.analysis_results["raw_articles"], 1):
                with st.expander(f"Article {i}: {article['title'][:50]}..."):
                    st.write(f"**URL:** {article['url']}")
                    st.write(f"**Query:** {article['query']}")
                    st.write(f"**Content:** {article['content'][:300]}...")
    
    elif not st.session_state.analysis_complete:
        st.info("👆 Start an analysis to see market data here")
