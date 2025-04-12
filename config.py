import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "26396405"))
API_HASH = environ.get("API_HASH", "26b69972-5578-13c1-32b5-30e363765ba4")
BOT_TOKEN = environ.get("BOT_TOKEN", "7955311254:AAHN9y9pdCvm0aDPI8Loae0Wuy9VcHYc-xc")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "1513994864"))
DB_URI = environ.get("DB_URI", "")) 
DB_NAME = environ.get("DB_NAME", "NITEESH")) 
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
