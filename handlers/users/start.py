from aiogram import types
from loader import dp, connect, cursor


@dp.message_handler(text='/start')
async def start(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute("""SELECT user_id FROM Users""").fetchall()

    if user_id not in [i[0] for i in result]:
        cursor.execute(f"""INSERT INTO Users(user_id, subject) VALUES({user_id}, 'Математика')""")
        connect.commit()

    await message.answer(f"""Привет, {message.from_user.full_name}! Я бот группы ИС-12, помогу:
• Узнать расписание
• Узнать домашние работы
• Напомнить про Дни рождения твоих одногруппников
Чем могу быть полезен?""")
