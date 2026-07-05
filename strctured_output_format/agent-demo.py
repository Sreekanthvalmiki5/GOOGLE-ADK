from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel,Field



APP_NAME="basic_agent_no_web"
USER_ID="USER1738"
SESSION_ID="SESSION1738"

class Capital(BaseModel):
    city:str=Field(description="The capital city of the country",example="Washington D.C.")

async def get_agent():
    root_agent = LlmAgent(
        name="First_Agent",
        description="This is a simple agent that can answer questions about a specific topic.",
        instruction="You are a helpful assistant that can answer questions about a specific topic. Please provide clear and concise answers to the user's questions.",
        model="gemini-2.5-flash",
        output_schema=Capital,
        output_key="found_capital"
    )
    return root_agent

async def main(query):
    #create memory session
    session_service=InMemorySessionService()
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    root_agent=await get_agent()
    runner=Runner(session_service=session_service,agent=root_agent, app_name=APP_NAME)
    content=types.Content(role="user",parts=[types.Part(text=query)])
    events=runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
        
    )
    #print response
    async for event in events:
        if event.is_final_response():
            final_response=event.content.parts[0].text
            print(final_response)
            
    current_session=await session_service.get_session(app_name=APP_NAME,user_id=USER_ID,session_id=SESSION_ID)
    stored_output=current_session.state.get("found_capital")
    print("Stored Output:",stored_output) 
            
            
            
if __name__=="__main__":
    asyncio.run(main("What is the Capital of Italy?"))
    
    
    