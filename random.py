from .. import loader, utils
from telethon.tl.types import Message
import random
from time import sleep

@loader.tds
class EveryMod(loader.Module):
    strings = {"name": "Every"}

    @loader.owner
    async def startcmd(self, message):
        """используй start для начала"""
        await utils.answer(message, '/start@EveryFloodilkaBot')

    @loader.owner
    async def leavecmd(self, message):
        """используй leave для выхода"""
        await utils.answer(message, '/leave@EveryFloodilkaBot')

    
    @loader.owner
    async def call1cmd(self, message: Message):
        reply = await message.get_reply_message()
        a = random.randint(0, 1)
        await reply.click(a)
    
    @loader.owner
    async def call2cmd(self, message: Message):
        reply = await message.get_reply_message()
        c = [1, 2, 3, 5, 6, 7, 8]
        b = random.choice(c) 
        await reply.click(b)
    
    @loader.owner
    async def call3cmd(self, message: Message):
        reply = await message.get_reply_message()
        d = [0, 7]
        e = random.choice(d) 
        await reply.click(e)
    @loader.owner
    async def call4cmd(self, message):
        """используй start для начала"""
        await utils.answer(sticker, 'CAACAgIAAxkBAAIFq2X1hOicCzsVnMRWxg2CpkWi1kMkAAKLOgACPlqoS8TmSGKxWm-0NAQ')
   

