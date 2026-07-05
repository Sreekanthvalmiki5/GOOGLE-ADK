from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv
load_dotenv()
import requests
from google.adk.tools.agent_tool import AgentTool





summary_agent=LlmAgent(
    name="Summary_Agent",
    description="This is a simple agent that can answer questions about a specific topic.",
    instruction="You are a helpful this summrize the text",
    model="gemini-2.5-flash",
)
                           
root_agent = LlmAgent(
        name="root_Agent",
        description="This is a simple agent that can answer questions about a specific topic.",
        instruction="You are a helpful assistant Summarizing the given text Please use the given Summarize tool to get the summary of the Text",
        tools=[AgentTool(agent=summary_agent, name="Summarize", description="This tool is used to summarize the given text")],
    )
  