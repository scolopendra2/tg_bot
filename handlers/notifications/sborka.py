from loader import dp
from handlers.notifications.update_schedule import my_shedule
from handlers.notifications.happy_birthday import happy_birtday


@dp.message_handler()
async def sborka():
    await my_shedule()
    await happy_birtday()


async def do_schedule():
    import aioschedule
    import asyncio
    aioschedule.every().day.at('23:10').do(sborka)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
