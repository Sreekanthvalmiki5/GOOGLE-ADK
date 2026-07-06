from google.adk.agents import LlmAgent ,ParallelAgent,SequentialAgent
from google.adk.tools import google_search



natural_resource_agent=LlmAgent(
    name="natural_resource_agent",
    instruction="you are a research agent give me the list of the countries based on the given input who are rich in natural resourcesSummarize the information in 2 lines use the google search tools to acheive the same",
    tools=[google_search],
output_key="natural_resource_countries")


gdp_per_capita_agent=LlmAgent(
    name="gdp_per_capita_agent",
    model="gemini-3-flash-preview",
    instruction="Your are a research agent Give me the list of top 5 countries who are having highest gdp per capita use the given search tool",
    tools=[google_search],
    output_key="gdp_per_capita_countries",)


parallel_agent=ParallelAgent(
    name="pipelilne_agent",
sub_agents=[natural_resource_agent,gdp_per_capita_agent]
)    

merger_agent=LlmAgent( 
                      name="merger_agent",
                      model="gemini-3-flash-preview",
                      instructios="""
                        Your are an helpful agent which would help the combining research results from multiple resources
                        
                        *Input Summaries*
                        --Natural Resource Countries :{nature_resource_countries}
                        --GDP Growth Countries:{gdp_growth_countries}
                        
                        
                        **Output Format**
                        ##Summary of the Countries Rich in Natural Resources and GDP Growth
                        -Synthesize the information from the input summarizes and provide a consice overview of the information who are rich in natural resources and gdp per capita growth include key insights and comparisions where relavant
                        
                      """,
                      tools=[google_search]
                      
                    
                      
)

sequential_agent=SequentialAgent(
    name="Research_agent",
    sub_agents=[parallel_agent,merger_agent]
    
)
root_agent=sequential_agent