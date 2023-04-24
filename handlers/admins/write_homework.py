from aiogram.dispatcher import FSMContext
import datetime
from loader import dp, cursor, connect
from aiogram import types
from data.config import creator_id
from states.admins import WriteHomework
photos = []
answer = None
ind = 0


@dp.message_handler(text='Записать домашнее задание')
async def write_homework(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    if user_id not in admins_id and user_id != creator_id:
        await message.answer("У вас нет доступа")
    else:
        await message.answer("Ожидаю домашнее задание, помни что я умею хранить не больше 10 фото")
        global photos, answer, ind
        photos = []
        answer = None
        ind = 0
        sub = cursor.execute(f"""SELECT subject FROM Users
                WHERE user_id={user_id}""").fetchall()[0][0]
        data = datetime.datetime.now()
        data = '.'.join([str(data.day), str(data.month), str(data.year)])
        cursor.execute(f"""INSERT INTO All_Homework(data, subject, text, photos) 
                VALUES('{data}', '{sub}', '{answer}', '{' '.join(photos)}') """)
        connect.commit()
        await WriteHomework.write.set()


@dp.message_handler(content_types=['photo', 'text'], state=WriteHomework.write)
async def state1(message: types.Message, state: FSMContext):
    message_type = message.content_type
    my_id = cursor.execute("""SELECT id FROM All_Homework""").fetchall()[-1][0]
    global photos, answer, ind
    if message_type == 'text':
        answer = message.text
        await message.answer('Текст успешно записан')
    else:
        if answer is None and ind == 0:
            answer = message.caption
        photos.append(str(message.photo[-1].file_id))
        ind += 1
        await message.answer(f'Фото №{ind} сохранено')
    cursor.execute(f"""UPDATE All_Homework
SET text = '{answer}'
WHERE id = {my_id}""")
    cursor.execute(f"""UPDATE All_Homework
    SET photos = '{' '.join(photos)}' 
    WHERE id = {my_id}""")
    connect.commit()
    await state.finish()

