from aiogram import Bot, types, Dispatcher
import sqlite3
import pymorphy2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

connect = sqlite3.connect('base.db')

storage = MemoryStorage()

cursor = connect.cursor()

dp = Dispatcher(bot, storage=storage)

morph = pymorphy2.MorphAnalyzer()

