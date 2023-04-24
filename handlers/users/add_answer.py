from aiogram.dispatcher import FSMContext
import datetime
from loader import dp, cursor, connect
from aiogram import types
from data.config import creator_id
from states.users import AddAnswerUser

photos = []
answer = None
ind = 0


@dp.message_handler(text='Добавить решение')
async def add_answer(message: types.Message):
    user_id = message.from_user.id
    result = cursor.execute(f"""SELECT user_id FROM Add_answer""").fetchall()
    all_user = [i[0] for i in result]
    if user_id not in all_user and user_id != creator_id:
        await message.answer(f'У вас нет прав на добавление решений, чтобы их получить перешлите это сообщение '
                             f'@scolopendra_v2, ваш id: {user_id}')
    else:
        await message.answer("Ожидаю решение, помни я умею хранить не больше 10 фото")
        global photos, answer, ind
        photos, answer, ind = [], None, 0
        name = cursor.execute(f"""SELECT name FROM Add_answer
        WHERE user_id={user_id}""").fetchall()[0][0]
        sub = cursor.execute(f"""SELECT subject FROM Users
                        WHERE user_id={user_id}""").fetchall()[0][0]
        data = datetime.datetime.now()
        data = '.'.join([str(data.day), str(data.month), str(data.year)])
        cursor.execute(f"""INSERT INTO All_answer(name, data, subject, text, photos) 
                        VALUES('{name}', '{data}', '{sub}', '{answer}', '{' '.join(photos)}') """)
        connect.commit()
        id_homework = cursor.execute(f"""SELECT id, id_answer FROM All_homework
        WHERE subject='{sub}'""").fetchall()[-1]
        id_answer = cursor.execute(f"""SELECT id FROM All_answer
        WHERE subject='{sub}'""").fetchall()[-1][0]
        if id_homework[1] != '0':
            id_answer = id_homework[1] + ' ' + str(id_answer)
        cursor.execute(f"""UPDATE All_homework
        SET id_answer='{id_answer}'
        WHERE id={id_homework[0]}""")
        connect.commit()
        await AddAnswerUser.add_answer_user.set()


@dp.message_handler(content_types=['text', 'photo'], state=AddAnswerUser.add_answer_user)
async def add_answer(message: types.Message, state: FSMContext):
    global photos, answer, id
    message_type = message.content_type
    my_id = cursor.execute("""SELECT id FROM All_answer""").fetchall()[-1][0]
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
    cursor.execute(f"""UPDATE All_answer
    SET text = '{answer}'
    WHERE id = {my_id}""")
    cursor.execute(f"""UPDATE All_answer
        SET photos = '{' '.join(photos)}' 
        WHERE id = {my_id}""")
    connect.commit()
    await state.finish()


