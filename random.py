from .. import loader
from asyncio import sleep


@loader.tds
class EveryMod(loader.Module):
    strings = {"name": "Every"}

    @loader.owner
    async def startcmd(self, message):
        await message.send_message('/start')
    
