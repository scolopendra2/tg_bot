from aiogram import types
from loader import dp


@dp.message_handler(text='/help')
async def help_bot(message: types.Message):
    await message.answer(f'Hello {message.from_user.full_name}\n'
                         f'/start - запустить бота\n'
                         f'/help - помощь\n'
                         f'/menu - открыть главное меню')