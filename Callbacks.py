from aiogram.filters.callback_data import CallbackData

cocktail_done_callback = 'cocktail_done'


class CocktailDoneCallback(CallbackData, prefix='CocktailDone'):
    data: str


class YesNoCallback(CallbackData, prefix='YesNo'):
    payload: str
    yes: str
