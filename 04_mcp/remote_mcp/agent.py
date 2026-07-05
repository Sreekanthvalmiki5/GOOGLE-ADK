from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv
load_dotenv()
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams, StdioConnectionParams

APP_NAME="MCP CUSTOM AGENT"
USER_ID="USER1738"
SESSION_ID="SESSION1738"

def get_agent():
    tool_set = MCPToolset(connection_params=StreamableHTTPConnectionParams(
       url="http://localhost:8000/mcp"
    ))
    root_agent=LlmAgent(
        name="Custom_mcp_Agent",
        description="This is a simple agent that can answer questions about a specific topic.",
        instruction="You are a helpful assistant that can answer questions about a specific topic. Please provide clear and concise answers to the user's questions.",
        model="gemini-2.5-flash",
        tools=[tool_set]
        
    )
    return root_agent,tool_set

async def main(query):
    session_service = InMemorySessionService()
    root_agent, tool_set = get_agent()
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(session_service=session_service, agent=root_agent, app_name=APP_NAME)
    content = types.Content(role="user", parts=[types.Part(text=query)])

    try:
        events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)
        async for event in events:
            print(event)
            if event.is_final_response():
                final_response = event.content.parts[0].text
                print(final_response)
    finally:
        await tool_set.close()
            

if __name__=="__main__":
    asyncio.run(main("How is the Whether in Hyderbad can i go to outside now?"))
            