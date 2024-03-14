from .. import loader, utils
from asyncio import sleep, gather
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon import utils

api_id = '10610638'
api_hash = 'e498ce5d88823c037e9edf1a2ab10c5a'

class EveryMod(loader.Module):
    """Every модуль"""
    strings = {'name': 'Every'}

async def main():
    async with TelegramClient('my_bot', api_id, api_hash) as client:
        me = await client.get_me()
        print(me.stringify())

        @client.on(events.NewMessage(pattern=r'.*\b(?:спонс|Спонс|СПОНС|spons|Spons|спонса|Спонса|Спонсы|спонсы|sponsi|cgjyc|Cgjyc|cgjycf|Cgjycf)\b.*'))
        async def handle_sponsor_message(event):
            if event.is_private:
                await event.respond('Привет, спонсы не выдаю!')

        @client.on(events.NewMessage(pattern=r'.*\b(?:пошел нахуй|Пошел нахуй)\b.*'))
        async def handle_sponsor_message(event):
            if event.is_private:
                await event.respond('Без осков пж')   

        await client.run_until_disconnected()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
