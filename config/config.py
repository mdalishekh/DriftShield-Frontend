import os
from dotenv import load_dotenv

load_dotenv()

class ENV:
    BASE_URL = os.getenv("BASE_URL")
    