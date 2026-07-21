from google.adk.agents import LlmAgent
from google.adk.agents import LoopAgent,SequentialAgent

basic_agent=LlmAgent(
    name="BasicArchagent",
    model="openai/openai/gpt-oss-120b",
    instruction="Your are an Ai agent Specialized with the Software Architecture. you will come up with the System Design architecture for given scenario",
    output_key="basic_arch_output"
    
)
critique_design_agent=LlmAgent(
    name="critique_agent",
    model="openai/openai/gpt-oss-120b",
    instruction="""Your are critique agent Specialized in the Software Architecture Design You need to critique the Provided  design and Suggest Improvement for Scalability and maintanance
    
    **Input** 
    {basic_arch_output}
    
    """,
    output_key="critique_output"
    
)
refine_desing_agent=LlmAgent(
    name="refine_agent",
    model="openai/openai/gpt-oss-120b",
    instruction="""you are an agent Specialized in refining the given architecture design if the design is good,you should return the design with the pharse
    
    "The design is good else, you need to refine the provided design based on the critique and suggeste the improvement for scalability and maintainability and performance  
    ** Input**
    {basic_arch_output}
    {critique_output}
    
    
    "
    """,
)

loop_agent=LoopAgent(
        name="loop_agent",
        sub_agents=[critique_design_agent,refine_desing_agent],
        max_iterations=3,
        
)

root_agent=SequentialAgent(
    name="sequential_agent",
    sub_agents=[basic_agent,loop_agent]
)