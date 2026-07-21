from google.adk.agents import LlmAgent ,ParallelAgent,SequentialAgent
from google.adk.tools import google_search

from google.adk.agents.callback_context import CallbackContext

natural_resource_agent=LlmAgent(
    name="natural_resource_agent",
    instruction="you are a research agent give me the list of the countries based on the given input who are rich in natural resourcesSummarize the information in 2 lines use the google search tools to acheive the same",
    
     model="openai/openai/gpt-oss-120b",
output_key="natural_resource_countries")


gdp_per_capita_agent=LlmAgent(
    name="gdp_per_capita_agent",
    model="openai/openai/gpt-oss-120b",
    instruction="Your are a research agent Give me the list of top 5 countries who are having highest gdp per capita use the given search tool",
 
    output_key="gdp_per_capita_countries",)


parallel_agent=ParallelAgent(
    name="pipelilne_agent",
sub_agents=[natural_resource_agent,gdp_per_capita_agent]
)    


                     
                      
                    
                      


def merger_instruction(context: CallbackContext) -> str:
    natural = context.state.get("natural_resource_countries", "No data")
    gdp = context.state.get("gdp_per_capita_countries", "No data")

    return f"""
You are a helpful research assistant.

Natural Resource Countries:
{natural}

GDP Per Capita Countries:
{gdp}

Combine the above information and provide:

1. Countries rich in natural resources
2. Countries with highest GDP per capita
3. Common countries
4. Final summary
"""
merger_agent = LlmAgent(
    name="merger_agent",
    model="openai/openai/gpt-oss-120b",
    instruction=merger_instruction,
    output_key="final_summary"
)
sequential_agent=SequentialAgent(
    name="Research_agent",
    sub_agents=[parallel_agent,merger_agent]
    
)
root_agent = sequential_agent