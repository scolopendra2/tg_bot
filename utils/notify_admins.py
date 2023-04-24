import logging
from aiogram import Dispatcher
from loader import cursor


async def on_startup_notify(dp: Dispatcher):
    result = cursor.execute("""SELECT admins_id FROM Admins""")
    admins_id = [i[0] for i in result]
    for admin in admins_id:
        try:
            text = 'Bot Started'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
