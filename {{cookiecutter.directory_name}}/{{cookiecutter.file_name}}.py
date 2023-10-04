from langchain.llms import OpenAIChat
from swarms.agents import OmniModalAgent


llm = OpenAIChat(model_name="gpt-3.5")

agent = OmniModalAgent(llm)

agent.run("{{cookiecutter.starting_prompt}}")
