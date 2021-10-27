import io, inspect
from .. import loader, utils
from asyncio import sleep
from math import floor

@loader.tds
class GULMod(loader.Module):
    """Я - гуль!"""
    strings = {'name': 'Ghoul'}
    
    async def гульcmd(self, message):
        x = 1000
        emojies = ['⚫️', '⚪️', '⬜️']
        await message.edit("Я - гуль!")
        await sleep(2)
        while x > 0:
            await message.edit(emojies[floor((1000 - x) / (1000 / len(emojies)))] + str(x) + " - 7 = " + str(x-7))
            x -= 7
            await sleep(1)
