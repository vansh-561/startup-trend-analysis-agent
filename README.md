# 🚀 AI Startup Trend Analysis Agent

A comprehensive AI-powered tool for analyzing startup trends, market opportunities, and investment patterns using Google Gemini 2.0 Flash, Tavily Search, and LangGraph.

## 🌟 Features

- **Multi-Agent Analysis**: Specialized agents for news collection, market analysis, investment patterns, and competitive intelligence
- **Real-time Data**: Live startup news and market data collection using Tavily Search
- **Comprehensive Reports**: Detailed analysis reports with actionable insights
- **Interactive UI**: User-friendly Streamlit interface with multiple analysis views
- **Export Capabilities**: Download reports in Markdown and JSON formats

## 📋 Prerequisites

- Python 3.13+
- Poetry (Python package manager)
- Google Cloud API key for Gemini 2.0 Flash
- Tavily Search API key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/vansh-561/ai-startup-trend-analysis-agent.git
cd ai-startup-trend-analysis-agent
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```
![Screenshot (113)](https://github.com/user-attachments/assets/0eda4da3-27d7-4e91-94c2-c2e651217afa)
![Screenshot (111)](https://github.com/user-attachments/assets/663d244d-e85c-4ddc-8811-a5198e220461)
![Screenshot (112)](https://github.com/user-attachments/assets/b438b795-74f4-43e6-8107-a1bf7504ba91)

## 🚀 Usage

1. Start the application:
```bash
poetry run python main.py
```

2. Access the Streamlit interface at `http://localhost:8501`

3. Use the interface to:
   - Configure analysis parameters
   - Select target markets or industries
   - Generate trend analysis reports
   - Export results in various formats

## 📊 Example Analysis

The tool can analyze various aspects of startup ecosystems:
- Market trends and opportunities
- Investment patterns and funding rounds
- Competitive landscape analysis
- Emerging technology adoption
- Regional startup ecosystem comparisons


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini 2.0 Flash for AI capabilities
- Tavily Search for real-time data collection
- LangGraph for multi-agent orchestration
- Streamlit for the interactive UI framework
