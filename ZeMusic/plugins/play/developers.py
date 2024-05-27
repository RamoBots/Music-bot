import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["رامو","المبرمج رامو ","مبرمج السورس","مبرمج","مطور السورس♕"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/33d3e9a856d12a7c158f8.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝑹𝑨𝑴𝑶 || رامـــــــو](https://t.me/c_lxl_c)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ c_lxl_c ❫
◉ 𝙸𝙳      : ❪ `6236388211` ❫
◉ 𝑪𝑯    : ❪ VIP_ALBEAR ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑹𝑨𝑴𝑶 || رامـــــــو", url=f"https://t.me/c_lxl_c"), 
                 ],[
                   InlineKeyboardButton(
                        "🎸𓏺𝗦𝗼𝘂𝗿𝗰𝗲ᯓ𝗥𝗔𝗠𝗢𖠛🎸", url=f"https://t.me/VIP_ALBEAR"),
                ],

            ]

        ),

    )
