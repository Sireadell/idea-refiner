from sentient_agent_framework import AbstractAgent
from huggingface_hub import InferenceClient
import os

# Set your Hugging Face API key
os.environ["HF_TOKEN"] = "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"

class IdeaRefiner(AbstractAgent):
    def __init__(self):
        super().__init__(name="IdeaRefiner")
        self.client = InferenceClient(model="tiiuae/falcon-7b-instruct")

    def assist(self, user_input):
        prompt = f"Refine this idea: '{user_input}'. Suggest 3 specific improvements."
        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat_completion(
                messages=messages,
                max_tokens=200,
                temperature=0.7,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            if "Rate limit" in str(e):
                return "Error: API rate limit exceeded. Wait or upgrade plan."
            return f"Error: {str(e)}. Check internet or token."

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