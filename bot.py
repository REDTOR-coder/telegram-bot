import asyncio
import json
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.filters import CommandStart

# 🔑 ТВОЙ ТОКЕН
TOKEN = "8266316926:AAG-BhL6KKVb1UOY3yDomOHRK8qIwwIF30M"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 🚀 Главное меню (открывает Mini App)
def main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 ОТКРЫТЬ ПАНЕЛЬ REDTOR",
                web_app=WebAppInfo(
                    url="https://redtor.vercel.app"  # ← ссылка на твой index.html
                )
            )
        ],
        [
            InlineKeyboardButton(text="ℹ О системе", callback_data="info")
        ]
    ])
    return keyboard


# ▶ Команда /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    text = """
🔻 <b>REDTOR CONTROL PANEL</b>

Вы вошли в интерфейс системы REDTOR.
Нажмите кнопку ниже для запуска панели управления.
"""
    await message.answer(text, parse_mode="HTML", reply_markup=main_menu())


# ℹ Кнопка "О системе"
@dp.callback_query(lambda c: c.data == "info")
async def info_handler(callback):
    await callback.message.answer("REDTOR Processing Team Interface 🟥")
    await callback.answer()


# 🔥 ПОЛУЧЕНИЕ ДАННЫХ ИЗ MINI APP
@dp.message()
async def webapp_data_handler(message: Message):
    if message.web_app_data:
        data = json.loads(message.web_app_data.data)

        action = data.get("action")
        user_id = data.get("user_id")

        print(f"[WEBAPP] ACTION: {action} | USER: {user_id}")

        if action == "modules":
            await message.answer("💳 Открываю модули процессинга...")
        elif action == "stats":
            await message.answer("📊 Загружаю статистику...")
        elif action == "settings":
            await message.answer("⚙ Открываю настройки...")
        else:
            await message.answer("Неизвестная команда из панели.")


# ▶ Запуск бота
async def main():
    print("REDTOR MINI APP BOT ONLINE")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
