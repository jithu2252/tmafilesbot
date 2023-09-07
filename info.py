import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 9301845 #int(environ['API_ID'],5540967)
API_HASH = '563e9fd30b529442b705c7230f766b83'#(environ['API_HASH'],'eedf0196b0533f361b51b5b7082358e9')
BOT_TOKEN = '' #(environ['BOT_TOKEN'],'1877486792:AAGr4aoWtD_31Qh9GGnMnV2kUNYPqSxQSkY')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/b6f42af4d20b757b46d73.jpg https://telegra.ph/file/f514edecba0f6c1ef3418.jpg https://telegra.ph//file/797fcafb53479875e2bc7.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1952992043 1713177274 5299424797 5348874903 5421706941 5673274527').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', " -1001201699325 -1001511163820 -1001435020763 -1001438293617 -1001556008450 -1001291060083 -1001465431548 -1001227500379 -1001543949874 -1001558654003 -1001438293617 -1001479888204 -1001610031839 -1001435020763 -1001636626174 -1001445318928 -1001625705075 -1001274297517 -1001374485034 -1001625705075 -1001722756764 -1001543052371 -1001651078319").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1086048529 1242169194 18025669102 895955663 5388296061 2117090309 1665818466 1094503092 832312885 1902119538 1478286558 5348483742 1880167885 1848232918 909693392 837573929 1267798585 1225990769 1779025877 5213335284 5148112772').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL','-1001860674667')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1001601961451").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Tmamoviesbottt")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001694472922'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Tmadiscuss')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_caption} \n Size :- <i>{file_size}</i> \n Join [TMAAdda](https://telegram.me/tmaadda)</b> ")
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_caption} \n Size :- <i>{file_size}</i> \n Join [TMAAdda](https://telegram.me/tmaadda)</b> ")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "Hey {message.from_user.mention}, \n Here is the result for your {query} \n <b>🏷 Title</b>: <a href={url}>{title}</a> \n 📆 Year: <a href={url}/releaseinfo>{year}</a> \n 🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.) \n ☀️ Languages : <code>{languages}</code> \n 📀 RunTime: {runtime} Minutes \n 📆 Release Info : {release_date} \n 🎛 Countries : <code>{countries}</code> \n \n Requested by : {message.from_user.mention} \n Powered By @TMAAdda")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
