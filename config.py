import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME", "AI Video Factory")
    APP_ENV = os.getenv("APP_ENV", "development")

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
