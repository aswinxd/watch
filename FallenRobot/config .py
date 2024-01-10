class Config(object):
    LOGGER = True
    
    # Get this value from my.telegram.org/apps
    API_ID = "27589257"
    API_HASH = "0af78b04b48361bc117fa4e06d6d2292"
    
    CASH_API_KEY = "NA11YFJ9ED9HBFH9"# Get this value for currencyconverter from https://www.alphavantage.co/support/#api-key
    
    DATABASE_URL = "postgresql://cloz9otou0057aupa5ylaak3i:rzs8NEdPLs2iFwV4eLbmJUyg@104.251.217.208:9001/cloz9otov0059aupaa9aqhvwt"
    EVENT_LOGS = "-1002049466903"  # Event logs channel to note dowimportant bot level
    MONGO_DB_URI = "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mong
    
    # Telegraph link of the image which will be shown at start commans
    START_IMG = "https://te.legra.ph/file/c5fc1c8df4c776e14c061.mp4"
    SUPPORT_CHAT = "SUbotsupport"  # Your Telegram support group chatsername where your users will go and bother you
    
    TOKEN = "2119246346:AAGLiG8RRlbP3rifH__22R--VBBO_kDvbA4"  # Get bot token from @BotFather on Telegram
    TIME_API_KEY = "YDNAVZ2G1KUL"  # Get this value from https://timezonedb.com/api
    OWNER_ID = "1137799257"  # User id of your telegram account (Mustbe integer)
    # Optional fields
    
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
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
