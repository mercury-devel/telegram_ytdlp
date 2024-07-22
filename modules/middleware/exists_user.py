# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware
from modules.database import DataBase
from modules.keyboards import sub_kb
import config

db = DataBase()

class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = event.from_user
        user_id = user.id
        user_exists = db.get_user(user_id)
        if not user_exists:
            db.add_user(user_id)
        user_status = await event.bot.get_chat_member(chat_id=config.channel_id, user_id=user.id)
        if user_status.status == "kicked":
            return
        if user_status.status != "left":
            return await handler(event, data)
        else:
            await event.bot.send_message(
                chat_id=user.id,
                text="To activate bot you need to subscribe the channel",
                reply_markup=sub_kb()
            )
