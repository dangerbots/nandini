from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
✨️Am Advanced Telegram Music Bot\n🔥Feel High Quality Muzic In Vc🎶🎼\n⚡️Developed By⚡️[TG Danger_Bots🤖](https://t.me/danger_bots)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ADD『♫•𝑁𝐴𝑁𝐷𝐼𝑁𝐼•♫』TO YOUR GROUP", url="https://t.me/LadyNandini_bot?startgroup=true")
                  ],
       
      
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Im Online..🎶\n🌠Drobot<3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌻Support🌻", url="https://t.me/danger_bots")
                ]
            ]
        )
   )
