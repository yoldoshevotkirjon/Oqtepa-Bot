from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_language = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton("🇺🇿 O'zbekcha"),

        ],
        [
            KeyboardButton("🇷🇺 Russian")
        ],
        [
            KeyboardButton("🇺🇸 English")
        ]

    ],
    resize_keyboard=True,
)

button_buyurtma = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton("🛵 Eltib berish"),
            KeyboardButton("🚶 Olib ketish")

        ],
        [
            KeyboardButton("⬅️ Ortga")
        ]
    ],
    resize_keyboard=True,
)


geolocatsiya = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton("📍Geo-joylashuvni yuborish", request_location=True)


        ],

    ],
    resize_keyboard=True,

)


loc_tanlash = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton("Ha"),
            KeyboardButton("Yoq")

        ],

    ],
    resize_keyboard=True,

)

