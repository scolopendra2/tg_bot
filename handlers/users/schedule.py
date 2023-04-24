from loader import dp, cursor
from aiogram import types
from keyboards.user import kb_schedule


@dp.message_handler(text='Расписание')
async def schedule(message: types.Message):
    await message.answer("Выберите день", reply_markup=kb_schedule)


@dp.message_handler(text='На завтра')
async def schedule(message: types.Message):
    answer = cursor.execute("""SELECT * FROM Shedule""").fetchall()[-1][3]
    await message.answer(answer)


@dp.message_handler(text='На сегодня')
async def schedule(message: types.Message):
    answer = cursor.execute("""SELECT * FROM Shedule""").fetchall()[-1][2]
    await message.answer(answer)
