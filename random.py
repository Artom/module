from .. import loader, utils

@loader.tds
class EverysMod(loader.Module):
    strings = {"name": "Everyyy"}

    @loader.owner
    async def startcmd(self, message):
        """используй <code>start</code> для начала"""
        await utils.answer(message, '/start')
    
