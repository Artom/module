from .. import loader, utils
from asyncio import sleep, gather


def register(cb):
    cb(SpamMod())

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Every'}

    async def stscmd(self, message):
        """Обычный спам. Используй .spam <кол-во:int> <текст или реплай>."""
        await message.client.send_message(message.to_id, '/start')
