"""News collector agent for gathering startup news and market data."""

from datetime import datetime
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from .base_agent import BaseAgent
from ..tools.search_tool import create_search_tool
from ..workflow.state import StartupAnalysisState

class NewsCollectorAgent(BaseAgent):
    """Agent responsible for collecting startup news and market data."""
    
    def __init__(self):
        """Initialize the news collector agent."""
        super().__init__()
        self.search_tool = create_search_tool()
    
    def execute(self, state: StartupAnalysisState) -> dict:
        """Collect startup news and market data using Tavily."""
        topic = state["topic"]
        sector = state["sector"]
        
        # Create targeted search queries
        prompt = f"""Create 3 specific search queries for startup analysis in "{topic}" within "{sector}" sector.
        
        Focus on: funding news, market trends, emerging technologies.
        Keep each query under 8 words.
        Format: one query per line."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        queries = [q.strip() for q in response.content.split('\n') if q.strip()][:3]
        
        # Search for articles
        articles = []
        for query in queries:
            try:
                search_results = self.search_tool.invoke({
                    "query": f"{query} startup funding {datetime.now().year}"
                })
                
                if search_results and isinstance(search_results, list):
                    for result in search_results[:2]:
                        if isinstance(result, dict):
                            article = {
                                "title": result.get('title', 'No title'),
                                "url": result.get('url', ''),
                                "content": result.get('content', '')[:400],
                                "query": query,
                                "published_date": result.get('published_date', 'Unknown')
                            }
                            articles.append(article)
                            
            except Exception as e:
                st.error(f"Search error for '{query}': {str(e)}")
        
        return {
            "search_queries": queries,
            "raw_articles": articles,
            "current_agent": "market_analyzer",
            "messages": [AIMessage(content=f"Collected {len(articles)} articles")]
        }
