from . import *
from telethon.tl.functions.users import GetFullUserRequest
from .redisdb import *

@HackerSpoilt.on(events.NewMessage(incoming=True, pattern="/start", func = lambda e: e.is_private))
async def _(event):
    xxx = await HackerSpoilt(GetFullUserRequest(event.sender_id))
    chk = await check_user(event.sender_id)
    if not is_added(event.sender_id):
        add_user(event.sender_id)
    if START_MSG is None:
        strt = "Hey {mention}, welcome to my Account Generator Bot!"
    else:
        strt = START_MSG
    if chk is True:
        await event.reply(strt.format(mention=xxx.user.first_name),
                        buttons=[
                            [Button.inline("Help", data="helpme"), Button.url("Channel", url=ltc)],
                            [Button.inline("Generate Accounts", data="gen")]
                        ])
    else:
        st_msg = strt.format(mention=xxx.user.first_name)
        await event.reply("{}\n\nOops! You need to join my channel so as to use me!".format(st_msg), buttons=[Button.url("Join My Channel", url=ltc)])

               [Button.inline("Help", data="helpme"), Button.url("Channel", url=ltc)],
                            [Button.inline("Generate Accounts", data="gen")]
                        ])
    else:
        st_msg = strt.format(mention=xxx.user.first_name)
        await event.reply("{}\n\nOops! You need to join my channel so as to use me!".format(st_msg), buttons=[Button.url("Join My Channel", url=ltc)])


