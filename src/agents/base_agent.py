"""Base agent class for all startup analysis agents."""

from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings

class BaseAgent(ABC):
    """Base class for all agents in the startup analysis workflow."""
    
    def __init__(self):
        """Initialize the base agent."""
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            temperature=settings.MODEL_TEMPERATURE,
            max_tokens=settings.MODEL_MAX_TOKENS
        )
    
    @abstractmethod
    def execute(self, state: dict) -> dict:
        """Execute the agent's functionality."""
        pass
