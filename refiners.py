from sentient_agent_framework import AbstractAgent
from fireworks.client import Fireworks
import os
from dotenv import load_dotenv

# Load .env
env_path = os.path.join(os.path.dirname(__file__), ".env")
if not os.path.exists(env_path):
    raise FileNotFoundError(f"No .env file found at {env_path}")
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("FIREWORKS_API_KEY")
if not api_key:
    raise ValueError("FIREWORKS_API_KEY not found")

class IdeaRefiner(AbstractAgent):
    def __init__(self):
        super().__init__(name="IdeaRefiner")
        self.client = Fireworks(api_key=api_key)

    def assist(self, user_input: str) -> str:
        prompt = (
            f"Refine this idea: '{user_input}'. Suggest 3 specific improvements. "
            "Use formal, professional, family-friendly language only."
        )
        try:
            response = self.client.chat.completions.create(
               model="accounts/fireworks/models/llama-v3p1-8b-instruct", # CLEAN model - NO profanity
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    agent = IdeaRefiner()
    print("Welcome to Idea Refiner 2.0! (Clean professional output)")
    while True:
        user_idea = input("Enter your idea (or 'quit' to exit): ").strip()
        if user_idea.lower() == "quit":
            print("Goodbye!")
            break
        if len(user_idea) < 5:
            print("Please enter a valid idea (at least 5 characters).")
            continue
        result = agent.assist(user_idea)
        print("\nRefined Idea:\n", result)