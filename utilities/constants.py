import os
from dotenv import load_dotenv

_ = load_dotenv()

MODEL_NAME = "gemini-1.5-pro-exp-0827"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
