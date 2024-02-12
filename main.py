import os
import dotenv

from aiogram import Bot, Dispatcher

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

if __name__ == '__main__':
    dp.run_polling(bot)
