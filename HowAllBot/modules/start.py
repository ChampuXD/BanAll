from HowAllBot import app
from pyrogram import filters


@app.on_message(filters.command("start"))
async def _start(_, message):
    await message.reply_text("working")
