from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.pages import page
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))

@dp.message_handler(text="🔵 Bizning sahifalarimiz")
async def bots(message:types.Message):
    await message.answer('🔵 Bizning sahifalarimiz',reply_markup=page)