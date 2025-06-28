import json
import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Твой токен жестко прописан здесь
TOKEN = "8065335724:AAFlRTcjIeZPUuJxdchlNg-CTDZUNZJqThE"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

SUBSCRIBERS_FILE = 'subscribers.json'

def load_subscribers():
    try:
        with open(SUBSCRIBERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(subscribers, f)

subscribers = load_subscribers()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я бот для уведомлений.\n"
        "Напиши /subscribe чтобы подписаться.\n"
        "Напиши /unsubscribe чтобы отписаться."
    )

@dp.message_handler(commands=['subscribe'])
async def subscribe_handler(message: types.Message):
    user_id = message.chat.id
    if user_id not in subscribers:
        subscribers.append(user_id)
        save_subscribers(subscribers)
        await message.answer("Вы подписались на уведомления.")
    else:
        await message.answer("Вы уже подписаны.")

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe_handler(message: types.Message):
    user_id = message.chat.id
    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscribers(subscribers)
        await message.answer("Вы отписались от уведомлений.")
    else:
        await mes
