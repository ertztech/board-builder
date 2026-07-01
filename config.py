import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_TOKEN")