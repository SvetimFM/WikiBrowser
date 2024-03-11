from .apikey import OPEN_AI_API_KEY, ANTHROPIC_API_KEY
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_anthropic import ChatAnthropic
from app_logic.constants import OPEN_AI, ANTHROPIC, GPT3, OPUS


def get_llm(llm_type: str, temp: float = 0.0):
    print(f"apiKey: {ANTHROPIC_API_KEY}")
    print(f"apiKey: {OPEN_AI_API_KEY}")
    if llm_type == "openai":
        return OpenAI(model_name=GPT3, temperature=temp, openai_api_key=OPEN_AI_API_KEY)
    if llm_type == "anthropic":
        return ChatAnthropic(temperature=0, anthropic_api_key=ANTHROPIC_API_KEY, model_name=OPUS)
    raise ValueError("Invalid LLM type")
    # __Tool Reference__
    # Inputs:
    # The name of the tool
    # A description of what the tool is
    # JSON schema of what the inputs to the tool are
    # The function to call
    # Whether the result of a tool should be returned directly to the user


def init_decision_agent(llm):
    tools = load_tools(['wikipedia', 'llm-math'], llm)
    agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent


def agent_execute(user_input: str, llm: str = OPEN_AI):
    llm_object = get_llm(llm)
    agent = init_decision_agent(llm_object)
    return agent.run(user_input)


def convert_select_llm(llm: str):
    if llm == 'OpenAI GPT3':
        return OPEN_AI
    else:
        return ANTHROPIC