"""Utility functions for the startup analysis agent."""

import json
from datetime import datetime
from typing import Dict, Any

def create_analysis_data(topic: str, sector: str, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
    """Create structured analysis data for export."""
    return {
        "topic": topic,
        "sector": sector,
        "timestamp": datetime.now().isoformat(),
        "report": analysis_results.get("final_report", ""),
        "market_data": analysis_results.get("market_data", {}),
        "opportunities": analysis_results.get("opportunities", [])
    }

def generate_filename(topic: str, extension: str = "md") -> str:
    """Generate filename for report downloads."""
    clean_topic = topic.replace(' ', '_').replace('/', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    return f"startup_analysis_{clean_topic}_{timestamp}.{extension}"

def format_json_export(data: Dict[str, Any]) -> str:
    """Format data for JSON export."""
    return json.dumps(data, indent=2)
