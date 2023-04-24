from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_subjects_list1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Русский язык'),
         KeyboardButton(text='Литература')],

        [KeyboardButton(text='Английский язык'),
         KeyboardButton(text='История')],

        [KeyboardButton(text='<-В главное меню'),
         KeyboardButton(text='Обществознание'),
         KeyboardButton(text='Следующая страница->')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_subjects_list2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Основы Финансовой Грамотности'),
         KeyboardButton(text='Экология')],

        [KeyboardButton(text='Большие данные'),
         KeyboardButton(text='Родной язык')],

        [KeyboardButton(text='<-Вернуться'),
         KeyboardButton(text='Физкультура'),
         KeyboardButton(text='Следующая страница->')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_subjects_list3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='ОБЖ'),
         KeyboardButton(text='Астрономия')],

        [KeyboardButton(text='Математика'),
         KeyboardButton(text='Информатика')],

        [KeyboardButton(text='<-Вернуться'),
         KeyboardButton(text='Физика')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

all_lists = [kb_subjects_list1, kb_subjects_list2, kb_subjects_list3]