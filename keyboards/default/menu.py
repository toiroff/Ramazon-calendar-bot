from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗓️ Bugungi taqvim")
        ],
        [
            KeyboardButton(text="📆 Bir oylik taqvim")
        ],
        [
            KeyboardButton(text="🤲 Saharlik / Iftorlik duosi")
        ],
        [
            KeyboardButton(text="⚙️Sozlamalar")
        ]
    ],resize_keyboard=True
)


menubutton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon")
        ],
        [
            KeyboardButton(text="Fargona"),
            KeyboardButton(text="Samarqand", )
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Sirdaryo")
        ],
        [
            KeyboardButton(text="Jizzax"),
            KeyboardButton(text="Zarafshon")
        ],
        [
            KeyboardButton(text="Qarshi"),
            KeyboardButton(text="Navoiy")
        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Nukus")
        ],
        [
            KeyboardButton(text="Termiz"),
            KeyboardButton(text="Urganch",)
        ],
        [
            KeyboardButton(text="Xorazm"),
            KeyboardButton(text="Margilon")
        ]
    ],resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="◀️ Orqaga")
        ]
    ],resize_keyboard=True
)

settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Shaharni o'zgartirish")
        ],
        [
            KeyboardButton(text="🔵 Bizning sahifalarimiz"),
            KeyboardButton(text="◀️ Orqaga")
        ]
    ],resize_keyboard=True
)

admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish")

        ],
        [
            KeyboardButton(text="👤 Foydalanuvchilarga xabar yuborish"),

        ],
        [
KeyboardButton(text="📨 Viloyatlar bo'yicha xabar yuborish"),


        ]
    ],
    resize_keyboard=True

)
Send_users = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TEXT Xabar 📝")

        ],
        [
            KeyboardButton(text="Video Xabar 📝"),
            KeyboardButton(text="RASM Xabar 📝")
        ],
        [
            KeyboardButton(text="⬅Orqaga")
        ],
    ],resize_keyboard=True

)
Send_message = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 TEXT Xabar")

        ],
        [
            KeyboardButton(text="📝 Video Xabar"),
            KeyboardButton(text="📝 RASM Xabar")
        ],
        [
            KeyboardButton(text="⬅Orqaga")
        ],
    ],resize_keyboard=True

)
Send_viloyat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📮 TEXT Xabar")

        ],
        [
            KeyboardButton(text="📮 Video Xabar"),
            KeyboardButton(text="📮 RASM Xabar")
        ],
        [
            KeyboardButton(text="⬅Orqaga")
        ],
    ],resize_keyboard=True

)
