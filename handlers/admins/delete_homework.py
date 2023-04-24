from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, connect, cursor
from data.config import creator_id
from keyboards.admin import kb_delete_homework
from states.admins import DeleteByID, DeleteByDate


@dp.message_handler(text='Удалить домашнее задание')
async def admin_delete(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT admins_id FROM Admins""").fetchall()
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer("Все домашние задания для выбранного предмета можно посмотреть по команде 'Все домашки'\n"
                             "\nВыберите как хочешь удалить домашку, но помни что удаление по дате удалит все домашки "
                             "на выбранну дату", reply_markup=kb_delete_homework)


@dp.message_handler(text='Удалить по id')
async def delete_homework_by_id(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT admins_id FROM Admins""").fetchall()
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer("Введите id домашнего задания:")
        await DeleteByID.delete_by_id.set()


@dp.message_handler(content_types=['text'], state=DeleteByID.delete_by_id)
async def delete_homework_by_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Неверный id домашнего задания")
    else:
        id = int(message.text)
        try:
            user_id = message.from_user.id
            subject = cursor.execute(f"""SELECT subject FROM Users
            WHERE user_id={user_id}""").fetchall()[0][0]
            id_subject = cursor.execute(f"""SELECT subject FROM All_homework
                WHERE id={id} AND subject='{subject}'""").fetchall()
            if len(id_subject) == 0:
                await message.answer(f"У предмета {subject} нет домашних заданий с id: {id}")
            else:
                cursor.execute(f"""DELETE FROM All_homework
                                    WHERE id={id} AND subject='{subject}'""")
                connect.commit()
                await message.answer(f"Домашнее задание для предмета {subject} с id: {id} Успешно удалено")
        except Exception:
            await message.answer('Не удалось удалить домашнее задание, обратитесь к администратору')
    await state.finish()


@dp.message_handler(text='Удалить по дате')
async def delete_homework_by_data(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT admins_id FROM Admins""").fetchall()
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer("Введите дату домашнего задания:")
        await DeleteByDate.delete_by_date.set()


@dp.message_handler(content_types=['text'], state=DeleteByDate.delete_by_date)
async def delete_homework_by_id(message: types.Message, state: FSMContext):
    data = message.text
    try:
        user_id = message.from_user.id
        subject = cursor.execute(f"""SELECT subject FROM Users
            WHERE user_id={user_id}""").fetchall()[0][0]

        data_subject = cursor.execute(f"""SELECT subject FROM All_homework
                WHERE data='{data}' AND subject='{subject}'""").fetchall()
        if len(data_subject) == 0:
            await message.answer(f"У предмета {subject} нет домашних заданий на дату: {data}")
        else:
            cursor.execute(f"""DELETE FROM All_homework
                    WHERE data='{data}'AND subject='{subject}'""")
            connect.commit()
            await message.answer(f"Домашние задания для предмета {subject} на дату: {data} Успешно удалены")
    except Exception:
        await message.answer('Не удалось удалить домашнее задание, обратитесь к администратору')
    await state.finish()
