from google.adk.agents import LlmAgent
from pydantic import BaseModel,Field

class Capital(BaseModel):
    city:str=Field(description="The capital city of the country",example="Washington D.C.")

root_agent=LlmAgent(
    name="basic_agent",
    description="This is a simple agent that can answer questions about a specific topic.",
    instruction="You are a helpful assistant that provides the capital city of country",
    model="gemini-2.5-flash",
    output_schema=Capital,
    output_key="found_capital"
    
)