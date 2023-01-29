import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6045885769:AAFl957b4VpLDiqB_rd_kQSKVTkPNKiBu9g")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIMBu7sDNA-fhGeiWLC4dJpVZSuhXbG6YVNO2CHDF8UYjb0hdL9DH5EDY-7qzZT9zvfbXSrYub6WGwC99M5CMfYFJ2BHyTReqS3x03Hu5D0lclL1lRB52ljIhtu6Efk2UzJDX3qzEgwP3QR16uEcNwQbe-a3u9kmWL_tRkwOv5Zwo1EFuy3KLuiq2nwVRtBNCctm_Xv_eode3iOdNRNzaXGyWeQUcUpsvE8vBVbf86NMDACkrtIGUOycpiYdCkZMIOWRtH3kYpYNiqdgh7LECS0D5vzH1TDcSC0pct1L25NbBR2EzSpInGvBSMiajgThT81QQzl_oC8tjhzOZmhoIZdVecU=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Shubh_assistant2_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5691601913")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
