from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteByID(StatesGroup):
    delete_by_id = State()

