"""Configuration settings for the AI Startup Trend Analysis Agent."""

import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings."""
    
    # API Keys
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    
    # Model Configuration
    MODEL_NAME: str = "gemini-2.0-flash"
    MODEL_TEMPERATURE: float = 0.3
    MODEL_MAX_TOKENS: int = 800
    
    # Search Configuration
    MAX_SEARCH_RESULTS: int = 3
    SEARCH_DEPTH: str = "advanced"
    
    # Industry Sectors
    INDUSTRY_SECTORS: List[str] = [
        "Healthcare", "Fintech", "EdTech", "E-commerce", "SaaS",
        "AI/ML", "Blockchain", "IoT", "Cybersecurity", "GreenTech"
    ]
    
    # Analysis Types
    ANALYSIS_TYPES: List[str] = [
        "Market Trends", "Investment Patterns", "Competitive Analysis",
        "Technology Adoption", "Regulatory Impact"
    ]
    
    # Example Topics
    EXAMPLE_TOPICS: List[tuple] = [
        ("AI-powered diagnostics", "Healthcare"),
        ("DeFi lending platforms", "Fintech"),
        ("VR learning platforms", "EdTech"),
        ("Sustainable packaging", "GreenTech"),
        ("No-code platforms", "SaaS")
    ]

settings = Settings()
