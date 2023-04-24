from loader import dp, cursor, connect, morph
import datetime
from data.config import creator_id


async def happy_birtday():
    try:
        result = cursor.execute(f"""SELECT date_birthday FROM Happy_birthday""").fetchall()
        all_data = [i[0] for i in result]
        result = cursor.execute(f"""SELECT user_id FROM Users""").fetchall()
        all_chat_id = [i[0] for i in result]
        now_data = str(datetime.datetime.now()).split()[0].split('-')
        now_data = datetime.datetime(2006, int(now_data[1]), int(now_data[2]))
        for i in range(len(all_data)):
            day, month, _ = all_data[i].split('.')
            happy_data = datetime.datetime(2006, int(month), int(day))
            before_birhday = happy_data - now_data
            if 'day' in str(before_birhday):
                before_birhday = str(before_birhday).split('day')[0]
            else:
                before_birhday = 0
            before_birhday = int(before_birhday)
            if before_birhday < 0:
                before_birhday = 365 + before_birhday

            cursor.execute(f"""UPDATE Happy_birthday
            SET before_the_birthday={before_birhday}
            WHERE id={i + 1}""")
        connect.commit()

        result = cursor.execute(f"""SELECT * FROM Happy_birthday
            WHERE before_the_birthday=7 OR before_the_birthday=3 OR before_the_birthday=0""").fetchall()
        for i in result:
            _, surname, name, patronymic, data_birthday, before_birhday = i
            surname = morph.parse(surname)[0]
            surname = surname.inflect({'gent'}).word

            name = morph.parse(name)[0]
            name = name.inflect({'gent'}).word

            patronymic = morph.parse(patronymic)[0]
            patronymic = patronymic.inflect({'gent'}).word

            if before_birhday != '0':
                for chat_id in all_chat_id:
                    try:
                        await dp.bot.send_message(chat_id=chat_id, text=f"ВНИМАНИЕ!!!"
                                                                        f"\nУ {surname.capitalize()} {name.capitalize()} {patronymic.capitalize()} "
                                                                        f"день рождение через {before_birhday} дней"
                                                                        f"\nДата рождения: {data_birthday}")
                    except Exception:
                        pass
            else:
                for chat_id in all_chat_id:
                    try:
                        await dp.bot.send_message(chat_id=chat_id,
                                                  text=f"ВНИМАНИЕ!!!\nУ {surname.capitalize()} {name.capitalize()} {patronymic.capitalize()} "
                                                       f"сегодня день рождение")
                    except Exception:
                        pass
        await dp.bot.send_message(creator_id, 'Дни рождения успешно обновлены')
    except Exception as ex:
        await dp.bot.send_message(creator_id, f'Не удалось обновить дни рождения\n'
                                              f'Error: {ex}')
