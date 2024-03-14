import datetime
import logging
import time

from telethon import types

from .. import loader, utils

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Every'}

async def watcher(self, message: Message):
    if message.text.lower() == 'HI':
        await utils.answer(message, '/leave')
