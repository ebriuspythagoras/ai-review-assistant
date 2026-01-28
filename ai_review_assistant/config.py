import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()

def get_groq_api_key() -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY не знайдено!")
    return api_key

def get_groq_model() -> str:
    model = os.getenv("GROQ_MODEL")
    if not model:
        model = "llama-3.3-70b-versatile"
    return model