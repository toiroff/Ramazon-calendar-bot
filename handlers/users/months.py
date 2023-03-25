from aiogram import types
from aiogram.types import InputFile

from keyboards.default.menu import back
from loader import dp,db,bot


# Echo bot
@dp.message_handler(text="📆 Bir oylik taqvim")
async def bot_echo(message: types.Message):
    await message.answer(message.text)
    id = message.from_user.id
    malumot = db.filter(tg_id=id)
    if malumot[3] == 'Toshkent':

        await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Rozai_taqvimi_ramazon_tabriklari/5957',caption='🕌 Ramazon taqvimi 2023 - Toshkent\n\n'
                                                 '<b>Saharlik duosi</b> 🤲\n'
                                                'Navaytu an asuma sovma shahri ramazona minal fajri ilal magʻribi, xolisal lillahi taʼala. Allohu akbar.\n\n'
                                                 '<b>Iftorlik duosi</b> 🤲\n'
                                                    'Allohumma laka sumtu va bika amantu va aʼlayka tavakkaltu va aʼla rizqika aftartu, fagʻfirli ya gʻoffaru ma qoddamtu va ma axxortu',reply_markup=back)

    else:
        await bot.send_photo(chat_id=message.from_user.id,photo='https://t.me/Ramazon_Taqvimi_Tabriklari_oyi/7734',caption= "🌙 Ramazon taqvimi 2023 – barcha viloyat uchun keltirilgan.\n\n (Infografikada saharlik va iftorlik duolari ham keltirilgan.)\n\n"
                             ,reply_markup=back
                             )