from sentient_agent_framework import AbstractAgent
from fireworks.client import Fireworks
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FIREWORKS_API_KEY")
if not api_key:
    raise ValueError("Missing API key")

class IdeaRefiner(AbstractAgent):
    def __init__(self):
        super().__init__(name="IdeaRefiner")
        self.client = Fireworks(api_key=api_key)

    def assist(self, idea):
        prompt = f"Give 3 short, practical ways to improve '{idea}':\n1.\n2.\n3."
        
        resp = self.client.chat.completions.create(
            model="accounts/fireworks/models/llama-v3p1-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.9
        )
        return resp.choices[0].message.content

if __name__ == "__main__":
    agent = IdeaRefiner()
    print("Idea Refiner")
    
    while True:
        idea = input("Idea (quit to exit): ").strip()
        if idea.lower() == 'quit':
            break
        if len(idea) < 2:
            print("Too short")
            continue
        print(f"\n{agent.assist(idea)}\n")