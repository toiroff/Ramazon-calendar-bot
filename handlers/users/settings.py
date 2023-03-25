from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import settings, menubutton, menu
from loader import dp,db


# Echo bot
from states.state import Update


@dp.message_handler(text="⚙️Sozlamalar")
async def bot_echo(message: types.Message):
    id = message.from_user.id
    malumot = db.filter(tg_id=id)

    await message.answer("Hozirgi sozlamalar.\n\n"
 f"📍Tanlangan shahar: {malumot[3]}",reply_markup=settings)

@dp.message_handler(text="📍Shaharni o'zgartirish")
async def call(message:types.Message):
    await message.answer(text="Sizga qaysi shahar bo'yicha ma'lumot olishni istaysiz!",reply_markup=menubutton)
    await Update.update.set()

@dp.message_handler(state=Update.update)
async def call(message:types.Message,state:FSMContext):
    id = message.from_user.id
    db.update(viloyat=message.text,tg_id=id)
    await message.answer(f"Muvaffaqqiyatli amalga oshirildi ✅\n\n📍Tanlangan shahar: {message.text}",reply_markup=menu)


    await state.finish()