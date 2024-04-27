import logging
import os
import traceback
import config
from tools.broadcast import broadcast
from pyrogram import Client, filters 
from tools.database import Database
from pyrogram.types import Message
from config import AUTH_USERS

from tools.status import handle_user_status
LOGS = logging.getLogger(__name__)

db = Database(config.DB_URL, config.DB_NAME)




@Client.on_message(filters.incoming & filters.private, group=-1)
async def check(client, msg):
    # if msg.from_user.id not in AUTH_USERS:
    #     # await m.delete()
    #     return
    await handle_user_status(client, msg)

@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        # await m.delete()
        return
    try:
        n = await m.reply_text("Collecting Bot stats...\n\nthis will take some time...")
        bu = await db.total_users_count()
        
        await n.edit_text(f"**Total Bot Users: {bu}**")
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.private & filters.command("ban"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        # await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to restrict / ban any user from using this bot.\n\nUsage:\n\n`/ban user_id ban_duration ban_reason`\n\nEg: `/ban 1234567 10 you abused our bot.`\n This will ban user with id `1234567` for `10` days for the reason `you abused our bot`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."

        try:
            await c.send_message(
                user_id,
                f"**Important Message From Bot Owner**\n\nMy Owner Banned You to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ ",
            )
            ban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Client.on_message(filters.private & filters.command("unban"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        # await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban any user.\n\nUsage:\n\n`/unban user_id`\n\nEg: `/unban 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"**Important Message From Bot Owner**\n\nMy Owner Unbanned You Now You Can Use This Bot")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )


@Client.on_message(filters.private & filters.command("banned"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        # await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"> **User_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)



@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        # await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)






