# Darkcobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,, 
#
#
#hehehhe
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath
from math import ceil
import asyncio
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
import os
from userbot.events import javes05, bot, rekcah05
from userbot.util import admin_cmd
from userbot import tebot as tgbot
from userbot import bot as borg
javes = client = bot
from telethon import events

import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io
#ABEE O KANGAR  BACK OPEN CLSE BTN KANG KIYA TO YE LONE CHIPKA DENA AUR GLOBALS K BINA NAHI CHALAGA aur global 5 gaja diff name and manipulation se imported hai 
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
from userbot.utils import remove_plugin,load_module
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
#from youtubesearchpython import SearchVideos
from userbot.javes_main.heroku_var import Var
from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

# 🇦 🇦 🇵     🇾 🇦 🇭 🇦    🇦 🇦 🇾 🇪    🇰 🇮 🇸     🇱 🇮 🇾 🇪 ??

# 🇨 🇭 🇦 🇱 🇴      🇸 🇮 🇷    🇵 🇱 🇪 🇦 🇸 🇪    🇬 🇪 🇹 🇴 🇺 🇹    




       
  #       🇮 🇹 🇳 🇦    🇰 🇾 🇺   🇸 🇵 🇾     🇰 🇷    🇷 🇭 🇪     🇭 🇴      🇸 🇭 🇦 🇦 🇩 🇮    🇰 🇷 🇳 🇮    🇭    🇰 🇾 🇦   🇧 🇸 🇩 🇰 

    @tgbot.on(events.InlineQuery(pattern=r"helpr"))  # pylint:disable=E0602
    async def inline_id_handler(event: events.InlineQuery.Event):
        builder = event.builder
        result = None
        query = event.text
        me = await client.get_me()
        if event.query.user_id == me.id and query.startswith("helpr"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_HELP, "helpr")
            result = builder.article(" Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_HELP)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Please get your own Userbot😁😁"
              await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))#hehe
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()  # pylint:disable=E0602
        if event.query.user_id == me.id:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_HELP, "helpr")
          
            await event.edit(buttons=dc)
        else:
            Cobra = "Please get your own Userbot"
            await event.answer(Cobra)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()  # pylint:disable=E0602
        if event.query.user_id == me.id:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_HELP,  # pylint:disable=E0602
                "helpr"
            )
            
            await event.edit(buttons=dc)
        else:
              TheDark = "Please get your own Userbot😁😁"
              await event.answer(TheDark)
 #hehehehehhehhehhehe   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"closer")))
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        if event.query.user_id == me.id:
            await event.edit("`Main Menu Has Been Closed`")
        else:
            reply_pop_up_alert = "Please get your own Userbot😁😁"
            await event.answer(reply_pop_up_alert)
   

  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"bus_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        if not event.query.user_id == me.id:
            atul= "Please get your own Userbot😁😁"
            await event.answer(atul)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        global shivam_sh1vam
        shivam_sh1vam="{}".format(plugin_name)
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "💠🔮💎"
        u = 0
        for i in CMD_HELP[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += "😁"

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n __Click on buttons below to load or unload them..".format(plugin_name)
        )
        try:
            me = await client.get_me()
            if event.query.user_id == me.id :
                dc = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)#hehe
        except: 
            me = await client.get_me()
            if event.query.user_id == me.id :
                sh1vam = [custom.Button.inline("◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥",data="backr({})".format(shivam)),custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="closer")]
                halps = "Do .hlp {} to get the list of commands.".format(plugin_name)
                await event.edit(halps,buttons=sh1vam)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"load\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              me = await client.get_me()
              if event.query.user_id == me.id :
                    
#  🇦 🇷 🇪      🇧 🇸 🇩 🇰      🇮 🇸 🇸 🇪    🇰 🇦 🇳 🇬  🇲 🇦 🇹   🇰 🇷    🇷 🇪   🇲 🇨 
                    
                    try:
                        fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                        load_module(event.data_match.group(1).decode("UTF-8"))# kyu sir kang krne m musil aa rhi h kya ... Bolo help kr du kya 😂😂😂
                        await event.edit( "`Successfully loaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e))+ " Successfully loaded" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot"
                    await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"unload\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              me = await client.get_me()
              if event.query.user_id == me.id :
                    
                    
                    try:
                        fcix = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                        remove_plugin(event.data_match.group(1).decode("UTF-8"))#kyu sir kang krne m muskil ho rhi h kya bologe toh help krdu 😂😂
                        await event.edit( "`Successfully unloaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e)) +"Successfully unloaded"+ str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot"
                    await event.answer(reply_pop_up_alert)#hehehe
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backr\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
            
            me = await client.get_me()
            if event.query.user_id == me.id :
                try:
                    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                    buttons = paginate_help(current_page_number, CMD_HELP, "helpr")
                    await event.edit("`>>> Here Is The Main Menu `", buttons=buttons)
                except:
                    buttons = paginate_help(0, CMD_HELP, "helpr")
                    await event.edit("`>>> Here Is The Main Menu `", buttons=buttons)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows =int(os.environ.get("NO_OF_COLM_TO_DESPLAY_IN_HELP",5))
    number_of_cols = int(os.environ.get("NO_OF_ROWS_TO_DESPLAY_IN_HELP",5))
    multi = os.environ.get("EMOJI_TO_DESPLAY_IN_HELP","🔥")
    mult2i = os.environ.get("EMOJI2_TO_DESPLAY_IN_HELP","💧")
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {} {}".format(random.choice(list(multi)), x,random.choice(list(mult2i))),
        data="bus_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs =  list(zip(modules[0::number_of_cols],modules[1::number_of_cols],modules[2::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam=modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("◃:✮𝙿𝚁𝙴𝚅.❃", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⋇⋆𝙲𝙻✦𝚂𝙴⋆⋇", data="closer"),
             custom.Button.inline("❃.𝙽𝙴𝚇𝚃✮:▹", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs

# chal nikal 
# gtfo
# SED aagye aap😂

