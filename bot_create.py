from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot_token = ''

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
