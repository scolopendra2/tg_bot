from aiogram import types

from loader import dp, cursor, connect
from keyboards.user import kb_start_menu, all_lists, kb_sub
from data.config import creator_id
from keyboards.admin import kb_admin_one_sub, kb_menu_admin
from keyboards.creator import kb_menu_creator


@dp.message_handler(text='Клавиатура предметов')
async def kb(message: types.Message):
    user_id = message.from_user.id
    cursor.execute(f"""UPDATE Users
                           SET kb = 0
                           WHERE user_id={user_id}""")
    connect.commit()
    await message.answer('Клавиатура предметов открыта!', reply_markup=all_lists[0])


@dp.message_handler(text='<-В главное меню')
async def main_menu(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    if user_id == creator_id:
        await message.answer('Вы вернулись в главное меню!', reply_markup=kb_menu_creator)
    elif user_id in admins_id:
        await message.answer('Вы вернулись в главное меню!', reply_markup=kb_menu_admin)
    else:
        await message.answer('Вы вернулись в главное меню!', reply_markup=kb_start_menu)


@dp.message_handler(text='Следующая страница->')
async def ret(message: types.Message):
    user_id = message.from_user.id

    ind = cursor.execute(f"""SELECT kb FROM Users
    WHERE user_id={user_id}""").fetchall()[0][0]
    if ind + 1 > 2:
        ind = 0
    else:
        ind += 1
    cursor.execute(f"""UPDATE Users
                       SET kb = {ind}
                       WHERE user_id={user_id}""")
    connect.commit()
    kb = all_lists[ind]
    await message.answer('Следующая страница предметов открыта!', reply_markup=kb)


@dp.message_handler(text='<-Вернуться')
async def back(message: types.Message):
    user_id = message.from_user.id

    ind = cursor.execute(f"""SELECT kb FROM Users
    WHERE user_id={user_id}""").fetchall()[0][0]
    if ind - 1 < 0:
        ind = 3
    else:
        ind -= 1
    cursor.execute(f"""UPDATE Users
                       SET kb = {ind}
                       WHERE user_id={user_id}""")
    connect.commit()
    kb = all_lists[ind]
    await message.answer('Предыдущая страница предметов открыта!', reply_markup=kb)


@dp.message_handler(text=['Русский язык', 'Литература', 'Английский язык', 'История', 'Обществознание',
                          'Основы Финансовой Грамотности', 'Большие данные', 'Родной язык', 'Экология', 'Физкультура',
                          'ОБЖ', 'Астрономия', 'Математика', 'Информатика', 'Физика'])
async def sub(message: types.Message):
    text = message.text
    user_id = message.from_user.id
    cursor.execute(f"""UPDATE Users
    SET subject='{text}'
    WHERE user_id={user_id}""")
    connect.commit()
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    if user_id in admins_id or user_id == creator_id:
        await message.answer(text=f'Клавиатура для предмета {text} открыта!', reply_markup=kb_admin_one_sub)
    else:
        await message.answer(text=f'Клавиатура для предмета {text} открыта!', reply_markup=kb_sub)


@dp.message_handler(text='<-Назад')
async def retur(message: types.Message):
    user_id = message.from_user.id
    ind = cursor.execute(f"""SELECT kb FROM Users
        WHERE user_id={user_id}""").fetchall()[0][0]
    await message.answer('Клавиатура предметов открыта!', reply_markup=all_lists[ind])
