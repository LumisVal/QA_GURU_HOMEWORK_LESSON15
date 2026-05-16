import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")