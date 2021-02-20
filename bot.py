import random
import os

from pyrogram import Client, filters
from PIL import Image


api_id = 123456789 #int of api id get from my.telegram.org
api_hash = " Your Api Hash Here " #str of api hash get from my.telegram.org
token = ' Your Bot Token here ' #str of token get from BotFather

bot = Client('Session_Name', api_id, api_hash, bot_token=token, workers = 4 )

START_MESSAGE = '''
😇 **Welcome to Sticker Convertor Bot**
💫 Suportted formats to convert: 
`Jpg to PNG, Sticker to PNG, Webp to PNG,  Animated Sticker to GIF`

🆔 Admin: @localhoct
You can Download Source Code on  Github.com/localhoct 🥰

**How to use?**
  Just send the file you want to convert 😁
''' #this is the message after client send /start to the bot
CAPTION = 'Coverted by @stickerConv_Bot 😬\n[Downlaod Source Code](https://Github.com/localhoct) 😈' # caption of the files

bot.set_parse_mode('md')
@bot.on_message(filters.command("start",'/'))
def start_messgae(c, m):
    m.reply_text(START_MESSAGE)

@bot.on_message(filters.photo)
def photo_convert(c, m):
    rand_id = random.randint(100,900) # generate random number between 100 to 900
    m.download(f"{m.chat.id}-{rand_id}.jpg")
    img = Image.open(f'downloads/{m.chat.id}-{rand_id}.jpg')
    img.save(f"{m.chat.id}-{rand_id}.png","PNG")
    m.reply_document(f"{m.chat.id}-{rand_id}.png",caption= CAPTION )
    os.remove(f"{m.chat.id}-{rand_id}.png")
    os.remove(f'downloads/{m.chat.id}-{rand_id}.jpg')

@bot.on_message(filters.sticker)
def conver_webp(c, m):
    rand_id = random.randint(100,900) # generate random number between 100 to 900
    if (m.sticker.is_animated) == False:
        m.download(f"{m.chat.id}-{rand_id}.webp")
        img = Image.open(f'downloads/{m.chat.id}-{rand_id}.webp').convert("RGBA")
        img.save(f"{m.chat.id}-{rand_id}.png","PNG")
        m.reply_photo(f"{m.chat.id}-{rand_id}.png",caption=CAPTION)
        m.reply_document(f"{m.chat.id}-{rand_id}.png",caption=CAPTION)
        os.remove(f"{m.chat.id}-{rand_id}.png")
        os.remove(f'downloads/{m.chat.id}-{rand_id}.webp')
    if m.sticker.is_animated == True:
        ms1 = m.reply_text("Converting...")
        ms2 = m.reply_text("🤞")
        m.download(f"{m.chat.id}-{rand_id}.tgs")
        os.system(f"lottie_convert.py downloads/{m.chat.id}-{rand_id}.tgs {m.chat.id}-{rand_id}.gif")
        m.reply_animation(f"{m.chat.id}-{rand_id}.gif",caption=CAPTION)
        ms1.delete()
        ms2.delete()
        os.remove(f"{m.chat.id}-{rand_id}.gif")
        os.remove(f'downloads/{m.chat.id}-{rand_id}.tgs')

bot.run()