# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25836402"))
API_HASH = getenv("API_HASH", "ed15e2112f1efddfa130c1996fca59c3")
BOT_TOKEN = getenv("BOT_TOKEN", "8107999230:AAFaYVaNGdI5yDitqPBckXVm7dXNrATyEWY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5657905693").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://omareyadtoz:safaamohamedelsayed5@series.aya7d.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002440206054")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002440206054"))
