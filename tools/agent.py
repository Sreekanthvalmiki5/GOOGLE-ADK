from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv
load_dotenv()
import requests





def get_weather_info(city:str)->str :
    
    endpoint="https://wttr.in"
    response=requests.post(f"{endpoint}/{city}?m")
    return response.text
                           
root_agent = LlmAgent(
        name="First_Agent",
        description="This is a simple agent that can answer questions about a specific topic.",
        instruction="You are a helpful assistant that can answer questions about a specific topic. Please provide clear and concise answers to the user's questions.",
        model="gemini-2.5-flash",
        tools=[get_weather_info]
    )
  