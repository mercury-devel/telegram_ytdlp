from aiogram import BaseMiddleware
from cachetools import TTLCache



class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, time_limit=1):
        self.limit = TTLCache(maxsize=10_000, ttl=time_limit)

    async def __call__(self, handler, event, data):
        if event.chat.id in self.limit:
            await event.bot.send_message(event.chat.id, "Не спамьте")
            return
        else:
            self.limit[event.chat.id] = None
        return await handler(event, data)