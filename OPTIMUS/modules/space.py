import os
from pyrogram import filters
from OPTIMUS import amaan, HANDLER, SUDO_USERS

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**JUST FOR FUN PURPOSE**
USAGE :-
{HANDLER}space
{HANDLER}blank

"""


# S P A C E

@amaan.on_message(filters.command("space", HANDLER) & filters.me)
@amaan.on_message(filters.command("space", HANDLER) & filters.user(SUDO_USERS))
async def space(client, message):
    await message.edit_text("ㅤ")

# B L A N K

@amaan.on_message(filters.command("blank", HANDLER) & filters.me)
@amaan.on_message(filters.command("blank", HANDLER) & filters.user(SUDO_USERS))
async def blank(client, message):
    await message.edit_text("­")

