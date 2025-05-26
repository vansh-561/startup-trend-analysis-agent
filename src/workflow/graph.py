"""Workflow graph for startup analysis using LangGraph."""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from .state import StartupAnalysisState
from ..agents.news_collector_agent import NewsCollectorAgent
from ..agents.market_analyzer_agent import MarketAnalyzerAgent
from ..agents.investment_analyzer_agent import InvestmentAnalyzerAgent
from ..agents.competitive_analyzer_agent import CompetitiveAnalyzerAgent
from ..agents.report_generator_agent import ReportGeneratorAgent

def create_startup_analysis_workflow():
    """Create and configure the startup analysis workflow."""
    
    # Initialize agents
    news_collector = NewsCollectorAgent()
    market_analyzer = MarketAnalyzerAgent()
    investment_analyzer = InvestmentAnalyzerAgent()
    competitive_analyzer = CompetitiveAnalyzerAgent()
    report_generator = ReportGeneratorAgent()
    
    # Create workflow
    workflow = StateGraph(StartupAnalysisState)
    
    # Add nodes
    workflow.add_node("news_collector", news_collector.execute)
    workflow.add_node("market_analyzer", market_analyzer.execute)
    workflow.add_node("investment_analyzer", investment_analyzer.execute)
    workflow.add_node("competitive_analyzer", competitive_analyzer.execute)
    workflow.add_node("report_generator", report_generator.execute)
    
    # Add edges
    workflow.set_entry_point("news_collector")
    workflow.add_edge("news_collector", "market_analyzer")
    workflow.add_edge("market_analyzer", "investment_analyzer")
    workflow.add_edge("investment_analyzer", "competitive_analyzer")
    workflow.add_edge("competitive_analyzer", "report_generator")
    workflow.add_edge("report_generator", END)
    
    # Compile the graph
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    return app
