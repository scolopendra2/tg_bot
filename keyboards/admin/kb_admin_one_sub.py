from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_admin_one_sub = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Записать домашнее задание'),
         KeyboardButton(text='Удалить домашнее задание')],

        [KeyboardButton(text='Прошлые домашки'),
         KeyboardButton(text='Домашнее задание')],

        [KeyboardButton(text='Добавить решение'),
         KeyboardButton(text='Посмотреть решение')],

        [KeyboardButton(text='<-Назад'),
         KeyboardButton(text='Статистика учащегося')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
