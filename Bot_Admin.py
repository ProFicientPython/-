import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


loop = asyncio.get_event_loop()
kategorii_calback=CallbackData('item_name')
bot = Bot(token="5474681575:AAG98rf55TIJhH7-wnwm8zvdom2riucCUrc")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

chat = -1001377836522

@dp.message_handler()
async def mes_obr(message: types.Message):
    mess = message.text
    print(mess)
    admin = 1087968824
    m = message.from_user.id
    print(m)
    if message.from_user.id != admin:
        if message.forward_date is not None:
            await message.reply('Нельзя пересылать')
            await message.delete()
        else:
            for entity in message.entities:
                if entity.type in ["url", "text_link"]:
                    await message.reply('Нельзя отправлять ссылки')
                    await message.delete()
    else:
        pass






async def on_shutdown(dp):
    await bot.close()
    await storage.close()

if __name__ == "__main__":
    executor.start_polling(dp, loop=loop, skip_updates=True)

