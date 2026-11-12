import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FinSight AI")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
# os.getenv() returns strings, not Python Booleans. That's why the comparison is necessary
DEBUG = os.getenv("DEBUG", "False").lower() == "true"