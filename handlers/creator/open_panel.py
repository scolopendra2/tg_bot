from loader import dp
from keyboards.creator import kb_creator_panel
from aiogram import types
from data.config import creator_id


@dp.message_handler(text='Клавиатура создателя')
async def open_creator(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer('Привет бро', reply_markup=kb_creator_panel)
