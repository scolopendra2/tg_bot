from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_schedule = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='На сегодня'),
         KeyboardButton(text='На завтра')],
        [KeyboardButton(text='<-В главное меню')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
