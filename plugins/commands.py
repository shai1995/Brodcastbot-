import random
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import *
import asyncio
from Script import text
from .db import tb
from .fsub import get_fsub

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(message.from_user.mention, message.from_user.id)
        )
    if IS_FSUB and not await get_fsub(client, message):return
    await message.reply_text(
        text.START.format(message.from_user.mention),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMIN))
async def total_users(client, message):
    try:
        users = await tb.get_all_users()
        await message.reply(f"👥 **Total Users:** {len(users)}",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎭 Close", callback_data="close")]]))
    except Exception as e:
        r=await message.reply(f"❌ *Error:* `{str(e)}`")
        await asyncio.sleep(30)
        await r.delete()

@Client.on_message(filters.group | filters.channel)
async def send_reaction(client: Client, msg: Message):
    try:
        await msg.react(random.choice(EMOJIS))
    except FloodWait as e:
        print(f"FloodWait: Sleeping for {e.value} seconds")
        await asyncio.sleep(e.value)
        await msg.react(random.choice(EMOJIS))
    except Exception as e:
        print(f"Error: {e}")
