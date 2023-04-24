from loader import dp
from aiogram import types
from data.config import creator_id
from aiogram.types import InputFile


@dp.message_handler(text='Получить базу данных')
async def get_bd(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer_document(InputFile('base.db'))
        await message.answer("Удачного дня бро")
