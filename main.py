import Desafio1
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool

@tool("sayHello", return_direct=True)
def say_Hello(name: str) -> str:
    return f"hello {name}! my name is Sainapsis"

def main():
    llm = chatOpenAI(temperature=0)
    tools = [
        say_Hello
    ]

    agent = initialize_agent(
        tools = tools,
        llm = llm,
        agent = AgentType.OPENAI_FUNCTIONS,
        verbose = True
    )
    print(agent.run("Hello, my name is david "))
    inst = Desafio1
    inst.main()

if __name__ == '__main__':
    main()