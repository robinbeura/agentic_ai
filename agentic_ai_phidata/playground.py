from phi.agent.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from os import getenv
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app
load_dotenv()
import phi
import os
phi.api = os.getenv("PHI_API_KEY")


webAgent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model = Groq(api_key=getenv('GROQ_API_KEY')),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Financial AI Agent",
    role="Providing financial insights",
    model = Groq(api_key=getenv('GROQ_API_KEY')),
    tools= [YFinanceTools(stock_price=True,stock_fundamentals=True, company_news=True, analyst_recommendations=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[finance_agent, webAgent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)