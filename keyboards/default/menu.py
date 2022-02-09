from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Qoraqalpogʻiston Respublikasi')],
        [KeyboardButton(text='Andijon viloyati')],
        [KeyboardButton(text='Buxoro viloyati')],
        [KeyboardButton(text='Fargʻona viloyati')],
        [KeyboardButton(text='Jizzax viloyati')],
        [KeyboardButton(text='Namangan viloyati')],
        [KeyboardButton(text='Navoiy viloyati')],
        [KeyboardButton(text='Qashqadaryo viloyati')],
        [KeyboardButton(text='Samarqand viloyati')],
        [KeyboardButton(text='Sirdaryo viloyati')],
        [KeyboardButton(text='Surxondaryo viloyati')],
        [KeyboardButton(text='Xorazm viloyati')],
        [KeyboardButton(text='Toshkent viloyati')],
        [KeyboardButton(text='Toshkent shahar')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
