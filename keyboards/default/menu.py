from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Урганч шаҳар')],
        [KeyboardButton(text='Урганч туман')],
        [KeyboardButton(text='Хива шаҳар')],
        [KeyboardButton(text='Хива туман')],
        [KeyboardButton(text='Хонка туман')],
        [KeyboardButton(text='Қўшкупир туман')],
        [KeyboardButton(text='Гурлан туман')],
        [KeyboardButton(text='Боғот туман')],
        [KeyboardButton(text='Ҳазорасп туман')],
        [KeyboardButton(text='Шовот туман')],
        [KeyboardButton(text='Янгибозор туман')],
        [KeyboardButton(text='Янгиарик туман')],
        [KeyboardButton(text='Питнак туман')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


info = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/list@hujjat_sld_bot')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
