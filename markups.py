from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

import Callbacks
import texts

menu_markup = ReplyKeyboardBuilder()
for text in texts.cocktails_text:
    menu_markup.button(text=text)
menu_markup.button(text='отмена')
menu_markup = menu_markup.adjust(3).as_markup()

cocktail_done_markup = InlineKeyboardBuilder().button(text='готово',
                                                      callback_data=Callbacks.CocktailDoneCallback(
                                                          data=Callbacks.cocktail_done_callback)).as_markup()

yes_no_request_markup = InlineKeyboardBuilder()
yes_no_request_markup.button(text='отправить?', callback_data='...')
yes_no_request_markup.button(text='да', callback_data=Callbacks.YesNoCallback(payload='request', yes='yes'))
yes_no_request_markup.button(text='нет', callback_data=Callbacks.YesNoCallback(payload='request', yes='no'))
yes_no_request_markup = yes_no_request_markup.adjust(1, 2).as_markup()

yes_no_done_markup = InlineKeyboardBuilder()
yes_no_done_markup.button(text='готово?', callback_data='...')
yes_no_done_markup.button(text='да', callback_data=Callbacks.YesNoCallback(payload='cocktail', yes='yes'))
yes_no_done_markup.button(text='нет', callback_data=Callbacks.YesNoCallback(payload='cocktail', yes='no'))
yes_no_done_markup = yes_no_done_markup.adjust(1, 2).as_markup()

