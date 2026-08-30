import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "openrouter:openai/gpt-4o-mini"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")