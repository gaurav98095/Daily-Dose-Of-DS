from crewai import Task, Agent, Crew


def validate_summary_length(task_output):
    try:
        print("Validating summary length")
        task_str_output = str(task_output)
        total_words = len(task_str_output.split())

        print(f"Word count: {total_words}")

        if total_words > 150:
            print("Summary exceeds 150 words")
            return (
                False,
                f"""Summary exceeds 150 words.
            Current Word count: {total_words}""",
            )

        if total_words == 0:
            print("Summary is empty")
            return (False, "Generated summary is empty.")

        print("Summary is valid")
        return (True, task_output)

    except Exception as e:
        print("Validation system error")
        return (False, f"Validation system error: {str(e)}")


summary_agent = Agent(
    role="Summary Agent",
    goal="Summarize a ML topic in 150 words",
    backstory="You specialize in summarizing ML topics.",
    verbose=True,
)

summary_task = Task(
    description="Summarize a ML topic in 150 words.",
    expected_output="""A summary of CNNs in 150 words""",
    agent=summary_agent,
    guardrail=validate_summary_length,  # <-- Guardrail function is added here
)

my_crew = Crew(agents=[summary_agent], tasks=[summary_task])
result = my_crew.kickoff()
