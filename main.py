from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
TOKEN = config('TOKEN')
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['hello'])
async def start_handler(message: types.Message):
            await bot.send_message(message.from_user.id, f'hello {message.from_user.first_name}')
            await message.answer('пока что все')


@db.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)