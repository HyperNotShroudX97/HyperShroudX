from ub.events import javes05
from ub import CMD_HELP, bot as javes, LOGS, CLEAN_WELCOME, BOTLOG_CHATID, JAVES_NAME
from ub.javes_main.commands import rekcah05
from telethon.events import ChatAction
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)

@javes.on(ChatAction)
async def welcome_to_chat(event):
    try:
        from ub.modules.sql_helper.welcome_sql import get_current_welcome_settings
        from ub.modules.sql_helper.welcome_sql import update_previous_welcome
    except AttributeError:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        """user_added=True,
        user_joined=True,
        user_left=False,
        user_kicked=False"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_welcome)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws and cws.reply:
                current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_welcome(event.chat_id, current_message.id)


@javes05(outgoing=True, pattern=r"^!savewelcome(?: |$)(.*)")
async def save_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE \nCHAT ID: {event.chat_id}"
                "\nThe following message is saved as the new welcome note "
                "for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            return await event.edit(
                "`Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.`"
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Welcome note {} for this chat.`"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('saved'))
    else:
        await event.edit(f"`{JAVES_NNAME}`: **Ops, old welcome message found, deleted it Sucessfully now you can save new welcome message!**")


@javes.on(rekcah05(pattern=f"savewelcome(?: |$)(.*)", allow_sudo=True))
async def save_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        return await event.reply("`Running on Non-SQL mode!`")
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE \nCHAT ID: {event.chat_id}"
                "\nThe following message is saved as the new welcome note "
                "for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            return await event.reply(
                "`Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.`"
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Welcome note {} for this chat.`"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.reply(success.format('saved'))
    else:
        await event.reply(f"`{JAVES_NNAME}`: **Ops, old welcome message found, deleted it Sucessfully now you can save new welcome message!**")






@javes05(outgoing=True, pattern="^!checkwelcome$")
async def show_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.edit(f"`{JAVES_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
             f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)



@javes.on(rekcah05(pattern=f"checkwelcome$", allow_sudo=True))
async def show_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.reply(f"`{JAVES_NNAME}`: **No welcome message saved here.**")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.reply(
            f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.reply(
             f"`{JAVES_NNAME}`: **I am currently welcoming new users with this welcome note.**")
        await event.reply(cws.reply)



@javes05(outgoing=True, pattern="^!clearwelcome$")
async def del_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit(f"`{JAVES_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.edit(f"`{JAVES_NNAME}`: ** I Didnt have any welcome messages here **")


@javes.on(rekcah05(pattern=f"clearwelcome$", allow_sudo=True))
async def del_welcome(event):
    try:
        from ub.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        await event.reply("`Running on Non-SQL mode!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.reply(f"`{JAVES_NNAME}`: **Welcome note deleted for this chat.**")
    else:
        await event.reply(f"`{JAVES_NNAME}`: ** I Didnt have any welcome messages here **")



CMD_HELP.update({
    "welcome":
    "\
!savewelcome <welcome message> or reply to a message with !savewelcome\
\nUsage: Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n!checkwelcome\
\nUsage: Check whether you have a welcome note in the chat.\
\n\n!clearwelcome\
\nUsage: Deletes the welcome note for the current chat.\
\n\n**Sudo commands type !help sudo for more info **\
\n.savewelcome , .checkwelcome , .clearwelcome.\
"
})