from .. import loader

@loader.tds
class EverysMod(loader.Module):
    strings = {"name": "Everyyy"}

    @loader.owner
    async def startcmd(self, message):
        """используй <code>start</code> для начала"""
        await message.send('/start')
    
