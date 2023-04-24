from loader import dp, cursor
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.user import kb_start_menu
from keyboards.admin import kb_menu_admin
from data.config import creator_id
from keyboards.creator import kb_menu_creator


@dp.message_handler(Command("menu"))
async def start_menu(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    if user_id == creator_id:
        await message.answer('Главное меню открыто!', reply_markup=kb_menu_creator)
    elif user_id in admins_id:
        await message.answer('Главное меню открыто!', reply_markup=kb_menu_admin)
    else:
        await message.answer('Главное меню открыто!', reply_markup=kb_start_menu)
