import os
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 Aku adalah bot canggih yang dibuat oleh @xskull7 untuk memutar musik di obrolan suara Grup & Saluran Telegram.\n\n✅ ketik /help atau info lebih lanjut."
      HELP_MSG = [
        ".",
f"""
**Hello, Selamat Datang di {PROJECT_NAME}

⭕ Aku dapat memutar musik di obrolan suara grup Anda serta obrolan suara saluran.

⭕ Assistant: @{ASSISTANT_NAME}\n\nKlik Next ➡️ Untuk Interuksi lebih lanjut.**
""",

f"""
**Pengaturan**

1) Mulai obrolan suara
2) Ketik /play <nama lagu> pertama kali oleh admin
 Jika userbot bergabung nikmati musik, Jika tidak tambahkan @{ASSISTANT_NAME} ke grup kamu dan coba lagi

**Untuk Putar Di Channel**
1) Jadikan aku admin channel kamu.
2) Kirim /userbotjoinchannel dalam grup tertaut.
3) Sekarang kirim perintah di grup tertaut.

**Perintah**

**=>> Memutar Lagu 🎧**

- /play <judul lagu>: Memutar lagu dengan judul.
- /play <yt link>: Memutar dari link YouTube
- /ytplay: Langsung memutar lagu melalui YouTube Music.
- /dplay: Memutar lagu lewat deezer.
- /splay: Memutar lagu lewat jio saavn.

**=>> Pemutaran ⏯**

- /player: Buka menu Pengaturan pemain.
- /skip: Melewati trek saat ini.
- /pause: Jeda trek.
- /resume: Melanjutkan trek yang dijeda.
- /end: Menghentikan pemutaran media.
- /current: Menampilkan trek yang sedang diputar.
- /playlist: Menampilkan daftar putar.

**Perintah yang hanya untuk admin grup -> /play, /current dan /playlist**
""",
        
f"""
**=>> Putar Musik Channel 👨‍🎤**

**⭕ Hanya untuk admin grup tertaut:**

- /cplay <nama lagu>: Putar lagu yang Anda minta.
- /cdplay <nama lagu>: Putar lagu yang Anda minta melalui deezer.
- /csplay <nama lagu>: Putar lagu yang Anda minta melalui jio saavn.
- /cplaylist: Tampilkan daftar yang sedang diputar.
- /cccurrent: Tampilkan sedang diputar.
- /cplayer: Buka panel pengaturan pemutar musik.
- /cpause: Menjeda pemutaran lagu.
- /cresume: Melanjutkan pemutaran lagu.
- /cskip: Putar lagu berikutnya.
- /cend: Menghentikan pemutaran musik.
- /userbotjoinchannel: Undang asisten ke obrolan Anda.

**Channel juga dapat digunakan sebagai pengganti c** ( /cplay = /channelplay )

**⭕ jika Anda tidak suka bermain di grup tertaut:**

1) Dapatkan ID channel Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Channel dengan izin penuh
4) Tambahkan @{ASSISTANT_NAME} ke Channel sebagai admin.
5) Cukup kirim perintah di grup Anda.
""",

f"""
**=>> Lebih banyak alat 😬**

- /musicplayer <on/off> : Aktifkan/Nonaktifkan Pemutar musik
- /reload: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
- /userbotjoin: Undang @{ASSISTANT_NAME} Userbot ke obrolan Anda
""",
f"""
**=>> Unduh lagu/video 📥**
- /video [song name]: Download video lagu dari youtube
- /song [song name]: Unduh audio lagu dari youtube
- /saavn [song name]: Download lagu dari saavn
- /deezer [song name]: Download lagu dari deezer

**=>> Alat pencari 🔍**
- /search [song name]: Cari youtube untuk lagu
- /lyrics [song name]: Dapatkan lirik lagu
""",

f"""
**=>> Perintah untuk Pengguna Sudo 👮**
 - /userbotleaveall - hapus asisten dari semua obrolan
 - /broadcast <reply to message> - siaran global membalas pesan ke semua obrolan
 - /pmpermit [on/off] - aktifkan/nonaktifkan pesan pmpermit
**Pengguna Sudo dapat menjalankan perintah apa pun di grup mana pun.**
"""
      ]
