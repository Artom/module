from .. import loader
from asyncio import sleep


@loader.tds
class EverysMod(loader.Module):
    strings = {"name": "Every"}

    @loader.owner
    async def startcmd(self, message):
        """используй <code>start</code> для начала"""
        await message.send('/start')
    
