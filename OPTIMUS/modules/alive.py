from OPTIMUS import amaan, HANDLER, StartTime
from pyrogram import filters, __version__
from sys import version_info
from datetime import datetime
import asyncio
import time

@amaan.on_message(filters.command("ping", HANDLER) & filters.me)
async def ping(client, message):
    start = datetime.now()
    await message.edit_text("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000 
    await message.edit_text(f"**🏓Pong!**\n`{m_s} ms`")



@amaan.on_message(filters.command("alive", HANDLER) & filters.me)
async def alive(client, message):
    text="**OPTIMUS USERBOT**\n"
    text += f"\nPython Version: `{version_info[0]}.{version_info[1]}.{version_info[2]}`"
    text += f"\nPyrogram Version: {__version__}"
    text += f"\nCurrent Uptime: `{str(datetime.now() - StartTime).split('.')[0]}`"
    
    await message.edit_text(text)

    
