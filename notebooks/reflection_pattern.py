"""
Reflection Pattern Agent Notebook

This script demonstrates the use of a ReflectionAgent for iterative code generation and improvement using LLMs.
It loads environment variables, initializes a Groq client, and runs the agent with user and system prompts.
"""

from dotenv import load_dotenv
from groq import Groq
from agentic_patterns import ReflectionAgent

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq()

# Create the ReflectionAgent with a supported model
agent = ReflectionAgent(model="llama3-70b-8192", client=client)

# System and user prompts
generation_system_prompt = "You are a Python programmer tasked with generating high quality Python code"
reflection_system_prompt = "You are Andrej Karpathy, an experienced computer scientist"
user_msg = "Generate a Python implementation of the Merge Sort algorithm"

# Run the agent
final_response = agent.run(
    user_msg=user_msg,
    generation_system_prompt=generation_system_prompt,
    reflection_system_prompt=reflection_system_prompt,
    n_steps=10,
    verbose=1,
)

# Print the final response
print(final_response)
