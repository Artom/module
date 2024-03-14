from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import inspect
from ..inline.types import InlineCall


@loader.tds
class mattk(loader.Module):
    '''Модуль для автоматической атаки боссов в боте MineEvo'''
    strings = {
        "name" : "mattk"
    }
@loader.watcher()
async def watcher(self,message):
    dly = self.get('dly', None)
    if "Artomka" in message.raw_text:
        await self.client.send_message("@KonkursWar", "/leave")
    
