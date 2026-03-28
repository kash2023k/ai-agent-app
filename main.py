from crewai import Crew
from tasks import research_task, writing_task

crew = Crew(
    agents=[research_task.agent, writing_task.agent],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff()

print("\n=== FINAL OUTPUT ===\n")
print(result)