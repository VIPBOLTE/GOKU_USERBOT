import asyncio
import os
import time
from random import choice

import requests
from telethon import Button, events
from telethon.tl import functions, types  # pylint:ignore

from GOKU_USER import *
from GOKU_USER._misc._assistant import asst_cmd, callback, in_pattern
from GOKU_USER._misc._decorators import ultroid_cmd
from GOKU_USER._misc._wrappers import eod, eor
from GOKU_USER.dB import DEVLIST, ULTROID_IMAGES
from GOKU_USER.fns.helper import *
from GOKU_USER.fns.misc import *
from GOKU_USER.fns.tools import *
from GOKU_USER.startup._database import _BaseDatabase as Database
from GOKU_USER.version import __version__, GOKU_USERBOT_version
from strings import get_help, get_string

udB: Database

Redis = udB.get_key
con = TgConverter
quotly = Quotly()
OWNER_NAME = GOKU_USERBOT_bot.full_name
OWNER_ID = GOKU_USERBOT_bot.uid

GOKU_USERBOT_bot: GOKU_USERBOTClient
asst: GOKU_USERBOTClient

LOG_CHANNEL = udB.get_key("LOG_CHANNEL")


def inline_pic():
    INLINE_PIC = udB.get_key("INLINE_PIC")
    if INLINE_PIC is None:
        INLINE_PIC = choice(GOKU_USERBOT_IMAGES)
    elif INLINE_PIC == False:
        INLINE_PIC = None
    return INLINE_PIC


Telegraph = telegraph_client()

List = []
Dict = {}
InlinePlugin = {}
N = 0
cmd = GOKU_USERBOT_cmd
STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001361294038,  # UltroidSupportChat
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1002126989582,  # goku_groupz
    -1001840775426,  # goopu_group
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
