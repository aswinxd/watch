class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "21443796"
    API_HASH = "34633377a9ece9883cbc43bc894c61d""

    CASH_API_KEY = "NA11YFJ9ED9HBFH9"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "something://cxyzdtck:c8wbJ2AJs2Gu2aqo6M8Xy2A8iJ7h9AJV@floppy.db.elephantsql.com/cxyzdtck"

    EVENT_LOGS = " -1002102374866"  # Event logs channel to note down important bot level
    MONGO_DB_URI = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"  # Get ths value from cloud.mong
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/7298939991d9f7e46c904.jpg"

    SUPPORT_CHAT = "X1Botchat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "854520103:AAF4VoneEumanUkCjJke6UN_T63dLR03tiQ"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "YDNAVZ2G1KUL"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "6419116622"  # User id of your telegram account (Must be integer)

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
