import json
import logging
import time
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка конфигурации
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

TOKEN = config['telegram_token']
CHAT_ID = config['chat_id']

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Для примера: простой хендлер /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для уведомлений о взлётах и пусках. Работаю стабильно.")

# Тестовый хендлер для статуса
@dp.message_handler(commands=['status'])
async def cmd_status(message: types.Message):
    await message.answer("Бот работает. Уведомлений пока нет.")

# Основная логика уведомлений (заглушка)
async def monitor_alerts():
    while True:
        # Здесь должна быть логика отслеживания самолетов и ракет
        # Для примера — просто логируем и ждём 60 секунд
        logger.info("Мониторинг активен...")
        await asyncio.sleep(60)

async def on_startup(dp):
    asyncio.create_task(monitor_alerts())
    logger.info("Бот запущен.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
