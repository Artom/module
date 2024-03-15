from .. import loader, utils

@loader.tds
class EveryMod(loader.Module):
    strings = {"name": "Every"}

    @loader.owner
    async def startcmd(self, message):
        """используй <code>start</code> для начала"""
        await utils.answer(message, '/start')

    @loader.owner
    async def leavecmd(self, message):
        """используй leave для выхода"""
        await utils.answer(message, '/leave')
    
