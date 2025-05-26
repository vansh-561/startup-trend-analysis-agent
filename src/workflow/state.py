"""State management for the startup analysis workflow."""

from typing import TypedDict, List, Annotated
import operator

class StartupAnalysisState(TypedDict):
    """State structure for startup analysis workflow."""
    
    messages: Annotated[List, operator.add]
    topic: str
    sector: str
    search_queries: List[str]
    raw_articles: List[dict]
    market_data: dict
    trend_analysis: str
    competitive_analysis: str
    investment_patterns: str
    opportunities: List[dict]
    final_report: str
    current_agent: str
