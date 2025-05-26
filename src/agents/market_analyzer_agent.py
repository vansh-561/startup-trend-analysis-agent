"""Market analyzer agent for analyzing market trends and patterns."""

from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from .base_agent import BaseAgent
from ..workflow.state import StartupAnalysisState

class MarketAnalyzerAgent(BaseAgent):
    """Agent responsible for analyzing market trends and patterns."""
    
    def execute(self, state: StartupAnalysisState) -> dict:
        """Analyze market trends and patterns."""
        articles = state["raw_articles"]
        topic = state["topic"]
        sector = state["sector"]
        
        # Combine article content
        combined_content = ""
        for article in articles[:6]:
            combined_content += f"Title: {article['title']}\nContent: {article['content']}\n\n"
        
        prompt = f"""Analyze startup market trends for "{topic}" in "{sector}" sector:

{combined_content[:1000]}

Provide 300-word analysis covering:
1. Market size and growth indicators
2. Key technology trends
3. Investment activity patterns
4. Regulatory factors

Be data-focused and specific."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        # Extract market data
        market_data = {
            "sector": sector,
            "topic": topic,
            "analysis_date": datetime.now().isoformat(),
            "articles_analyzed": len(articles),
            "key_trends": response.content
        }
        
        return {
            "market_data": market_data,
            "trend_analysis": response.content,
            "current_agent": "investment_analyzer",
            "messages": [AIMessage(content="Market trends analyzed")]
        }
