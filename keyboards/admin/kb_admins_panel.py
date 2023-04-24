from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_admins_panel = ReplyKeyboardMarkup([
    [KeyboardButton(text='Отправить рассылку'), KeyboardButton('Случайный комплимент')],
    [KeyboardButton(text='<-В главное меню')]
],
    one_time_keyboard=True,
    resize_keyboard=True)