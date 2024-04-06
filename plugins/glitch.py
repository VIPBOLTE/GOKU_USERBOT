"""
✘ Commands Available -

•`{i}glitch <reply to media>`
    gives a glitchy gif.
"""
import os

from . import bash, get_string, mediainfo, GOKU_USERBOT_cmd


@GOKU_USERBOT_cmd(pattern="glitch$")
async def _(e):
    try:
        import glitch_me  # ignore :pylint
    except ModuleNotFoundError:
        await bash(
            "pip install -e git+https://github.com/1Danish-00/glitch_me.git#egg=glitch_me"
        )
    reply = await e.get_reply_message()
    if not reply or not reply.media:
        return await e.eor(get_string("cvt_3"))
    xx = await e.eor(get_string("glitch_1"))
    wut = mediainfo(reply.media)
    if wut.startswith(("pic", "sticker")):
        ok = await reply.download_media()
    elif reply.document and reply.document.thumbs:
        ok = await reply.download_media(thumb=-1)
    else:
        return await xx.eor(get_string("com_4"))
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{ok}' ult.gif"
    await bash(cmd)
    await e.reply(file="ult.gif", force_document=False)
    await xx.delete()
    os.remove(ok)
    os.remove("ult.gif")
