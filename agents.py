from crewai import Agent
from langchain_community.llms import Ollama

llm = "ollama/llama3"

research_agent = Agent(
    role="Research Analyst",
    goal="Find accurate and relevant information",
    backstory="Expert in analyzing and summarizing data",
    llm=llm,
    verbose=True
)

writer_agent = Agent(
    role="Content Writer",
    goal="Write clear and engaging content",
    backstory="Professional writer skilled in storytelling",
    llm=llm,
    verbose=True
)