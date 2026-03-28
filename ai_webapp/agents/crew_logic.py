from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

def run_ai_task(user_input):

    search_tool = SerperDevTool()

    # ✅ FIXED: use named argument
    search_results = search_tool.run(search_query=user_input)

    agent = Agent(
        role="AI Assistant",
        goal="Answer using latest internet data",
        backstory="Helpful assistant",
        llm="ollama/llama3",
        verbose=True
    )

    task = Task(
        description=f"""
        Use this latest information:
        {search_results}

        Answer the question:
        {user_input}
        """,
        agent=agent,
        expected_output="Bullet points with spacing"
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    return crew.kickoff()