import os
from pyrogram import filters
from OPTIMUS import amaan, HANDLER, SUDO_USERS


__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**SEND TAGGED MESSAGE TO SAVED MESSAGES**
USAGE :- {HANDLER}save
""" 

@amaan.on_message(filters.command("save", HANDLER) & filters.me)
@amaan.on_message(filters.command("save", HANDLER) & filters.user(SUDO_USERS))
async def to_saved(client, message):
    await message.reply_to_message.forward("self")
    await message.edit_text('`Message Has BeeN SaveD.`')

