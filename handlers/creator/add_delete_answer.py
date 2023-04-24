from aiogram.dispatcher import FSMContext
from loader import dp, cursor, connect
from aiogram import types
from states.creator import AddAnswer, DeleteAnswer
from data.config import creator_id


@dp.message_handler(text='Выдать права на решение')
async def add_answer(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer('Я думаю ты помнишь что я жду {user_id} {name}')
        await AddAnswer.add_answer.set()


@dp.message_handler(content_types=['text'], state=AddAnswer.add_answer)
async def add_answer(message: types.Message, state: FSMContext):
    try:
        user_id, name = message.text.split()
        cursor.execute(f"""INSERT INTO Add_answer(user_id, name) VALUES({int(user_id)}, '{name}')""")
        connect.commit()
        await message.answer('У меня всё получилось права на решение выдали')
        await dp.bot.send_message(int(user_id), 'Вам выдали права на добавление решений')
    except Exception:
        await message.answer('У меня не получилось выдать права на решение')
    await state.finish()


@dp.message_handler(text='Забрать права на решение')
async def delete_answer(message: types.Message):
    user_id = message.from_user.id
    if user_id != creator_id:
        await message.answer('У вас нет доступа')
    else:
        await message.answer('Я думаю ты помнишь что я жду {user_id}')
        await DeleteAnswer.delete_answer.set()


@dp.message_handler(content_types=['text'], state=DeleteAnswer.delete_answer)
async def delete_admin(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        cursor.execute(f"""DELETE FROM Add_answer
        WHERE user_id={user_id}""")
        connect.commit()
        await message.answer('У меня всё получилось права на добавления решений забраны')
        await dp.bot.send_message(user_id, 'У вас забрали права на добавление решений')
    except Exception as ex:
        await message.answer('У меня не получилось забрать права на добавление решение')
        print(ex)
    await state.finish()
