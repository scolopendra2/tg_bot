from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_delete_homework = ReplyKeyboardMarkup([
    [KeyboardButton(text='Удалить по id'), KeyboardButton('Удалить по дате')],
    [KeyboardButton(text='<-Обратно')]
],
    one_time_keyboard=True,
    resize_keyboard=True)
