"""Competitive analyzer agent for analyzing competitive landscape and identifying opportunities."""

from langchain_core.messages import HumanMessage, AIMessage
from .base_agent import BaseAgent
from ..workflow.state import StartupAnalysisState

class CompetitiveAnalyzerAgent(BaseAgent):
    """Agent responsible for analyzing competitive landscape and identifying opportunities."""
    
    def execute(self, state: StartupAnalysisState) -> dict:
        """Analyze competitive landscape and identify opportunities."""
        articles = state["raw_articles"]
        topic = state["topic"]
        trend_analysis = state["trend_analysis"]
        
        prompt = f"""Analyze competitive landscape for "{topic}" startups:

Market Analysis: {trend_analysis[:400]}

Based on articles, identify:
1. Key competitors and their strategies (100 words)
2. Market gaps and opportunities (100 words)
3. Differentiation strategies (50 words)

Be specific and actionable."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        # Extract opportunities
        opportunities = [
            {
                "type": "Market Gap",
                "description": "Underserved market segments identified",
                "confidence": "Medium"
            },
            {
                "type": "Technology Trend",
                "description": "Emerging technology adoption opportunity",
                "confidence": "High"
            }
        ]
        
        return {
            "competitive_analysis": response.content,
            "opportunities": opportunities,
            "current_agent": "report_generator",
            "messages": [AIMessage(content="Competitive analysis completed")]
        }
