# by:ilham @bismillahselaluadaa
# Petercord Userbot

from userbot import ALIVE_NAME, CMD_HELP, bot
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName
from telethon.events import ChatAction


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`𝗚𝗮𝗯𝗶𝘀𝗮 𝗱𝗶 𝗯𝗮𝗻 , 𝗧𝗮𝗻𝗽𝗮 𝗜𝗗 𝗸𝗮𝗹𝗮𝘂 𝗴𝗮 𝗸𝗮𝘂 𝗿𝗲𝗽𝗹𝗮𝘆:)`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`KASIAN HARAP... Mohon Lapor Ke GRUP` @petercord", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

# Tentang aku dan dia


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"**╭✠╼━━━━━━⚜━━━━━━━✠╮\n**➢⚜𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔 𝐁𝐲: ** `{ALIVE_NAME}`\n**➢⚜𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔 𝗠𝗘𝗥𝗘𝗦𝗔𝗛𝗞𝗔𝗡: **[{guser.id}](tg://user?id={guser.id})\n**➢⚜𝗔𝗞𝗦𝗜: ** `𝗚𝗹𝗼𝗯𝗮𝗹 𝗕𝗮𝗻𝗻𝗲𝗱`\n╰✠╼━━━━━━⚜━━━━━━━✠╯"
                            )
                        except BaseException:
                            return


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Kamu Harus Di Global Banned, Karena Kamu meresahkan dunia!`")
    else:
        dark = await dc.edit("`➢ Global Banned Pengguna meresahkan Segera Di Proses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`➢ Terdeteksi Pengguna, Rasakan Dibanned Secara Global Karena Kau meresahkan dunia`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`𝗪𝗮𝗵 𝗕𝗲𝗿𝗮𝗻𝗶𝗻𝘆𝗮 𝗠𝗮𝘂 𝗯𝗮𝗻 𝗵𝗮𝗵𝗮`")
    if user:
        if user.id == 1593802955:
            return await dark.edit(
                f"`𝗞𝗮𝘂 𝗚𝗮𝗸 𝗕𝗶𝘀𝗮 𝗕𝗮𝗻 𝗦𝗮𝘆𝗮 𝗸𝗮𝗿𝗲𝗻𝗮 𝗦𝗮𝘆𝗮 𝗣𝗘𝗠𝗜𝗟𝗜𝗞 𝗕𝗢𝗧  𝗶𝗻𝗶`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`➢ 𝗚𝗹𝗼𝗯𝗮𝗹 𝗕𝗮𝗻𝗻𝗲𝗱 𝗔𝗞𝗧𝗜𝗙 ✔`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`𝗕𝗮𝗹𝗮𝘀 𝗞𝗲 𝗣𝗲𝘀𝗮𝗻𝗻𝘆𝗮 𝗹𝗮𝗵 𝗺𝗮𝗻𝗮 𝗯𝗶𝘀𝗮 𝗴𝗯𝗮𝗻 𝗸𝗮𝗹𝗮𝘂 𝗴𝗶𝘁𝘂 𝗱𝗼𝗻𝗴:)`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔 𝗠𝗘𝗥𝗘𝗦𝗔𝗛𝗞𝗔𝗡.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**╭✠╼━━━━━━⚜━━━━━━━✠╮\n**➢⚜𝗣𝗘𝗥𝗜𝗡𝗧𝗔𝗛 𝗦𝗔𝗬𝗔 𝐁𝐲: ** `{ALIVE_NAME}`\n**➢⚜𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔: ** [{user.first_name}](tg: // user?id={user.id})\n**➢⚜𝗔𝗞𝗦𝗜:𝗣𝗘𝗡𝗚𝗛𝗔𝗣𝗨𝗦𝗔𝗡 𝗞𝗞 \n╰✠╼━━━━━━⚜━━━━━━━✠╯"

    )


@ register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`➢ 𝗠𝗲𝗻𝗴𝗮𝗺𝗽𝘂𝗻𝗶 𝗣𝗲𝗻𝗴𝗴𝘂𝗻𝗮 𝗬𝗮𝗻𝗴 𝗠𝗲𝗿𝗲𝘀𝗮𝗵𝗸𝗮𝗻`")
    else:
        dark = await dc.edit("`➢ 𝗠𝗲𝗻𝗰𝗮𝗯𝘂𝘁 𝗛𝘂𝗸𝘂𝗺𝗮𝗻 𝗦𝗲𝗱𝗮𝗻𝗴 𝗗𝗶 𝗣𝗿𝗼𝘀𝗲𝘀`")
    me = await userbot.client.get_me()
    await dark.edit(f"`𝗣𝗲𝗻𝗴𝗴𝘂𝗻𝗮 𝗧𝗲𝗹𝗮𝗵 𝗗𝗶 𝗗𝗶𝗺𝗮𝗮𝗳𝗸𝗮𝗻, 𝗟𝗮𝗶𝗻 𝗞𝗮𝗹𝗶 𝗝𝗮𝗴𝗮 𝗣𝗲𝘁𝗲𝗿𝗸𝗮𝘁𝗮𝗮𝗻 𝗝𝗮𝗻𝗴𝗮𝗻 𝘀𝗽𝗮𝗺...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`📛`")
    if user:
        if user.id == 1593802955:
            return await dark.edit("**𝗔𝗸𝘂 𝗞𝗲𝗯𝗮𝗹 𝗔𝗻𝘁𝗶𝗯𝗮𝗻, 𝗝𝗮𝗻𝗴𝗮𝗻 𝗣𝗘𝗥𝗡𝗔𝗛 𝗖𝗢𝗕𝗔 𝗕𝗔𝗡 𝗬𝗔 𝗛𝗔𝗛𝗔...**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`➢ 𝗣𝗘𝗠𝗕𝗘𝗕𝗔𝗦𝗔𝗡 𝗕𝗘𝗥𝗦𝗬𝗔𝗥𝗔𝗧 𝗕𝗔𝗚𝗜 𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔... Please Wait... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Balas Ke Pesan Pengguna`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Pengguna Tidak Pernah Anda Gban.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**╭✠╼━━━━━━⚜━━━━━━━✠╮ \n**➢⚜𝗣𝗘𝗥𝗜𝗡𝗧𝗔𝗛 𝗦𝗔𝗬𝗔 𝐁𝐲: ** `{ALIVE_NAME}`\n**➢⚜𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔: ** [{user.first_name}](tg: // user?id={user.id})\n**➢⚜𝗣𝗘𝗠𝗕𝗘𝗕𝗔𝗦𝗔𝗡\n𝗕𝗘𝗥𝗦𝗬𝗔𝗥𝗔𝗧\n𝗕𝗔𝗚𝗜\n𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔:🇦 🇰 🇹 🇮 🇫\n╰✠╼━━━━━━⚜━━━━━━━✠╯"

    )


CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: ➢ Melakukan Global Banned Untuk Pengguna Tele Yang Mereshahkan.\
\n\n`.ungban`\
\nUsage: ➢ Memnatalkan Gban"
})
