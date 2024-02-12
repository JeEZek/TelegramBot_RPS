from aiogram import Bot, Dispatcher
from environs import Env

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

bot = Bot(bot_token)
dp = Dispatcher()

if __name__ == '__main__':
    dp.run_polling(bot)
