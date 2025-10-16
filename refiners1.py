from sentient_agent_framework import AbstractAgent
from fireworks.client import Fireworks

# Set Fireworks API key directly
fireworks.client.api_key = "fw_3ZLxtjL6n2h3JhX7de6xP8Wk"  # Your key

class IdeaRefiner(AbstractAgent):
    def __init__(self):
        super().__init__(name="IdeaRefiner")
        self.client = Fireworks()

    def assist(self, user_input):
        prompt = f"Refine this idea: '{user_input}'. Suggest 3 specific improvements."
        try:
            response = self.client.chat.completions.create(
                model="accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}. Check internet or API key."

# Run the agent with a loop for multiple inputs
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