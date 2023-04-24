from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchByDate(StatesGroup):
    search_by_date = State()