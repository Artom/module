from .. import loader, utils
from telethon.tl.types import Message
import re
import logging
logger = logging.getLogger(__name__)


@loader.tds
class Mod(loader.Module):
    strings = {
        'name': 'ModForDan',

        "get_user": "🚀Пользователь: \n"
        "<b>🥷🏻</b> <a href='tg://openmessage?user_id={0}'>{1}</a> \n"
        "<b>📃Юзернейм:</b> @{2} \n"
        "<b>📋Юзер</b> : #user{0} \n"
        "📌<b>Бан</b> : <code>/banid {0}</code> \n"
        "<b>🆔Айди : </b> <code>@{3}</code>",
    }

async def watcher(self, message: Message):
    while True:
        async with message.client.conversation("username") as conv:
            conv.send_message("text")
    
