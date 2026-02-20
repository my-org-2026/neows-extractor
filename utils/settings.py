
from dotenv import load_dotenv
from utils.helper import access_secret
import os

load_dotenv()

class Settings:
    PROJECT_ID = os.getenv("PROJECT_ID")
    API_KEY = access_secret(PROJECT_ID, "NASA_API_KEY")
    API_BASE_URL = os.getenv("NASA_BASE_URL")
    ASTEROIDS_BUCKET = os.getenv("ASTEROIDS_BUCKET")


settings = Settings()