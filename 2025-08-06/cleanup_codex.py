from cleanlab_codex.client import Client
from cleanlab_codex.project import Project

# Create Project
codex_client = Client()
project = codex_client.create_project(name="RAG")
project = Project.from_access_key(access_key)

# Your existing code (RAG pipeline)
context = rag_retrieve_context(user_query)
messages = rag_form_prompt(user_query, context)
response = rag_generate_response(messages)

# Validated results
results = project.validate(
    messages=messages,
    query=user_query,
    context=context,
    response=response
)
