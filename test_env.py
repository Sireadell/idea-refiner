import os
from dotenv import load_dotenv

# Force load .env from current folder
env_path = os.path.join(os.path.dirname(__file__), ".env")
loaded = load_dotenv(dotenv_path=env_path, override=True)

print(f".env loaded: {loaded}")
print(f"FIREWORKS_API_KEY: {os.getenv('FIREWORKS_API_KEY')}")
