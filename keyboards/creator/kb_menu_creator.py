from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_creator = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Клавиатура предметов')],
        [KeyboardButton(text='Расписание'), KeyboardButton(text='Дни рождения')],
        [KeyboardButton(text='Клавиатура создателя'), KeyboardButton(text='Клавиатура админа')]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)