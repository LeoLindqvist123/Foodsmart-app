import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "google/gemini-2.5-pro"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")