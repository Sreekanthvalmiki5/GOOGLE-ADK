from google.adk.agents import LlmAgent,SequentialAgent


capital_agent=LlmAgent(
    name="capital_agent",
    description="This is agent simply returns capital",
    instruction="Your a agent that provides the capital city of a coutry",
    model="gemini-2.0-flash",
    output_key="capital_city"
)

papulation_agent=LlmAgent(
    name="papulation_agent",
    description="This agent returns the papulation of the given {capital_city}",
    model="gemini-2.0-flash",
    
)

root_agent=LlmAgent(
    name="pipeline_agent",
    sub_agents=[capital_agent,papulation_agent],
 
)

