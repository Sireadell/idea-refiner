import requests
try:
    response = requests.get("https://huggingface.co", timeout=10)
    print("Connection successful:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Connection error:", e)