from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "8487936095:AAE5NxkeR0Bx2LqBkbO_2Gzb_HJzcWbZW_I"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Salom 👋")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
