# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "13963336")
API_HASH = environ.get("API_HASH" , "a144d1e22ef0b29738e8c00713d02678")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7831423954:AAEk-zDmtqwiyTtodNCZwI2mOVAs_58oM9g")
ADMIN = int(environ.get("ADMIN" , "2103299862"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002440952521"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002421238378")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002465691872")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
