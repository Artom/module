import io
import json

import grapheme
from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils


@loader.tds
class Mod(loader.Module):
    strings = {'name': 'ModForDan'}
async def watcher(self, message: Message):
    a = 'A'
    if message.raw_text.lower() == a:
        await utils.answer(message, '/leave')
    
