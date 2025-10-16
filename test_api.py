import traceback
from huggingface_hub import InferenceClient

client = InferenceClient(model="gpt2", token="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", timeout=30)
try:
    print("Sending test request to Hugging Face API...")
    response = client.text_generation("Test prompt", max_new_tokens=50)
    print("API Response:", response)
except Exception as e:
    print("API Error:", str(e))
    print("Full stack trace:")
    traceback.print_exc()