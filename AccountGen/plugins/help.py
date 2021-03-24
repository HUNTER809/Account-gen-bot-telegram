#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/HUNTER809/Account-gen-bot-telegram/blob/master/LICENSE > 
#    for the license.

from . import *

@HackerSpoilt.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am an Account Generator Bot!\nI can generate working accounts for you.\n\nClick generate accounts to get your account!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc), Button.url("Dev", url="https://t.me/HackerSpoilt")],
                         [Button.url("Repository", url="https://github.com/HUNTER809/Account-gen-bot-telegram")],
                         [Button.inline("Generate Accounts", data="gen")]
                     ])