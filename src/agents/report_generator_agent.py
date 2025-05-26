"""Report generator agent for creating comprehensive startup analysis reports."""

from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from .base_agent import BaseAgent
from ..workflow.state import StartupAnalysisState

class ReportGeneratorAgent(BaseAgent):
    """Agent responsible for generating comprehensive startup analysis reports."""
    
    def execute(self, state: StartupAnalysisState) -> dict:
        """Generate comprehensive startup analysis report."""
        topic = state["topic"]
        sector = state["sector"]
        trend_analysis = state["trend_analysis"]
        investment_patterns = state["investment_patterns"]
        competitive_analysis = state["competitive_analysis"]
        articles = state["raw_articles"]
        
        prompt = f"""Create a comprehensive startup analysis report for "{topic}" in "{sector}":

Market Trends: {trend_analysis[:300]}
Investment Patterns: {investment_patterns[:300]}
Competitive Analysis: {competitive_analysis[:300]}

Generate a structured report with:
1. Executive Summary (50 words)
2. Market Opportunity (100 words)
3. Key Recommendations (100 words)
4. Risk Factors (50 words)

Use clear, actionable language for entrepreneurs."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        # Create comprehensive report
        report = f"""# 🚀 Startup Trend Analysis Report: {topic}

**Sector:** {sector}  
**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Articles Analyzed:** {len(articles)}

## 📊 Executive Summary
{response.content}

## 📈 Market Trends
{trend_analysis}

## 💰 Investment Patterns
{investment_patterns}

## 🏆 Competitive Landscape
{competitive_analysis}

## 🔍 Data Sources
"""
        
        for i, article in enumerate(articles[:5], 1):
            report += f"{i}. [{article['title']}]({article['url']})\n"
        
        return {
            "final_report": report,
            "current_agent": "complete",
            "messages": [AIMessage(content="Analysis report generated")]
        }
