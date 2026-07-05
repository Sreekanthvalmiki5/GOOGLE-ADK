from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="First_Agent",
    description="This is a simple agent that can answer questions about a specific topic.",
    instruction="You are a helpful assistant that can answer questions about a specific topic. Please provide clear and concise answers to the user's questions.",
    model="gemini-2.5-flash",
)