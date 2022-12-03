import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", ""))
      API_HASH = os.environ.get("API_HASH")
      FORCE_SUB = os.environ.get("FORCE_SUB", "") 
      FLOOD = int(os.environ.get("FLOOD", "10"))
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Sreehari3")
      PORT = os.environ.get("PORT", "8080")
