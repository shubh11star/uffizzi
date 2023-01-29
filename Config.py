import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20137765"))
    API_HASH = os.environ.get("API_HASH", "461d1c1a84566a810b38145947b29e83")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1BVtsOHMBuzj8E_Ztjd9fjWlDLUAtyv2NWewire3mRxJKar0VcTz3bqFJvJYNLAL6bj_auLCX7XEVMcqoN5S5yUcPu31y5AQGXVoWdVy4ASATdLu7PloTYYiP4tqgqk9OLindBIiYHFLY-QGtpNKq6KV8GZCc7A87f9_HV2t5KgZzDb8RFtZkHGiPumD2RRMfewmjoPiCrborPCiXzHGh_QTwcJfH__VulteXSLQk1uAtqm67luEUWNY9bmZ3jj8MvsuxbKckdf3jisvTqGftRB6FekH03B_-ySNrIzfKJHdJIgyGpAetcy3RmNGypvlEBRWgkVAbg-6bP0XQl746LiFFl8f9P0g=
")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5691601913")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True ) # Change it to "True"
