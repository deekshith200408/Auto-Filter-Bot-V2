#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import re
import pyrogram

from pyrogram import (
    filters,
    Client
)

from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot import Bot
from script import script
from database.mdb import searchquery
from plugins.channel import deleteallfilters
from config import AUTH_USERS

BUTTONS = {}
 
@Client.on_message(filters.group & filters.text)
async def filter(client: Bot, message: Message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return

    if 2 < len(message.text) < 50:    
        btn = []

        group_id = message.chat.id
        name = message.text

        filenames, links = await searchquery(group_id, name)
        if filenames and links:
            for filename, link in zip(filenames, links):
                btn.append(
                    [InlineKeyboardButton(text=f"🎥➡️{filename}",url=f"{link}")]
                )
        else:
            return

        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="🎖️🅄🄼🅁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 1/1",callback_data="pages") 🆄🅼🆁🎖️]
            )
            await message.reply_text(
                f"[𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝙶𝙴𝚃 🤹].\n\nᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n⛃ 𝙼𝙾𝚅𝙸𝙴 𝙽𝙰𝙼𝙴 ❱»<code>{message.text}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀs ғɪʟᴇ ⏬⏬",

                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="𝙶𝙾 𝙽𝙴𝚇𝚃 𝙿𝙰𝙶𝙴 ⏩",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"🤹🆄🅼🆁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 1/{data['total'] 🅄🄼🅁🤹}",callback_data="pages")]
        )

        await message.reply_text("https://telegra.ph/file/2111124196ef563a4c59d.jpg"
                f"<b> [𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝙶𝙴𝚃 🤹].\n\nᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n⛃ 𝙼𝙾𝚅𝙸𝙴 𝙽𝙰𝙼𝙴 ❱»<code>{message.text}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀs ғɪʟᴇ ⏬⏬</b>",


                reply_markup=InlineKeyboardMarkup(buttons)
            )    


@Client.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    clicked = query.from_user.id
    typed = query.message.reply_to_message.from_user.id

    if (clicked == typed) or (clicked in AUTH_USERS):

        if query.data.startswith("next"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword]

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ 𝙶𝙾 𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🤹 🆄🅼🆁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}🆄🅼🆁 🤹", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ 𝙶𝙾 𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🤹 🆄🅼🆁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 {int(index)+2}/{data['total']}🆄🅼🆁 🤹", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword] 

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("𝙶𝙾 𝙽𝙴𝚇𝚃 𝙿𝙰𝙶𝙴 ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎖️🆄🅼🆁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 {int(index)}/{data['total']}🆄🅼🆁🎖️", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ 𝙶𝙾 𝙱𝙰𝙲𝙺 𝙿𝙰𝙶𝙴", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎖️ 🆄🅼🆁 𝚃𝙾𝚃𝙻𝙴 𝙿𝙰𝙶𝙴𝚂 {int(index)}/{data['total']}🆄🅼🆁 🎖️", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data == "pages":
            await query.answer()


        elif query.data == "start_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("⚡𝘾𝙍𝙀𝘼𝙏𝙀𝙍/𝙁𝙐𝙉𝘿𝙀𝙍 🤓", url="https://t.me/Deeks_04_8")],
                [InlineKeyboardButton("🤔 𝙷𝙴𝙻𝙿 ", callback_data="help_data"),
                    InlineKeyboardButton("🤹 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data")],
                [InlineKeyboardButton("🔰 𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐀𝐋𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒 🔰", url="https://t.me/UNI_MOVIES_BOX")]
            ])

            await query.message.edit_text(
                script.START_MSG.format(query.from_user.mention),
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "help_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝙶𝙾 𝙱𝙰𝙲𝙺 ", callback_data="start_data"),
                    InlineKeyboardButton("🤹 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data")],
                [InlineKeyboardButton("🎖️ 𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 🎖️ ", url="https://t.me/UM_Requests")]
            ])

            await query.message.edit_text(
                script.HELP_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "about_data":
            await query.answer()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data="help_data"),
                    InlineKeyboardButton("🏡 𝙶𝙾 𝙷𝙾𝙼𝙴", callback_data="start_data")],
                [InlineKeyboardButton("🔰𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝙍🔰", url="https://t.me/Deeks_04_8")]
            ])

            await query.message.edit_text(
                script.ABOUT_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )


        elif query.data == "delallconfirm":
            await query.message.delete()
            await deleteallfilters(client, query.message)
        
        elif query.data == "delallcancel":
            await query.message.reply_to_message.delete()
            await query.message.delete()

    else:
        await query.answer("🤓𝐇𝐞𝐥𝐨𝐨 𝐁𝐫𝐨𝐨,\n\n⚡ 𝐓𝐡𝐚𝐭𝐬 𝐍𝐨𝐭 𝐁𝐞𝐥𝐨𝐧𝐠𝐬 𝐓𝐨 𝐘𝐨𝐮.\n😅𝐓𝐡𝐚𝐭 𝐁𝐞𝐥𝐨𝐧𝐠𝐬 𝐓𝐨 𝐖𝐡𝐨 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐓𝐡𝐚𝐭 𝐌𝐎𝐕𝐈𝐄 𝐋𝐈𝐍𝐊.\n\n🎖️© 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 :~»ᴜɴɪᴠᴇʀsᴀʟ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛs✓",show_alert=True)


def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]  
