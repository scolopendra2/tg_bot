from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAnswerUser(StatesGroup):
    add_answer_user = State()