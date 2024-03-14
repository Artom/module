from .. import loader, utils
from asyncio import sleep, gather

def register(cb):
   cb(SpamMod())

class SpamMod(loader.Module):
   """Спам модулh"""
   strings = {'name': 'Spam'}

 async def startscmd(self, message):
     """Обычный спам. Используй .spam <кол-во:int> <текст или реплай>."""
     await message.client.send_file(message.to_id, '/start')
