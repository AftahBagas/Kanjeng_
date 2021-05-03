""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.mintabantuan$")
async def usit(e):
    await e.edit(
        f"**Hai Kanjeng {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/kanjengingsun)"
        "\n[Repo](https://github.com/AftahBagas/-KANJENG)"
        "\n[Instagram](Instagram.com/AftahBagas)")


@register(outgoing=True, pattern="^.varsraw$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/AftahBagas/-KANJENG/Petercord-Userbot/varshelper.txt)")


CMD_HELP.update({
    "petercordmintabantuan":
    "`.mintabantuan`\
\nUsage: Bantuan Untuk Kanjeng-Userbot.\
\n`.varsraw`\
\nUsage: Melihat Daftar Vars."
})
