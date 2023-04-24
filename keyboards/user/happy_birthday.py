from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_happy_birthday = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ближайшее день рождение'),
         KeyboardButton(text='Поиск дня рождения')],
        [KeyboardButton(text='<-В главное меню')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)