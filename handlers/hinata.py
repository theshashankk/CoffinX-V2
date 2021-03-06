from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJ2GxgnAvflL04PN0B-qpRBbk6trc--AAC3AAD227gRIFzzr3VR17HHwQ")
    await message.reply_text(                               
        f"""<b>Hey {message.from_user.mention} !!
\nI'm Here to Play music In your voice chat...
maintain by @CoffinXSupport..â¨
\nuse this inline buttons to know more đđ.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ Support group đ", url="t.me/CoffinXsupport")
                  ],[
                    InlineKeyboardButton(
                        "âšī¸ updates channel", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "đ¨âđģ Creator đ¨âđģ", url="https://t.me/xD_shashank"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "đ Assistant đ", url="https://t.me/CoffinXPlayer"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "â Add To Your Group â", url="https://t.me/CoffinXmusic_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
   
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yoo Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ SUPPORT GROUP đ", url="https://t.me/CoffinXsupport")
                ]
            ]
        )
   )     
            
@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
      await message.reply_text("""**Cá´É´á´á´á´á´ á´á´ ÉĒÉ´ á´á´ Ōá´Ę Ęá´Ęá´**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ help đ", url="https://t.me/CoffinXmusic_bot?start=help")
                ]
            ]
        )
   )  
            
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nâ /play <song name> - play song you requested
â /dplay <song name> - play song you requested via deezer
â /splay <song name> - play song you requested via jio saavn
â /playlist - Show now playing list
â /current - Show now playing
â/song <song name> - download songs you want quickly
â /search <query> - search videos on youtube with details
â /deezer <song name> - download songs you want quickly via deezer
â /saavn <song name> - download songs you want quickly via saavn
â /video <song name> - download videos you want quickly
\n*Admins only*
âĒ /player - open music player settings panel
âĒ /pause - pause song play
âĒ /resume - resume song play
âĒ /skip - play next song
âĒ /end - stop music play
âĒ /userbotjoin - invite assistant to your chat
âĒ /admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đ Channel", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "đŦ Group", url="https://t.me/CoffinXsupport"
                    )
                ]
            ]
        )
    )                
