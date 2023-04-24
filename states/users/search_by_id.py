from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchByID(StatesGroup):
    search_by_id = State()