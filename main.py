import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *


bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm exo Bot", reply_markup=buttons)


@dp.message_handler(commands=['inline'])
async def exo(message: types.Message):
    await message.answer('Inline buttons', reply_markup=inline_buttons)
   



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)