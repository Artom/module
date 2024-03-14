import io
import json

import grapheme
from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils


@loader.tds
class Mod(loader.Module):
    strings = {'name': 'Every'}


@loader.watcher()
async def watcher(self, message):
    if 'StarsArt' in message.raw_text:
        await self.client.send_message(message, '/start')
    
