from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from utils.db.postgres import Database
from data.config import BOT_TOKEN

db = Database()

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)