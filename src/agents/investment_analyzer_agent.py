"""Investment analyzer agent for analyzing investment patterns and funding trends."""

from langchain_core.messages import HumanMessage, AIMessage
from .base_agent import BaseAgent
from ..workflow.state import StartupAnalysisState

class InvestmentAnalyzerAgent(BaseAgent):
    """Agent responsible for analyzing investment patterns and funding trends."""
    
    def execute(self, state: StartupAnalysisState) -> dict:
        """Analyze investment patterns and funding trends."""
        articles = state["raw_articles"]
        topic = state["topic"]
        
        # Focus on funding-related content
        funding_content = ""
        for article in articles:
            if any(keyword in article['content'].lower() for keyword in ['funding', 'investment', 'round', 'valuation', 'vc']):
                funding_content += f"{article['title']}: {article['content']}\n\n"
        
        prompt = f"""Analyze investment patterns for "{topic}" startups:

{funding_content[:800]}

Provide 150-word analysis covering:
1. Recent funding rounds and amounts
2. Active investor types
3. Valuation trends
4. Investment stage preferences

Focus on actionable insights."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        return {
            "investment_patterns": response.content,
            "current_agent": "competitive_analyzer",
            "messages": [AIMessage(content="Investment patterns analyzed")]
        }
