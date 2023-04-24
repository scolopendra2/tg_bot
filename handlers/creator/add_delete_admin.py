from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, cursor, connect
from data.config import creator_id
from states.creator import AddAdmin, DeleteAdmin


@dp.message_handler(text='Добавить администратора')
async def add_admin(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer('Ты и так всё знаешь но напомню {admin_id} {admin_name}, жду')
        await AddAdmin.add_admin.set()


@dp.message_handler(content_types=['text'], state=AddAdmin.add_admin)
async def add_admin(message: types.Message, state: FSMContext):
    try:
        admin_id, admin_name = message.text.split()
        cursor.execute(f"""INSERT INTO Admins(admins_id, admins_name) VALUES({int(admin_id)}, '{admin_name}')""")
        connect.commit()
        await message.answer('У меня всё получилось админ добавлен')
        await dp.bot.send_message(int(admin_id), 'Вам выдали права администратора')
    except Exception as ex:
        print(ex)
        await message.answer('У меня не получилось добавить админа')
    await state.finish()


@dp.message_handler(text='Удалить администратора')
async def delete_admin(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer('Ты и так всё знаешь но напомню удаляем по id админа, жду')
        await DeleteAdmin.delete_admin.set()


@dp.message_handler(content_types=['text'], state=DeleteAdmin.delete_admin)
async def delete_admin(message: types.Message, state: FSMContext):
    try:
        admin_id = int(message.text)
        cursor.execute(f"""DELETE FROM Admins
        WHERE admins_id={admin_id}""")
        connect.commit()
        await message.answer('У меня всё получилось админ удалён')
        await dp.bot.send_message(admin_id, 'У вас забрали права админа')
    except Exception:
        await message.answer('У меня не получилось удалить админа')
    await state.finish()
