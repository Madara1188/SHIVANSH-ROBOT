import secureme
from pyrogram import filters
from MukeshRobot import pbot as mukesh


@mukesh.on_message(filters.command("encrypt") & filters.private)
async def encyrpt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/encyrpt India`")
    m = message.text.split(' ',1)[1]
    try:
        Secure = secureme.encrypt(m)
        
        await message.reply_text(f"`{Secure}`")
        

    except Exception as e:
        await message.reply_text(f"Error {e}")

@mukesh.on_message(filters.command("decrypt") & filters.private)
async def decrypt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/decrypt Nsinf`")
    m = message.text.split(' ',1)[1]
    try:
        Decrypt = secureme.decrypt(m)
        
        await message.reply_text(f"`{Decrypt}`")
        

    except Exception as e:
        await message.reply_text(f"{e}")
