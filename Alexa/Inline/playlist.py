# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝚐𝚛𝚘𝚞𝚙'𝚜 𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑𝙲𝚕𝚘𝚜𝚎 𝚖𝚎𝚗𝚞", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙶𝚛𝚘𝚞𝚙𝚜 𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴 𝙼𝙴𝙽𝚄", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙱𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"𝙷𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝙿𝙰𝚁𝚃𝚈",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"𝙻𝙾𝙵𝙸",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝚂𝙰𝙳",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"𝚆𝙴𝙴𝙱",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝙿𝚄𝙽𝙹𝙰𝙱𝙸",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"𝙾𝚃𝙷𝙴𝚁𝚂",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️𝙶𝙾 𝙱𝙰𝙲𝙺",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            
            InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴 𝙼𝙴𝙽𝚄", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚𝚆𝙴𝙴𝙱",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝚂𝙰𝙳",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ 𝙿𝙰𝚁𝚃𝚈",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝙻𝙾𝙵𝙸",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚𝙱𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"✚𝙷𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚𝙿𝚄𝙽𝙹𝙰𝙱𝙸",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝙾𝚃𝙷𝙴𝚂",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ ᴍᴇɴᴜ", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝚆𝙴𝙴𝙱", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"𝚂𝙰𝙳", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝙿𝙰𝚁𝚃𝚈", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"𝙻𝙾𝙵𝙸", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝙱𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"𝙷𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝙿𝚄𝙽𝙹𝙰𝙱𝙸",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"𝙾𝚃𝙷𝙴𝚃𝚂", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴 𝙼𝙴𝙽𝚄", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙶𝚁𝙿 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="𝙲𝙷𝙴𝙲𝙺𝙾𝚄𝚃 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃", url=f"{url}")],
        [InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴 𝙼𝙴𝙽𝚄", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ᴘʟᴀʏ {user_name[:10]}'s {genre} ᴘʟᴀʏʟɪsᴛ",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="𝙲𝙷𝙴𝙺𝙾𝚄𝚃 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃", url=f"{url}")],
        [InlineKeyboardButton(text="🗑𝙲𝙻𝙾𝚂𝙴 𝙼𝙴𝙽𝚄", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"🗑 𝙳𝙴𝙻𝙴𝚃 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="❌ɴᴏ", callback_data=f"close"),
        ],
    ]
    return buttons
