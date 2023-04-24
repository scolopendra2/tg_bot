from aiogram.dispatcher import FSMContext

from loader import dp, cursor, morph
from aiogram import types
from keyboards.user import kb_happy_birthday
from states.users import SearchBirthday


@dp.message_handler(text='Дни рождения')
async def happy(message: types.Message):
    await message.answer("Клавиатура дней рожддений открыта", reply_markup=kb_happy_birthday)


@dp.message_handler(text='Ближайшее день рождение')
async def happy_birhday(message: types.Message):
    answer = cursor.execute("""SELECT * FROM Happy_birthday
    ORDER BY before_the_birthday""").fetchall()[0]
    _, surname, name, patronymic, data_birthday, before_birhday = answer
    surname = morph.parse(surname)[0]
    surname = surname.inflect({'gent'}).word

    name = morph.parse(name)[0]
    name = name.inflect({'gent'}).word

    patronymic = morph.parse(patronymic)[0]
    patronymic = patronymic.inflect({'gent'}).word
    await message.answer(f"Ближайшее день рождение у {surname.capitalize()} {name.capitalize()} "
                         f"{patronymic.capitalize()} "
                         f"через {before_birhday} дней."
                         f"\nДата рождения: {data_birthday}")


@dp.message_handler(text='Поиск дня рождения')
async def search(message: types.Message):
    await message.answer("Введите фамилию и имя:")
    await SearchBirthday.search.set()


@dp.message_handler(content_types=['text'], state=SearchBirthday.search)
async def state_search(message: types.Message, state: FSMContext):
    try:
        answer = message.text.split()
        surname, name = answer[0].capitalize(), answer[1].capitalize()
        result = cursor.execute(f"""SELECT * FROM Happy_birthday
        WHERE surname='{surname}' AND name='{name}'""").fetchall()[0]
        _, surname, name, patronymic, data_birthday, before_birhday = result
        surname = morph.parse(surname)[0]
        surname = surname.inflect({'gent'}).word

        name = morph.parse(name)[0]
        name = name.inflect({'gent'}).word

        patronymic = morph.parse(patronymic)[0]
        patronymic = patronymic.inflect({'gent'}).word
        await message.answer(f"Ближайшее день рождение у {surname.capitalize()} {name.capitalize()} "
                             f"{patronymic.capitalize()} "
                             f"через {before_birhday} дней."
                             f"\nДата рождения: {data_birthday}")
    except Exception:
        await message.answer("Студент не найден")
    await state.finish()
