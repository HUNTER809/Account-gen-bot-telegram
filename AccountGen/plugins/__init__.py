from telethon import events, Button
from .. import *
import requests
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

if ACCOUNTS is None:
    print("I guess you forgot to load accounts!")
    print("Bot is quiting..")
    exit()

try:
    temp = requests.get(ACCOUNTS)
except:
    print("Issues with the ACCOUNTS url.")
    print(str(e))
    print("Bot is quiting...")
    exit()
else:
    tmp = temp.text
    listofaccs = tmp.split()

async def check_user(id):
    if CHANNEL is None:     # incase no join check is needed
        return True
    ok = True
    try:
        await HackerSpoilt(GetParticipantRequest(channel=CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if CHANNEL.startswith('@'):
    x = CHANNEL.split('@')[1]
    ltc = f"https://t.me/{x}"
else:
    ltc = CHANNEL
it()

async def check_user(id):
    if CHANNEL is None:     # incase no join check is needed
        return True
    ok = True
    try:
        await HackerSpoilt(GetParticipantRequest(channel=CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if CHANNEL.startswith('@'):
    x = CHANNEL.split('@')[1]
    ltc = f"https://t.me/{x}"
else:
    ltc = CHANNEL
L
