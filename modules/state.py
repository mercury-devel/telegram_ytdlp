from aiogram.fsm.state import State, StatesGroup

class CatchMessageState(StatesGroup):
    message = State()
