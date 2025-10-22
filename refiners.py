from sentient_agent_framework import AbstractAgent
from fireworks.client import Fireworks
import os
from dotenv import load_dotenv

# 
# Load .env properly
# 
env_path = os.path.join(os.path.dirname(__file__), ".env")

if not os.path.exists(env_path):
    raise FileNotFoundError(f"No .env file found at {env_path}. Please create one with FIREWORKS_API_KEY.")

# Force load .env and override any existing env variables
loaded = load_dotenv(dotenv_path=env_path, override=True)


# Debug: print FIREWORKS_API_KEY to confirm it's loaded
api_key_debug = os.getenv("FIREWORKS_API_KEY")


if not api_key_debug:
    raise ValueError("FIREWORKS_API_KEY not found in environment variables after loading .env.")

# ----------------------
# Idea Refiner Class
# ----------------------
class IdeaRefiner(AbstractAgent):
    def __init__(self):
        super().__init__(name="IdeaRefiner")
        api_key = os.getenv("FIREWORKS_API_KEY")
        if not api_key:
            raise ValueError("FIREWORKS_API_KEY not found in environment variables.")
        self.client = Fireworks(api_key=api_key)

    def assist(self, user_input):
        prompt = (
            f"Refine this idea: '{user_input}'. Suggest 3 specific improvements. "
            "Use family-friendly, professional language suitable for all audiences."
        )
        try:
            response = self.client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3-8b-instruct",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}. Check internet or API key."

# ----------------------
# Run Loop
# ----------------------
if __name__ == "__main__":
    agent = IdeaRefiner()
    print("Welcome to Idea Refiner 2.0!")
    while True:
        user_idea = input("Enter your idea (or 'quit' to exit): ")
        if user_idea.lower() == 'quit':
            print("Goodbye!")
            break
        if not user_idea.strip() or len(user_idea) < 5:
            print("Please enter a valid idea (at least 5 characters).")
            continue
        result = agent.assist(user_idea)
        print("Refined Idea:\n", result)
