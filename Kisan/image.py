import os
import logging
from os import getenv
import requests
from requests import get 
from pyrogram import filters
from pyrogram.types import InputMediaPhoto



# config vars
API_ID = int(os.getenv("API_ID","20878057"))
API_HASH = os.getenv("API_HASH","eaf35f73b9b04235b7b730d866ddb770")
BOT_TOKEN = os.getenv("BOT_TOKEN","7069412088:AAFEmJ2HptvL0i5veJXqOGrCroutbJNTeKo")
OWNER = os.getenv("OWNER","6266348511")

# pyrogram client
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
) 
@app.on_message(filters.command(["image", "img"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> Bɢᴛ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:
        
        await app.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
