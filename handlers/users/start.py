from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from handlers.users.data import *
from keyboards.default.menu import menu, menubutton, back
from loader import dp, db, bot
from states.state import start

@dp.message_handler(text="◀️ Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Ramazon taqvimi 2023 — saharlik va iftorlik vaqtlari.", reply_markup=menu)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        id =message.from_user.id
        malumot = db.filter(tg_id=id)
        if malumot[2] == id:
            await message.answer(f"Ramazon taqvimi 2023 — saharlik va iftorlik vaqtlari.", reply_markup=menu)

        else:

            await message.answer(
                f'<b>Assalomu alaykum {message.from_user.full_name}</b>. Ramazon taqvimi botga xush kelibsiz.\n\n'
                f'Ushbu bot yordamida hohlagan viloyatdagi Ramazon taqvimi bilib olishingiz mumkin.Hozir esa sizga kerakli viloyatni kiriting 😇',reply_markup=menubutton)
    except:
        await message.answer(
            f'<b>Assalomu alaykum {message.from_user.full_name}</b>. Ramazon taqvimi botga xush kelibsiz.\n\n'
            f'Ushbu bot yordamida hohlagan viloyatdagi Ramazon taqvimi bilib olishingiz mumkin.Hozir esa sizga kerakli viloyatni kiriting 😇',
            reply_markup=menubutton)

        await start.shahar.set()

@dp.message_handler(state=start.shahar)
async def bot_echo(message:types.Message,state:FSMContext):

    try:
        ism = message.from_user.first_name
        telegram_id = message.from_user.id
        user_name = message.from_user.username
        db.user_qoshish(name=ism, tg_id=telegram_id, username=user_name,shahar=message.text)

        await message.answer(f"Ramazon taqvimi 2023 — saharlik va iftorlik vaqtlari.", reply_markup=menu)





    except:
        await message.answer("Qayta urinib ko'ring!")
    await state.finish()

@dp.message_handler(text="🗓️ Bugungi taqvim")
async def call(message:types.Message):
    try:
        id = message.from_user.id
        malumot = db.filter(tg_id=id)
        viloyat = malumot[3]

        await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
        await message.answer(text=f"☪️ Ramazon taqvimi:\n\n"
                                             f"<b>Bugun {bugun(f'{viloyat}')}"
                                             f"{hozirgi(f'{viloyat}')}\n</b>"
                                             f"( {viloyat} shahri )\n\n"
                                             f"🏙 <b>Bomdod</b>: {bomdod(viloyat)} 🕰 <b>gacha (Saharlik)</b>\n\n"
                                             f"🌅 <b>Quyosh</b>: {quyosh(viloyat)} 🕰\n\n"
                                             f"🏞 <b>Peshin</b>: {peshin(viloyat)} 🕰\n\n"
                                             f"🌇 <b>Asr</b>: {asr(viloyat)} 🕰\n\n"
                                             f"🌆 <b>Shom</b>: {shom(viloyat)} 🕰 <b>so'ng (Iftor)</b>\n\n"
                                             f"🌃 <b>Xufton</b>: {xufton(viloyat)} 🕰 \n\n"
                                             f"Manba : namozvaqti.uz", disable_web_page_preview=True, reply_markup=back)
    except:
        await message.answer('Sizning shaharingiz topilmadi!')

@dp.message_handler(text="🤲 Saharlik / Iftorlik duosi")
async def bots(message:types.Message):
    await message.answer('☪️ <b>Saharlik duosi</b>\n'
        "Navaytu an asuma sovma shahri ramazona minal fajri ilal magʻribi, xolisal lillahi taʼala. Allohu akbar.\n\n"
                         "☪️ <b>Iftorlik duosi</b>\n"
        "Allohumma laka sumtu va bika amantu va aʼlayka tavakkaltu va aʼla rizqika aftartu, fagʻfirli ya gʻoffaru ma qoddamtu va ma axxortu")
