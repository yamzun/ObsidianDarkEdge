from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ParseMode
import database
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def start(msg: types.Message):
    database.add_user(msg.from_user.id)
    await msg.answer(
        "🖤 *OBSIDIAN DARK EDGE*\n\n"
        "Precision crypto trading signals.\n"
        "No hype. No promises. No noise.\n\n"
        "Free users receive limited access.\n"
        "Subscribers unlock full signals.\n\n"
        "⚠️ Educational purposes only.\n"
        "Not financial advice.\n\n"
        "Use /subscribe to upgrade.",
        parse_mode=ParseMode.MARKDOWN
    )

@dp.message(Command(commands=["subscribe"]))
async def subscribe(msg: types.Message):
    await msg.answer(
        "🔒 *OBSIDIAN DARK EDGE — PRO ACCESS*\n\n"
        "• High-quality crypto signals\n"
        "• Clear entries, TP & SL\n"
        "• Risk-managed setups\n"
        "• Private Telegram delivery\n\n"
        "Monthly Subscription\n"
        "Limited spots available.\n\n"
        "Contact admin after payment.",
        parse_mode=ParseMode.MARKDOWN
    )

@dp.message(Command(commands=["status"]))
async def status(msg: types.Message):
    if database.is_subscribed(msg.from_user.id):
        await msg.answer("✅ Subscription active")
    else:
        await msg.answer("❌ Not subscribed")

@dp.message(Command(commands=["signal"]))
async def signal(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return

    signal_text = msg.text.replace("/signal", "").strip()
    if not signal_text:
        await msg.answer("Usage: /signal BTC BUY 42000 SL 41000 TP 45000")
        return

    cursor = database.cursor
    cursor.execute("SELECT user_id FROM users WHERE subscribed=1")
    users = cursor.fetchall()

    for user in users:
        await bot.send_message(user[0], f"🚨 *SIGNAL*\n{signal_text}", parse_mode=ParseMode.MARKDOWN)

    await msg.answer("✅ Signal sent to subscribers.")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp)
