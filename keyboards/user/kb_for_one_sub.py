from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_sub = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Домашнее задание'), KeyboardButton(text='Добавить решение')],
        [KeyboardButton(text='Прошлые домашки'), KeyboardButton(text='Посмотреть решение')],
        [KeyboardButton(text='<-Назад'),
         KeyboardButton(text='Статистика учащегося')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
