from aiogram.dispatcher import FSMContext
from aiogram.types import MediaGroup

from loader import dp, cursor
from aiogram import types
from keyboards.user import kb_last_homework
from keyboards.user import kb_sub
from keyboards.admin import kb_admin_one_sub
from data.config import creator_id
from states.users import SearchByID, SearchByDate


async def send_homework(result, message):
    _, data, subject, text, photos, _ = result
    photos = photos.split()
    if len(photos) == 0:
        try:
            await message.answer(f'Дата добавления: {data}\n'
                                 f'Предмет: {subject}\n'
                                 f'Задание: {text}')
        except Exception:
            await message.answer('Не удалось получить домашнее задание, обратитесь к администратору')
    else:
        album = MediaGroup()
        for i in range(len(photos)):
            if i == 0:
                album.attach_photo(photo=photos[i], caption=f'Дата добавления: {data}\n'
                                                            f'Предмет: {subject}\n'
                                                            f'Задание: {text}')
            else:
                album.attach_photo(photo=photos[i])
        try:
            await message.answer_media_group(media=album)
        except Exception:
            await message.answer('Не удалось получить домашнее задание, обратитесь к администратору')


async def send_answer(sub_id, message):
    try:
        all_answer = cursor.execute(f"""SELECT id_answer FROM All_homework
                WHERE id={sub_id}""").fetchall()[-1][0]
        for i in all_answer.split():
            try:
                id = int(i)
                answer = cursor.execute(f"""SELECT * FROM All_answer
                                WHERE id={id}""").fetchall()[0]
                _, name, data, subject, text, photos = answer
                photos = photos.split()
                if len(photos) == 0:
                    await message.answer(f'Автор решения: {name}\n'
                                         f'Дата добавления решения: {data}\n'
                                         f'Текст: {text}')
                else:
                    album = MediaGroup()
                    for i in range(len(photos)):
                        if i == 0:
                            album.attach_photo(photo=photos[i], caption=f'Автор решения: {name}\n'
                                                                        f'Дата добавления решения: {data}\n'
                                                                        f'Текст: {text}')
                        else:
                            album.attach_photo(photo=photos[i])
                        await message.answer_media_group(media=album)
            except Exception:
                await message.answer('Решение не добавлено или было удалено')
    except Exception:
        await message.answer("Решений для текущего домашнего задания нет")


@dp.message_handler(text='Прошлые домашки')
async def last_homework(message: types.Message):
    user_id = message.from_user.id
    subject = cursor.execute(f"""SELECT subject FROM Users
    WHERE user_id='{user_id}'""").fetchall()[0][0]
    result = cursor.execute(f"""SELECT id, data FROM All_homework
    WHERE subject='{subject}'""").fetchall()
    if len(result) == 0:
        await message.answer(f'Домашние задания для предмета {subject} не найдены')
    else:
        result_v2 = f'Домашние задания по предмету: {subject}:\n'
        for i in range(len(result)):
            id, data = result[i]
            result_v2 += f'Задание №{i + 1}\nid: {id}, date: {data}.\n'
        await message.answer(result_v2, reply_markup=kb_last_homework)


@dp.message_handler(text='<-Обратно')
async def ret(message: types.Message):
    user_id = message.from_user.id
    subject = cursor.execute(f"""SELECT subject FROM Users
        WHERE user_id='{user_id}'""").fetchall()[0][0]
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    if user_id in admins_id or user_id == creator_id:
        await message.answer(f'Клавиатура для предмета {subject} открыта!', reply_markup=kb_admin_one_sub)
    else:
        await message.answer(f'Клавиатура для предмета {subject} открыта!', reply_markup=kb_sub)


@dp.message_handler(text='Посмотреть по id')
async def find_by_id(message: types.Message):
    await message.answer("Введите id домашнего задания:")
    await SearchByID.search_by_id.set()


@dp.message_handler(content_types=['text'], state=SearchByID.search_by_id)
async def state_id(message: types.Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        subject = cursor.execute(f"""SELECT subject FROM Users
                WHERE user_id='{user_id}'""").fetchall()[0][0]
        id = int(message.text)
        result = cursor.execute(f"""SELECT * FROM All_homework
        WHERE id={id} AND subject='{subject}'""").fetchall()[0]
        await send_homework(result, message)
        await send_answer(result[0], message)
    except Exception as ex:
        await message.answer("Неверный id домашнего задания")
    await state.finish()


@dp.message_handler(text='Посмотреть по дате')
async def find_by_id(message: types.Message):
    await message.answer("Введите дату домашнего задания:")
    await SearchByDate.search_by_date.set()


@dp.message_handler(content_types=['text'], state=SearchByDate.search_by_date)
async def state_id(message: types.Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        subject = cursor.execute(f"""SELECT subject FROM Users
                WHERE user_id='{user_id}'""").fetchall()[0][0]
        data = message.text
        result = cursor.execute(f"""SELECT * FROM All_homework
        WHERE data='{data}' AND subject='{subject}'""").fetchall()
        if len(result) == 0:
            await message.answer("На выбранную дату домашних заданий не найдено")
        else:
            for i in result:
                await send_homework(i, message)
                await send_answer(i[0], message)
    except Exception:
        await message.answer("Неверная дата домашнего задания")
    await state.finish()
