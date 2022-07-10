
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_ID, CHANNELS, ADMINS
from pyrogram import Client, filters
from utils import main_convertor_handler, extract_link
from database import db
# Channel

@Client.on_message(~filters.forwarded & filters.chat(CHANNEL_ID) & (
				filters.channel | filters.group) & filters.incoming & ~filters.private &
		~filters.forwarded)
async def channel_link_handler(c:Client, message):
	bot = await c.get_me()
	user_method = await db.get_bot_method(bot.username)

	if CHANNELS is True or CHANNELS == "True":
		try:
			if user_method is None:
				for chat_id in ADMINS:
					await c.send_message(chat_id=chat_id, text="Set your /method first")
				return
			await main_convertor_handler(message, user_method, True)
		except Exception as e:
			print(e)