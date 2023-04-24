from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_last_homework = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Посмотреть по id'), KeyboardButton(text='Посмотреть по дате')],
    [KeyboardButton(text='<-Обратно')]

],
    one_time_keyboard=True,
    resize_keyboard=True)
