from .. import loader, utils

@loader.tds
class AFKMod(loader.Module):
    """Every"""

    strings = {
        "name": "Every"}

@loader.on(loader.cmd(pattern='prem'))
async def prem(event):
    async with event.client.conversation(event.chat_id) as conv:
        await conv.send_message('/leave')
    
