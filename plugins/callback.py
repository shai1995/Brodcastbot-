from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url='https://telegram.me/QuickReactRobot?startgroup=botstart')
                    ],
                    [
                        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
                        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
                    ],
                    [
                        InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url='https://telegram.me/QuickReactRobot?startchannel=botstart')
                    ]
                ]
            )
        )

    elif query.data == "help":
        await query.message.edit_text(
            text.HELP.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ᴜᴩᴅᴀᴛᴇꜱ', url='https://telegram.me/Techifybots'),
                        InlineKeyboardButton('ꜱᴜᴩᴩᴏʀᴛ', url='https://telegram.me/TechifySupport')
                    ],
                    [
                        InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
                    ]
                ]
            )
        )

    elif query.data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💥 ʀᴇᴘᴏ', url='https://github.com/TechifyBots/Auto-Reaction-Bot'),
                        InlineKeyboardButton('👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/TechifyRahul')
                    ],
                    [
                        InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='start')
                    ]
                ]
            )
        )
