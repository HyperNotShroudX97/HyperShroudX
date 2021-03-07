import asyncio
# made by telebot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ub import CMD_HELP
from ub import bot
from ub import bot as borg
from ub.utils import admin_cmd

bot = "@MissRose_bot"

@borg.on(admin_cmd("fedstats ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit(f"**CHECKING**`...`")
    fid = event.text[10:]
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.text[10:]
        user,fid  = sysarg.split(";")
        sysarg,fid  = sysarg.split(";")
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her fedstat.`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"/fedstat {sysarg} {fid}")
                audio = await conv.get_response()
                if "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await borg.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\nFSTATS CHECKED BY @MissRose_bot 🔥\n\nCollected.",
                    )
                else:
                    await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")

@borg.on(admin_cmd("fstat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit(f"**CHECKING**`...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her fedstat.`"
        )
        return
    else:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                audio = await conv.get_response()
                if "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await borg.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\nFSTATS CHECKED BY @MissRose_bot 🔥\n\nCollected.",
                    )
                else:
                    await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")
				
@borg.on(admin_cmd(pattern="fedsub"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Subscribing...`")
    sysarg = event.text[8:]
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedsub " + sysarg)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nSubscribed to given fed ")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")
@borg.on(admin_cmd(pattern="mifed"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Extracting information...`")
    
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds " )
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nMyFedInfo Excracted ")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@borg.on(admin_cmd(pattern="fedinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Extracting information...`")
    sysarg = event.pattern_match.group(1)
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nFedInfo Excracted ")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


CMD_HELP.update(
    {
        "fedstuff": ".fstat <username/userid/reply to user>\nUse - To check the persons fedban stat in @MissRose_Bot.\
        \n\n.fedinfo <fedid>\nUse - To see info about the fed."
    }
)
