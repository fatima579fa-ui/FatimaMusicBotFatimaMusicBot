from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

app = Client(
    "MusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    msg = f"Welcome {message.from_user.mention} to Music Bot!"
    url = f"https://t.me/{config.OWNER_NAME}"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton(" المطور 👑", url=url)]])
    await message.reply_text(msg, reply_markup=btn)

if __name__ == "__main__":
    print("Bot Starting...")
    app.run()
