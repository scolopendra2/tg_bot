from aiogram import types
from aiogram.types import MediaGroup
from loader import dp, cursor


@dp.message_handler(text='Домашнее задание')
async def dz(message: types.Message):
    user_id = message.from_user.id
    sub = cursor.execute(f"""SELECT subject FROM Users
    WHERE user_id={user_id}""").fetchall()[0][0]

    all_homework = cursor.execute(f"""SELECT * FROM All_Homework
    WHERE subject = '{sub}'""").fetchall()
    if len(all_homework) == 0:
        await message.answer(f"Домашние задания для предмета {sub} не найдены")
    else:
        _, data, subject, text, photos, id_answer = all_homework[-1]
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


@dp.message_handler(text='Статистика учащегося')
async def stat(message: types.Message):
    await message.answer('Функция в разработке, ожидайте обновлений')
