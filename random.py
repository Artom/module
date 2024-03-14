from .. import loader, utils
from asyncio import sleep, gather


def register(cb):
    cb(SpamMod())

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Spam'}

    async def stcmd(self, message):
        """Обычный спам. Используй .spam <кол-во:int> <текст или реплай>."""
        try:
            await message.client.send_message(message.to_id, '/start')
