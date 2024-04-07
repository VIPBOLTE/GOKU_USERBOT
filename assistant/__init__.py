from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from GOKU_USER import *
from GOKU_USER import _ult_cache
from GOKU_USER._misc import owner_and_sudos
from GOKU_USER._misc._assistant import asst_cmd, callback, in_pattern
from GOKU_USER.fns.helper import *
from GOKU_USER.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = GOKU_USERBOT_bot.full_name
OWNER_ID = GOKU_USERBOT_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException as er:
        LOGS.exception(er)
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
