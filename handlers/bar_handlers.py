from datetime import datetime

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import Callbacks
import markups
import texts
from bot_create import bot, dp, config
from states import CocktailStates

now = datetime.now()
log = open(now.strftime("%d-%m-%y--%H-%M") + '.log', 'w')


@dp.message(F.text == 'отмена')
async def any_message_menu_respond(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('отменено')


@dp.message(F.text == '/menu')
async def any_message_menu_respond(message: Message, state: FSMContext):
    await state.set_state(CocktailStates.get_cocktail)
    await message.answer(texts.select_cocktails_text,
                         reply_markup=markups.menu_markup)


@dp.message(CocktailStates.get_cocktail)
async def set_cocktail(message: Message, state: FSMContext):
    await state.update_data({'cocktail': message.text})
    await message.answer(texts.get_name_text)
    await state.set_state(CocktailStates.get_name)


@dp.message(CocktailStates.get_name)
async def set_name(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    data = await state.get_data()
    await message.answer(texts.get_request_text(data.get('cocktail'), message.text),
                         reply_markup=markups.yes_no_request_markup)


@dp.callback_query(Callbacks.YesNoCallback.filter((F.payload == 'request') & (F.yes == 'yes')))
async def request_yes(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if await send_cocktail_request(data.get('cocktail'), data.get('name')):
        await callback.message.answer('заявка создана')
    else:
        await callback.message.answer('чат для заявок не установлен (/setchat)')
    await callback.message.delete_reply_markup()
    await state.clear()
    await any_message_menu_respond(callback.message, state)


@dp.callback_query(Callbacks.YesNoCallback.filter((F.payload == 'request') & (F.yes == 'no')))
async def request_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await any_message_menu_respond(callback.message, state)


async def send_cocktail_request(cocktail: str, name: str):
    if config.request_chat is None:
        return False
    await bot.send_message(config.request_chat, texts.get_request_text(cocktail, name),
                           reply_markup=markups.cocktail_done_markup)
    return True


@dp.callback_query(Callbacks.CocktailDoneCallback.filter())
async def issuance_cocktail(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=markups.yes_no_done_markup)


@dp.callback_query(Callbacks.YesNoCallback.filter((F.payload == 'cocktail') & (F.yes == 'yes')))
async def issuance_yes(callback: CallbackQuery):
    log.write(callback.message.text.partition('\n')[0][9:] + '\n')
    await callback.message.delete()


@dp.callback_query(Callbacks.YesNoCallback.filter((F.payload == 'cocktail') & (F.yes == 'no')))
async def issuance_no(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=markups.cocktail_done_markup)


@dp.message(F.text == '/setchat')
async def set_cocktail_request_chat(message: Message):
    config.update_request_chat(message.chat.id)
    await message.answer('чат выдачи установлен')
