from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Клавиатура предметов')],
        [KeyboardButton(text='Расписание'), KeyboardButton(text='Дни рождения')],
        [KeyboardButton(text='Клавиатура админа'), KeyboardButton(text='Поддержать бота')]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
