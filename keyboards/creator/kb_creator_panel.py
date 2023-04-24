from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_creator_panel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить администратора'), KeyboardButton(text='Удалить администратора')],
        [KeyboardButton(text='Выдать права на решение'), KeyboardButton(text='Забрать права на решение')],
        [KeyboardButton(text='<-В главное меню'), KeyboardButton(text='Получить базу данных')]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)