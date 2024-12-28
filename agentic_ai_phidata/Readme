Project: Web and Financial AI Agents

## Overview
This repository implements a multi-agent system for web searches and financial analysis. It combines the capabilities of individual agents to provide real-time insights and analysis for tasks like stock market evaluation and general web-based research. The agents utilize advanced AI models and specialized tools to deliver precise, up-to-date information in a user-friendly format.

---

## Features
- **Web Search Agent**:
  - Searches the web for information using DuckDuckGo.
  - Ensures results include sources for credibility.
  - Outputs results in Markdown format for readability.

- **Financial AI Agent**:
  - Provides detailed financial insights, including:
    - Stock prices.
    - Stock fundamentals.
    - Company news.
    - Analyst recommendations.
  - Displays data in tables for better visualization.

- **Multi-Agent Collaboration**:
  - Combines web search and financial insights into a single comprehensive agent.
  - Specializes in stock market analysis and integrates financial data with web-based insights.

---

## Code Structure
### Files
- **`phi/agent/agent.py`**:
  - Defines the core Agent class for implementing intelligent agents.
- **`phi/model/groq.py`**:
  - Implements the Groq model used for AI-driven insights.
- **`phi/tools/yfinance.py`**:
  - Provides tools for fetching financial data from Yahoo Finance.
- **`phi/tools/duckduckgo.py`**:
  - Enables web searches using DuckDuckGo.
- **`.env`**:
  - Stores environment variables such as API keys.

---

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install Dependencies**:
   Ensure you have Python installed. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```
4. **Run the Script**:
   Execute the script to test the multi-agent system:
   ```bash
   python main.py
   ```

---

## Usage
The system is designed to answer specific queries, such as combining web search results and financial data. Below is an example command:

```python
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for Nvidia.",
    stream=True
)
```

This command will:
- Fetch real-time financial data and news about Nvidia.
- Display results with proper formatting and sources.

---

## Contributing
We welcome contributions to improve the system's capabilities. Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- **Groq**: For powering the AI model.
- **Yahoo Finance**: For providing financial data.
- **DuckDuckGo**: For enabling web search capabilities.

