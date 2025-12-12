from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

model = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature= 0.5 #0 - 2
)

ddgs_search = DuckDuckGoSearchRun(
    name='search',
    description='A tool for real time web search'
)

agent = create_agent(
    tools=[ddgs_search],
    model=model,
    system_prompt="""You are a helpful assistant.
            INSTRUCTIONS:
            1. READ the search results provided by the 'search' tool. 
            2. SYNTHESIZE the answer based on those results.
            3. END with a playful animal sound.

            FORMAT EXAMPLE:
            "The weather in the requested city is sunny with 25 degrees.
            Quack!"

            Do not skip step 2. You MUST provide the weather details before the sound.
            """
)

if __name__== 'main':
    answer = agent.invoke(
        {'messages':[
            {"role":"user","content":"Qual o clima em salvador hoje 12/12/2025?"}
        ]})

    print(answer["messages"][-1].content)



