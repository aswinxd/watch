class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "27589257"
    API_HASH = "0af78b04b48361bc117fa4e06d6d2292"

    CASH_API_KEY = "NA11YFJ9ED9HBFH9"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://cloz9otou0057aupa5ylaak3i:rzs8NEdPLs2iFwV4eLbmJUyg@104.251.217.208:9001/cloz9otov0059aupaa9aqhvwt"

    EVENT_LOGS = "-1001535538162"  # Event logs channel to note down important bot level
    MONGO_DB_URI = "mongodb+srv://filetolink:DWPEfBYWs4y1ricL@filetolink.xgmsac5.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mong
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/7298939991d9f7e46c904.jpg"

    SUPPORT_CHAT = "onmywaylo"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "1711796263:AAGqLyPusqxENy0VHceY2vOVCbWWxdP8-SQ"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "YDNAVZ2G1KUL"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "1137799257"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = [6756452709]  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = False
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
