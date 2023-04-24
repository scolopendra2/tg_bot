from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Клавиатура предметов'), KeyboardButton(text='Поддержать бота')],
        [KeyboardButton(text='Расписание')],
        [KeyboardButton(text='Дни рождения')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
