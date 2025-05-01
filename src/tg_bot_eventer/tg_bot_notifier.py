from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('bot_token')


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
