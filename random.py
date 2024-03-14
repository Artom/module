import datetime
import logging
import time
import re
from telethon.tl.types import Message

from telethon import types

from .. import loader, utils

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Every'}

async def watcher(self, message:Message):
    a = 'HI'
    if message.text = a:
        await utils.answer(message, '/leave')
    
