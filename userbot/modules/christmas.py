#made by shivam patel
from telethon import events

import asyncio

from userbot.utils import admin_cmd
from userbot import bot as javes
from telethon import events

from userbot import CMD_HELP
@javes.on(admin_cmd("christmas"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,80)
    await event.edit("😊𝓜𝓔𝓡𝓡𝓨 𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢😁")
    animation_chars = ["💖𝓜𝓔𝓡𝓡𝓨💖𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢💖","💙𝓜𝓔𝓡𝓡𝓨💙𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢💙","❤️𝓜𝓔𝓡𝓡𝓨♥️𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢❤️","💚𝓜𝓔𝓡𝓡𝓨💚𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢💚","💜𝓜𝓔𝓡𝓡𝓨💜𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢💜",]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
@javes.on(admin_cmd("wish"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,22)
    await event.edit("😊𝓜𝓔𝓡𝓡𝓨 𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢😁")
    animation_chars = ["""😀😀                              😀😀
😀😀😀                      😀😀😀
😀😀😀😀            😀😀😀😀
😀😀    😀😀    😀😀    😀😀
😀😀        😀😀😀        😀😀
😀😀             😀             😀😀
😀😀                              😀😀
😀😀                              😀😀
😀😀                              😀😀
😀😀                              😀😀""",
"""🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩
🤩🤩
🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩
🤩🤩
🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩
🤩🤩🤩🤩🤩🤩🤩🤩""",
"""😉😉😉😉😉😉😉
😉😉😉😉😉😉😉😉
😉😉                     😉😉
😉😉                     😉😉
😉😉😉😉😉😉😉😉
😉😉😉😉😉😉😉
😉😉    😉😉
😉😉         😉😉
😉😉              😉😉
😉😉                  😉😉""",
"""⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️                     ⭐️⭐️
⭐️⭐️                     ⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️⭐️⭐️⭐️⭐️⭐️
⭐️⭐️    ⭐️⭐️
⭐️⭐️         ⭐️⭐️
⭐️⭐️              ⭐️⭐️
⭐️⭐️                  ⭐️⭐️""",
"""💥💥                    💥💥
   💥💥              💥💥
      💥💥        💥💥
         💥💥  💥💥
            💥💥💥
              💥💥
              💥💥
              💥💥
              💥💥
              💥💥""","""
     🧣🧣🧣🧣🧣🧣
     🧣🧣🧣🧣🧣🧣🧣🧣
   🧣🧣                      🧣🧣
 🧣🧣
🧣🧣
🧣🧣
 🧣🧣
   🧣🧣                      🧣🧣
     🧣🧣🧣🧣🧣🧣🧣🧣
         🧣🧣🧣🧣🧣🧣""",
"""🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟🌟🌟🌟🌟🌟🌟🌟
🌟🌟🌟🌟🌟🌟🌟🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟
🌟🌟                        🌟🌟""",
"""💝💝💝💝💝💝💝
💝💝💝💝💝💝💝💝
💝💝                     💝💝
💝💝                     💝💝
💝💝💝💝💝💝💝💝
💝💝💝💝💝💝💝
💝💝    💝💝
💝💝         💝💝
💝💝              💝💝
💝💝                  💝💝""",
"""🎅🎅🎅🎅🎅🎅
🎅🎅🎅🎅🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
          🎅🎅
🎅🎅🎅🎅🎅🎅
🎅🎅🎅🎅🎅🎅""",
"""       💫💫💫💫💫
  💫💫💫💫💫💫💫
  💫💫                 💫💫
💫💫
  💫💫💫💫💫💫
      💫💫💫💫💫💫
                            💫💫
💫💫                 💫💫
  💫💫💫💫💫💫💫
       💫💫💫💫💫""",
"""✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨
               ✨✨""",
"""☄️☄️                              ☄️☄️
☄️☄️☄️                      ☄️☄️☄️
☄️☄️☄️☄️            ☄️☄️☄️☄️
☄️☄️    ☄️☄️    ☄️☄️    ☄️☄️
☄️☄️        ☄️☄️☄️        ☄️☄️
☄️☄️             ☄️             ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️
☄️☄️                              ☄️☄️""",
"""⁭
                    🌎
                  🌎🌎
               🌎🌎🌎
            🌎🌎 🌎🌎
          🌎🌎    🌎🌎
        🌎🌎       🌎🌎
      🌎🌎🌎🌎🌎🌎
     🌎🌎🌎🌎🌎🌎🌎
   🌎🌎                 🌎🌎
  🌎🌎                    🌎🌎
🌎🌎                       🌎🌎""",
"""       🪐🪐🪐🪐🪐
  🪐🪐🪐🪐🪐🪐🪐
  🪐🪐                 🪐🪐
🪐🪐
  🪐🪐🪐🪐🪐🪐
      🪐🪐🪐🪐🪐🪐
                            🪐🪐
🪐🪐                 🪐🪐
  🪐🪐🪐🪐🪐🪐🪐
       🪐🪐🪐🪐🪐"""]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
