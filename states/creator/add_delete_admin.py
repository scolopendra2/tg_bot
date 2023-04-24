from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteAdmin(StatesGroup):
    delete_admin = State()


class AddAdmin(StatesGroup):
    add_admin = State()


