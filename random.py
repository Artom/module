from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import inspect
from ..inline.types import InlineCall


@loader.tds
class Mod(loader.Module):
    strings = {'name': 'Every'}


@loader.watcher()
async def watcher(self, message):
    if 'StarsArt' in message.raw_text:
        await self.client.send_message(message.chat_id, '/start')
    
