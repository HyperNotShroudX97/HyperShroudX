#made by shivam patel
from telethon import events

import asyncio

from ub.utils import admin_cmd
from ub import bot as javes
from telethon import events

from ub import CMD_HELP
@javes.on(admin_cmd("newyear"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,80)
    await event.edit("😊 HAPPY NEW YEAR 😁")
    animation_chars = ["💖HAPPY NEW YEAR💖","💙HAPPY NEW YEAR💙","❤️HAPPY NEW YEAR❤️","💚HAPPY NEW YEAR💚","💜HAPPY NEW YEAR💜",]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
@javes.on(admin_cmd("happynewyear"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,22)
    await event.edit("😊 HAPPY NEW YEAR TO ALL 😁")
    animation_chars = ["""💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜""","""ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""","""💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚                     💚💚
💚💚                     💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚
💚💚
💚💚
💚💚
💚💚""","""💛💛💛💛💛💛
💛💛💛💛💛💛💛
💛💛                💛💛
💛💛                💛💛
💛💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛
💛💛
💛💛
💛💛""","""💜💜                    💜💜
   💜💜              💜💜
      💜💜        💜💜
         💜💜  💜💜
            💜💜💜
              💜💜
              💜💜
              💜💜
              💜💜
              💜💜""",
"""😺😺                           😺😺
😺😺😺                       😺😺
😺😺😺😺                 😺😺
😺😺  😺😺               😺😺
😺😺     😺😺            😺😺
😺😺         😺😺        😺😺
😺😺             😺😺    😺😺
😺😺                 😺😺😺😺
😺😺                     😺😺😺
😺😺                          😺😺
⁭""","""😁😁😁😁😁😁😁😁
😁😁😁😁😁😁😁😁
😁😁
😁😁
😁😁😁😁😁😁
😁😁😁😁😁😁
😁😁
😁😁
😁😁😁😁😁😁😁😁
😁😁😁😁😁😁😁😁""",
"""🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳              🥳            🥳🥳
 🥳🥳           🥳🥳          🥳🥳
 🥳🥳        🥳🥳🥳       🥳🥳
  🥳🥳   🥳🥳  🥳🥳   🥳🥳
   🥳🥳🥳🥳      🥳🥳🥳🥳
    🥳🥳🥳             🥳🥳🥳""",
"""🌈🌈                    🌈🌈
   🌈🌈              🌈🌈
      🌈🌈        🌈🌈
         🌈🌈  🌈🌈
            🌈🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈""",
"""🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊
🎊🎊
🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊
🎊🎊
🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊""",
"""⁭
                    ㅤ
                  🎉🎉
               🎉🎉🎉
            🎉🎉 🎉🎉
          🎉🎉    🎉🎉
        🎉🎉       🎉🎉
      🎉🎉🎉🎉🎉🎉
     🎉🎉🎉🎉🎉🎉🎉
   🎉🎉                 🎉🎉
  🎉🎉                    🎉🎉
🎉🎉                       🎉🎉""",
"""⁭
🕉🕉🕉🕉🕉🕉🕉
🕉🕉🕉🕉🕉🕉🕉🕉
🕉🕉                     🕉🕉
🕉🕉                     🕉🕉
🕉🕉🕉🕉🕉🕉🕉🕉
🕉🕉🕉🕉🕉🕉🕉
🕉🕉    🕉🕉
🕉🕉         🕉🕉
🕉🕉              🕉🕉
🕉🕉                  🕉🕉"""]
    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
