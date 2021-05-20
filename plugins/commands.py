#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⚡𝘾𝙍𝙀𝘼𝙏𝙀𝙍/𝙁𝙐𝙉𝘿𝙀𝙍 🤓", url="https://t.me/Deeks_04_8")],
                    [
                        InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="help_data"),
                        InlineKeyboardButton("🤹 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🎖️ 𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐀𝐋𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒 🎖️", url="https://t.me/UNI_MOVIES_BOX")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data="start_data"),
                        InlineKeyboardButton("🤹 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🔰𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏🔰", url="https://t.me/UM_Requests")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data="help_data"),
                        InlineKeyboardButton("🏡 𝙶𝙾 𝙷𝙾𝙼𝙴", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⚡𝙾𝚆𝙽𝙴𝚁/𝙲𝚁𝙴𝙰𝚃𝙴𝚁⚡", url="https://t.me/Deeks_04_8")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
