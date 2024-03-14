from .. import loader, utils
from asyncio import sleep, gather


def register(cb):
    cb(SpamMod())

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Every'}

    async def sts(self, message):
        """Обычный спам. Используй .spam <кол-во:int> <текст или реплай>."""
        user_id = str(message.from_user.id)
        if message.text == 'Артом свали':
            await message.client.send_message(message.to_id, '/leave')
