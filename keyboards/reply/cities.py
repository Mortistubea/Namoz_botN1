<<<<<<< HEAD
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


cities = ReplyKeyboardMarkup(

    keyboard=[

        [
            KeyboardButton("Toshkent"),
            KeyboardButton("Samarqand")
        ],
        [
            KeyboardButton("Namangan"),
            KeyboardButton("Jizzax")
        ],
        [
            KeyboardButton("Buxoro"),
            KeyboardButton("Andijan")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,

=======
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


cities = ReplyKeyboardMarkup(

    keyboard=[

        [
            KeyboardButton("Toshkent"),
            KeyboardButton("Samarqand")
        ],
        [
            KeyboardButton("Namangan"),
            KeyboardButton("Jizzax")
        ],
        [
            KeyboardButton("Buxoro"),
            KeyboardButton("Andijan")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,

>>>>>>> cf14891cc75f301c7843a0f56a901e1633ff1309
)