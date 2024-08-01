from pyrogram.types import Message
import random
from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
from pyrogram.types import *
import requests
from ANNIEMUSIC import app



@app.on_message(filters.command("logo"))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("Usage:\n\n /logo eva")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.api-ninjas.com/v1/logo?text={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")

@app.on_message(filters.command("animelogo"))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("Usage:\n\n /animelogo eva")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.api-ninjas.com/v1/logo?name={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")
