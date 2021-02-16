"""
Created by @Jisan7509
modified by  @mrconfused
Userbot plugin for CatUserbot
"""
#ported by Sh1vam For javes
#Bug fixed by Sh1vam
import emoji

from userbot import CMD_HELP
from userbot import bot as borg

from userbot.utils import admin_cmd
from userbot.helpers import fonts as emojify


@borg.on(admin_cmd(pattern="eem(?: |$)(.*)"))

async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(
             "`What am I Supposed to do with this , Give me a text. `"
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await event.edit(result)


@borg.on(admin_cmd(pattern="cmoji(?: |$)(.*)"))

async def itachi(event):
    ars = event.text
    args = ars[7:]
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(
             "`What am I Supposed to do with this , Give me a text. `"
        )
        return
    try:
         arg,emoji = args.split(";")
    except:
        arg = args
        emoji = "😺"
    '''if not char_is_emoji(emoji):
        arg = args
        emoji = "😺"'''
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await event.edit(result)


'''def char_is_emoji(character):
    return character in emoji.UNICODE_EMOJI'''


CMD_HELP.update(
    {
        "emojify": "**Plugin :** `emojify`\
      \n\n**Syntax :** `.eem` <text>\
      \n****Usage : **Converts your text to big emoji text, with default emoji. \
      \n\n**Syntax :** `.cmoji` <text>;<emoji>\
      \n****Usage : **Converts your text to big emoji text, with your custom emoji.\
      "
    }
)
