import io
import json

import grapheme
from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, utils


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
    a = 'A'
    if message.raw_text.lower() == a:
        await utils.answer(message, '/leave')
    
