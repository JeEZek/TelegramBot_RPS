from aiogram import Bot, Dispatcher

BOT_TOKEN = 'BOT TOKEN HERE'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

if __name__ == '__main__':
    dp.run_polling(bot)
