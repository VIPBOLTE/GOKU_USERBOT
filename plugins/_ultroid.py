from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, GOKU_USERBOT_cmd

REPOMSG = """
• **GOKU_USERBOT USERBOT** •\n
• Repo - [Click Here](https://github.com/VIPBOLTE/GOKU_USERBOT)
• Addons - [Click Here](https://github.com/VIPBOLTE/GOKU_USERBOTAddons)
• Support - @goku_groupz
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/VIPBOLTE/GOKU_USERBOT"),
        Button.url("Addons", "https://github.com/VIPBOLTE/GOKU_USERBOTAddons"),
    ],
    [Button.url("Support Group", "t.me/goku_groupz")],
]

ULTSTRING = """🎇 **Thanks for Deploying GOKU_USERBOT Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@GOKU_USERBOT_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@GOKU_USERBOT_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/a0c824b3ad40e8bd86db7.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
