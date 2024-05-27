import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                

@app.on_message(
    command(["سورس","السورس","السورس♡"])

)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video="https://graph.org/file/8c121033bd5d988eb59eb.mp4",
        caption="⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/XXXXC_121"), 
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/VIP_ALBEAR"),
                  ],[
                    InlineKeyboardButton(
                        "𝑹𝑨𝑴𝑶 || رامـــــــو", url=f"https://t.me/c_lxl_c"),
                  ],[
                    InlineKeyboardButton(
                        "ضف البوت الي مجموعتك او قناتك🎸", url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )
