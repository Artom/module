from .. import loader, utils

@loader.tds
class EveryMod(loader.Module):
    strings = {"name": "Every"}

    @loader.owner
    async def startcmd(self, message):
        """используй start для начала"""
        await utils.answer(message, '/start@EveryFloodilkaBot')

    @loader.owner
    async def leavecmd(self, message):
        """используй leave для выхода"""
        await utils.answer(message, '/leave@EveryFloodilkaBot')

    
    @loader.owner
    async def call1cmd(self, message):
        await eval(message.click(0))

    @loader.owner
    async def call2cmd(self, message):
        await eval(click(0))
