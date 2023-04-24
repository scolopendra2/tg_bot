from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteAnswer(StatesGroup):
    delete_answer = State()


class AddAnswer(StatesGroup):
    add_answer = State()
