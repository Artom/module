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
        await reply.click(9)
    
    @loader.owner
    async def call3cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(12)
        
    @loader.owner
    async def call4cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(7)

    @loader.owner
    async def call5cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(5)

    @loader.owner
    async def call6cmd(self, message: Message):
        reply = await message.get_reply_message()
        a = [1, 2, 3, 5, 6, 7, 8, 10]
        b = random.choice(a)
        await reply.click(b)

    @loader.owner
    async def call7cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(6)

    @loader.owner
    async def call8cmd(self, message: Message):
        reply = await message.get_reply_message()
        a = [3, 5, 6, 7, 8, 10]
        b = random.choice(a)
        await reply.click(b)

    @loader.owner
    async def call9cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(7)

    @loader.owner
    async def call10cmd(self, message: Message):
        reply = await message.get_reply_message()
        a = [5, 6, 7, 8, 10]
        b = random.choice(a)
        await reply.click(b)

    @loader.owner
    async def call11cmd(self, message: Message):
        reply = await message.get_reply_message()
        await reply.click(8)

    @loader.owner
    async def call12cmd(self, message: Message):
        reply = await message.get_reply_message()
        a = [2, 3, 5, 6, 7, 8, 10]
        b = random.choice(a)
        await reply.click(b)

