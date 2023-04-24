from loader import dp
from aiogram import types


@dp.message_handler(text='Поддержать бота')
async def donate(message: types.Message):
    await message.answer("""Краткая статистика по боту:
Всего строк кода: 1270
Всего питоновских файлов: 66
На всё это ушло +-50 часов
Так что без лищних слов""")
    await message.answer('5336 6901 9138 7820')
    await message.answer('сбер) ')
