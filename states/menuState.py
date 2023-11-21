from aiogram.dispatcher.filters.state import State, StatesGroup


class StateMenu(StatesGroup):
    step = State()
    step1 = State()
    step2 = State()
