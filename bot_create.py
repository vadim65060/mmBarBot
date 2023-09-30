from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from Config import Config

config = Config('config.json')

bot = Bot(token=config.bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
