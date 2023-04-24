from aiogram.dispatcher import FSMContext

from loader import dp, cursor
from aiogram import types
from data.config import creator_id
from states.admins import Spam
from keyboards.admin import kb_admins_panel
from random import sample

@dp.message_handler(text='Клавиатура админа')
async def open_panel(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT admins_id FROM Admins""").fetchall()
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer('Клавиутура админа открыта', reply_markup=kb_admins_panel)


@dp.message_handler(text='Отправить рассылку')
async def spam(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT admins_id FROM Admins""").fetchall()
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer('Введите текст, внимание он будет отправлен всем пользователям которые когда либо '
                             'пользовались ботом, отменить это действие уже не получится)))))')
        await Spam.spam.set()


@dp.message_handler(content_types=['text'], state=Spam.spam)
async def spam(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    message = message.text
    result = cursor.execute("""SELECT user_id FROM Users""").fetchall()
    all_user_id = [i[0] for i in result]
    del all_user_id[all_user_id.index(user_id)]
    for i in all_user_id:
        try:
            await dp.bot.send_message(i, f'ПРИШЛО СООБЩЕНИЕ ОТ АДМИНИСТРАТОРА:\n'
                                         f'{message}')
        except Exception:
            pass
    await dp.bot.send_message(user_id, 'Сообщения были отправлены всем пользователям бота')
    await state.finish()


@dp.message_handler(text='Случайный комплимент')
async def komp(message: types.Message):
    result = cursor.execute("""SELECT text FROM compliments""").fetchall()
    all_comp = [i[0] for i in result]
    answer = sample(all_comp, 1)[0]
    await message.answer(answer)