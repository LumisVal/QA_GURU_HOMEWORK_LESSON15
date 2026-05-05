import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
SELENOID_URL = os.getenv("SELENOID_URL")
BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
BROWSER_NAME = os.getenv("BROWSER_NAME", "chrome")
BROWSER_VERSION = os.getenv("BROWSER_VERSION", "")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920x1080")