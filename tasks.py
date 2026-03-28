from crewai import Task
from agents import research_agent, writer_agent

research_task = Task(
    description="Research about 'AI in Banking'",
    agent=research_agent,
    expected_output="Key insights and bullet points"
)

writing_task = Task(
    description="Write a blog based on research findings",
    agent=writer_agent,
    expected_output="A well-structured blog article"
)