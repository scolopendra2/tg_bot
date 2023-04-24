from aiogram.types import MediaGroup

from loader import dp, cursor
from aiogram import types


@dp.message_handler(text='Посмотреть решение')
async def view_answer(message: types.Message):
    try:
        user_id = message.from_user.id
        subject = cursor.execute(f"""SELECT subject FROM Users
            WHERE user_id={user_id}""").fetchall()[0][0]
        all_answer = cursor.execute(f"""SELECT id_answer FROM All_homework
                WHERE subject='{subject}'""").fetchall()[-1][0]
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
    await message.answer('Для прошлых домашних заданий решение все решения выводятся вместе с заданием')
