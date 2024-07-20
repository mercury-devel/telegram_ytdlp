from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
channel_id = int(os.getenv('CHANNEL_ID'))
channel_link = os.getenv('CHANNEL_LINK')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
admin_list = list(os.getenv('ADMIN_LIST'))
