from data.apikey import OPEN_AI_API_KEY,CLAUDE_API_KEY
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


def get_llm(llm_type: str, llm_name: str = GPT3, temp: float = 0.0):
    if llm_type == "openai":
        return OpenAI(model_name=llm_name, temperature=temp, openai_api_key=OPEN_AI_API_KEY)
    if llm_type == "anthropic":
        return ChatAnthropic(temperature=0, anthropic_api_key=CLAUDE_API_KEY, model_name=llm_name)
    raise ValueError("Invalid LLM type")
    # __Tool Reference__
    # Inputs:
    # The name of the tool
    # A description of what the tool is
    # JSON schema of what the inputs to the tool are
    # The function to call
    # Whether the result of a tool should be returned directly to the user
def init_decision_agent():
    tools = load_tools()
    agent = initialize_agent()
