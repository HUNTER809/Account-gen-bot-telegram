from . import *

@HackerSpoilt.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am an Account Generator Bot!\nI can generate working accounts for you.\n\nClick generate accounts to get your account!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc), Button.url("Dev", url="https://t.me/HackerSpoilt")],
                         [Button.url("Repository", url="https://github.com/xditya/AccountsGenBot")],
                         [Button.inline("Generate Accounts", data="gen")]
                     ])
 Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc), Button.url("Dev", url="https://t.me/HackerSpoilt")],
                         [Button.url("check", url="https://t.me/HackerSpoilt_Network")],
                         [Button.inline("Generate Accounts", data="gen")]
                     ])
         ])
)
