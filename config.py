from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/7605e4861576cc8f74973.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/da4b1dd77f18c5aedca91.jpg")
SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TKS_CHAT_OFFICIAL")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TKS_CHAT_OFFICIAL")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5686536025").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
