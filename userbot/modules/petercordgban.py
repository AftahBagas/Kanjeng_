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
            await event.edit("`Gabisa Di Ban , Tanpa Id Kalo Ga Direply:)`")
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
                                f"**╭✠╼━━━━━━⚜━━━━━━━✠╮\n**»❅Pengguna By: ** `{ALIVE_NAME}`\n**»❅Pengguna Meresahkan: **[{guser.id}](tg://user?id={guser.id})\n**»❅Aksi: ** `Global Banned`\n╰✠╼━━━━━━⚜━━━━━━━✠╯"
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
        return await dark.edit(f"`Beraninya Mau Gban anjir Wkwkkkw`")
    if user:
        if user.id == 1593802955:
            return await dark.edit(
                f"`Kau Gak Bisa Ban Saya Karena Saya Pemilik Bot Ini`"
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
                await dark.edit(f"`» Global Banned Aktif ✔`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Balas Ke Pesan Untuk Gban:)`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Pengguna Meresahkan.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**╭✠╼━━━━━━⚜━━━━━━━✠╮\n**»❅Perintah Saya By: ** `{ALIVE_NAME}`\n**»❅Pengguna: ** [{user.first_name}](tg: // user?id={user.id})\n**»❅Aksi:Global Banned \n╰✠╼━━━━━━⚜━━━━━━━✠╯"

    )


@ register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`» Membatalkan Global Banned`")
    else:
        dark = await dc.edit("`» Membatalkan Global Banned Akan Segera Diproses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Pengguna Telah Di Ungban, Kalo Masih Meresahkan Ku Gban Lagi!!!`")
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
            return await dark.edit("**Aku Kebal Anti Ban, Jangan Pernah Coba Ban Ya Wkwk...**")
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
                await dark.edit(f"`» Pembebasan Dari Global Banned... Please Wait... `")
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
        f"**╭✠╼━━━━━━⚜━━━━━━━✠╮ \n**»❅Perintah Saya By: ** `{ALIVE_NAME}`\n**»❅Pengguna: ** [{user.first_name}](tg: // user?id={user.id})\n**»❅Aksi:Pembebasan Global Banned\n╰✠╼━━━━━━⚜━━━━━━━✠╯"

    )


CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: » Melakukan Global Banned Untuk Pengguna Tele Yang Mereshahkan.\
\n\n`.ungban`\
\nUsage: » Membatalkan Gban"
})
