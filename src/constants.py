import os
from dotenv import load_dotenv

load_dotenv()

# Path constants
SPT_SERVER_HOST = os.environ.get("SPT_SERVER_HOST", "localhost")
SPT_SERVER_PORT = os.environ.get("SPT_SERVER_HOST", 6969)
SPT_PROFILES_URL = f"http://{SPT_SERVER_HOST}:{SPT_SERVER_PORT}/launcher/profile/list"
FIKA_PLAYERS_URL = f"http://{SPT_SERVER_HOST}:{SPT_SERVER_PORT}/fika/players"  # Fika's player status endpoint

# connection constants
SPT_SERVER_TIMEOUT = os.environ.get("SPT_SERVER_TIMEOUT", 2)