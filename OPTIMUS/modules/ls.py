from OPTIMUS import amaan, HANDLER, SUDO_USERS
from pyrogram import filters
import os

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
**OTHER ADMIN FUNCTIONS**
• {HANDLER}ls
 
"""

@amaan.on_message(filters.command("ls", HANDLER) & filters.me)
@amaan.on_message(filters.command("ls", HANDLER) & filters.user(SUDO_USERS))
async def ls(client, message):
    args = message.text.split(None, 1)
    if len(args) == 2:
        basepath = "/app/{}".format(args[1])
    else:
        basepath = "/app/"
    directory = ""
    listfile = ""
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            directory += "\n{}".format(entry)
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            listfile += "\n{}".format(entry)
    await message.edit_text("**List directory :**`{}`\n**List file :**`{}`".format(directory, listfile))
