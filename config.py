import os

# BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# API_ID = int(os.environ.get("API_ID", ""))
# API_HASH = os.environ.get("API_HASH", "")
# LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
# MUST_JOIN = os.environ.get("MUST_JOIN", "@nrbots")
# AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "932498979 5422759678 5399174823 5679956601").split())
# DB_URL = os.environ.get("DB_URL", "")
# DB_NAME = os.environ.get("DB_NAME", "memadder")
# BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
# FORCE_SUBS = bool(os.environ.get("FORCE_SUBSCRIBE", False))
# PORT = os.environ.get("PORT", "8080")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "6502302860:AAHF9hmDi-D1SQTBIcP_rs257wD9A8vGPGk")
API_ID = int(os.environ.get("API_ID", "14185021"))
API_HASH = os.environ.get("API_HASH", "b29b81f8a9f892ff457df8f3372489fc")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002023116661"))
MUST_JOIN = os.environ.get("MUST_JOIN", -1001755915892)
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "932498979 5422759678 5399174823 5679956601 1854384004 2008540176").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://nora:nora@nora.f0ea0ix.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "memadder")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
FORCE_SUBS = bool(os.environ.get("FORCE_SUBSCRIBE", False))
PORT = os.environ.get("PORT", "8080")