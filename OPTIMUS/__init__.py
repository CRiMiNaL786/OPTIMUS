import importlib
import os
from pyrogram import Client
from datetime import datetime
#from plugins import *
import logging
from inspect import getfullargspec
from pyrogram.types import Message
from OPTIMUS.modules import ALL_PLUGINS

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
LOGGER = logging.getLogger(__name__)
HANDLER = os.environ["HANDLER"]
SUDO_USERS = os.environ["SUDO_USERS"]
SUDO_USERS = [int(i) for i in SUDO_USERS.split()]
ALIVE_PIC = "https://telegra.ph/file/38e0b251dfc0d267d9a89.jpg"

# the logging things

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - [OPTIMUS] - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
log = logging.getLogger("[OPTIMUS]")
log.info("OPTIMUS Userbot | Powered By AMAAN THE GAMER KING | Licensed under GPLv3.")
log.info(" OPTIMUS is Started TRY .help or .alive ")

# client

amaan = Client(
    "amaan",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
 plugins=dict(root=f"OPTIMUS/modules"),
 in_memory=True
)

# start time

StartTime = datetime.now()

# help starter

async def start(self):
        await super().start()
        result = load_cmds(ALL_PLUGINS)
        log.info(result)


# for help command

HELP_COMMANDS = {}

def load_cmds(ALL_PLUGINS):
    for oof in ALL_PLUGINS:
        if oof.lower() == "help":
            continue
        imported_module = importlib.import_module("OPTIMUS.modules." + oof)
        if not hasattr(imported_module, "__PLUGIN__"):
            imported_module.__PLUGIN__ = imported_module.__name__

        if not imported_module.__PLUGIN__.lower() in HELP_COMMANDS:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module.__help__
    return "Done Loading Plugins and Commands!"


# edit or reply

async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})                    
