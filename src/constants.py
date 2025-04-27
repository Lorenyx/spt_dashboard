import os
from dotenv import load_dotenv

load_dotenv()

# Path constants
SPT_SERVER = os.environ.get("SPT_SERVER", "https://localhost:6969")

# connection constants
CONNECT_TIMEOUT = int(os.environ.get("SPT_SERVER_TIMEOUT", 2))
