import os
import asyncio
import math
from datetime import datetime
from pyrogram import filters
from OPTIMUS import amaan, HANDLER, SUDO_USERS
from pyrogram.errors import FloodWait

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))
__HELP__ = f"""
THIS FEATURE IS DISABLE DUE BUG ON DELETE ALL MESSAGE
Purge many messages in less than one seconds, you need to became admin to do this.
Except for purgeme feature
Do with you own risk!
Purges message will immediately purge that message without warning!
**「 DO NOT PLAY WITH THIS FEATURE 」**
THIS IS NOT A TROLL MODULE!
```
I am not responsible if you nuke all messages in your group, when purges
is running, none can stop that except restart your bot in terminal, but
that was too late, 1 second will purge over than 10000 messages, and
you're fucked off.
```
Developer create this module only for managing group, not for trolling user!
Read this before take an action!
-> All deleted message cannot restore
-> If you're not an admin, and purge with powerful number or reply first message of group, all of your message will deleted!
-> **DON'T DESTROY/DELETE ALL MESSAGES**, developer will not responsible if you're nuked your chat group. Except for cleaning group purposes.
-> This is not a joke, not funny if you're nuked a group by this feature and blame developer for made this powerful weapon!
Ok look like you're understand what happened if you playing with this powerful weapon.
──「 **Purge** 」──
-> `{HANDLER}purge`
Purge from bellow to that replyed message, you need to became admins to do this, else it only purge your message only!
Give a number **without reply** to purge for x messages.
──「 **Purge My Messages** 」──
-> `{HANDLER}purgeme`
Purge your messages only, no need admin permission.
"""


@amaan.on_message(filters.command("purge", HANDLER) & filters.me)
@amaan.on_message(filters.command("purge", HANDLER) & filters.user(SUDO_USERS))
async def purge(client, message):
    if message.reply_to_message:
        datetime.now()
        from_user = None
        start_message = message.reply_to_message.id
        end_message = message.id
        list_of_messages = await client.get_messages(chat_id=message.chat.id,
                                                    message_ids=range(start_message, end_message),
                                                    replies=0)
        list_of_messages_to_delete = []
        purged_messages_count = 0
        for a_message in list_of_messages:
            if len(list_of_messages_to_delete) == 100:
                await client.delete_messages(chat_id=message.chat.id,
                                            message_ids=list_of_messages_to_delete,
                                            revoke=True)
                purged_messages_count += len(list_of_messages_to_delete)
                list_of_messages_to_delete = []
            if from_user is not None:
                if a_message.from_user == from_user:
                    list_of_messages_to_delete.append(a_message.id)
            else:
                list_of_messages_to_delete.append(a_message.id)
        await client.delete_messages(chat_id=message.chat.id,
                                    message_ids=list_of_messages_to_delete,
                                    revoke=True)
        purged_messages_count += len(list_of_messages_to_delete)
        datetime.now()
        await message.delete()
    else:
        await message.delete()



@amaan.on_message(filters.command("purgeme", HANDLER) & filters.me)
@amaan.on_message(filters.command("purgeme", HANDLER) & filters.user(SUDO_USERS))
async def purgeme(client, message):
 if message.reply_to_message:
  await message.delete()
  for x in range(message.reply_to_message.id, message.id):
   try:
    await client.delete_messages(
      message.chat.id, x
    )
   except FloodWait as v:
    await asyncio.sleep(v.value)
   except Exception:
    return False
 else:
  return await message.delete()


@amaan.on_message(filters.command("del", HANDLER) & filters.me)
@amaan.on_message(filters.command("del", HANDLER) & filters.user(SUDO_USERS))
async def delete_replied(client, message):
    msg_ids = [message.id]
    if message.reply_to_message:
        msg_ids.append(message.reply_to_message.id)
    await client.delete_messages(message.chat.id, msg_ids)
