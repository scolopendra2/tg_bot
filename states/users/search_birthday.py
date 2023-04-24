from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchBirthday(StatesGroup):
    search = State()