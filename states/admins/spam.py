from aiogram.dispatcher.filters.state import StatesGroup, State


class Spam(StatesGroup):
    spam = State()