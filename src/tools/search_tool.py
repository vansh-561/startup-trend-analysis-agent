"""Search tool configuration for Tavily."""

from langchain_community.tools import TavilySearchResults
from config.settings import settings

def create_search_tool() -> TavilySearchResults:
    """Create and configure Tavily search tool."""
    return TavilySearchResults(
        max_results=settings.MAX_SEARCH_RESULTS,
        include_answer=True,
        include_raw_content=False,
        include_images=False,
        search_depth=settings.SEARCH_DEPTH
    )
