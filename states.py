from aiogram.fsm.state import State, StatesGroup


class CocktailStates(StatesGroup):
    get_cocktail = State()
    get_name = State()
