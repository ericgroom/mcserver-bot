import os
from dotenv import load_dotenv
load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")