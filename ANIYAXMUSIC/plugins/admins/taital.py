# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import aiohttp
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
import config
from ANIYAXMUSIC import app

# --- RAW API CALLER (FOR BOT API 9.5 HACK) ---
async def raw_api_request(method: str, payload: dict):
    # Get Bot Token from config or app
    token = getattr(config, "BOT_TOKEN", getattr(app, "bot_token", None))
    url = f"https://api.telegram.org/bot{token}/{method}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                return await resp.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None

# --- PREMIUM HACK INJECTION (COLORED BUTTON) ---
async def inject_premium_markup(chat_id, message_id, markup):
    payload = {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": markup}}
    await raw_api_request("editMessageReplyMarkup", payload)

# --- COMMAND HANDLER ---
@app.on_message(filters.command(["settag", "settital", "settitle"], prefixes=["/", "."]) & filters.group)
async def set_tag_or_title(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # 0. STRICT ADMIN CHECK (Only Admins and Owner can use this)
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply_text("❌ **ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.**")
    except Exception:
        return await message.reply_text("❌ **ꜰᴀɪʟᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ ᴀᴅᴍɪɴ ꜱᴛᴀᴛᴜꜱ.**")

    # 1. Check if user replied to someone
    if not message.reply_to_message:
        return await message.reply_text("❌ **ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴇᴛ ᴛʜᴇɪʀ ᴛᴀɢ ᴏʀ ᴛɪᴛʟᴇ.**")
        
    target_user = message.reply_to_message.from_user
    if not target_user:
        return await message.reply_text("❌ **ᴄᴏᴜʟᴅ ɴᴏᴛ ɪᴅᴇɴᴛɪꜰʏ ᴛʜᴇ ᴜꜱᴇʀ.**")
        
    # 2. Extract the text (tag or title)
    if len(message.command) < 2:
        return await message.reply_text("❌ **ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴛᴇxᴛ.**\n<blockquote>ᴇxᴀᴍᴘʟᴇ: `/settag ᴠɪᴘ` ᴏʀ `.settitle ʙᴏꜱꜱ`</blockquote>")
        
    text_value = message.text.split(None, 1)[1]
    
    # Telegram limit is 16 characters for both tags and titles
    if len(text_value) > 16:
        return await message.reply_text("❌ **ᴛᴇxᴛ ᴄᴀɴɴᴏᴛ ʙᴇ ʟᴏɴɢᴇʀ ᴛʜᴀɴ 16 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ!**")
        
    cmd = message.command[0].lower()
    target_user_id = target_user.id
    
    load_msg = await message.reply_text("<emoji id='6334789677396002338'>⏱</emoji> **ᴘʀᴏᴄᴇꜱꜱɪɴɢ ʀᴇQᴜᴇꜱᴛ...**")
    
    # 3. Choose the API Method based on Command
    if cmd == "settag":
        # NEW API 9.5 METHOD: For Regular Members
        payload = {"chat_id": chat_id, "user_id": target_user_id, "tag": text_value}
        res = await raw_api_request("setChatMemberTag", payload)
        action_name = "ᴛᴀɢ"
    else:
        # EXISTING METHOD: For Admins
        payload = {"chat_id": chat_id, "user_id": target_user_id, "custom_title": text_value}
        res = await raw_api_request("setChatAdministratorCustomTitle", payload)
        action_name = "ᴛɪᴛʟᴇ"
        
    # 4. Handle Response & Send Message
    if res and res.get("ok"):
        success_text = (
            f"<emoji id='5375434433195164090'>✨</emoji> **ꜱᴜᴄᴄᴇꜱꜱ!**\n\n"
            f"<blockquote><emoji id='6334333036473091884'>📌</emoji> ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ᴛʜᴇ **{action_name}** ꜰᴏʀ {target_user.mention} ᴛᴏ:\n"
            f"**`{text_value}`**</blockquote>"
        )
        
        await load_msg.edit_text(success_text)
        
        # Inject the Red (Danger) Premium Close Button
        buttons = [
            [
                {"text": "ᴄʟᴏꜱᴇ", "callback_data": "close", "style": "danger", "icon_custom_emoji_id": "6334598469746952256"}
            ]
        ]
        await inject_premium_markup(chat_id, load_msg.id, buttons)
        
    else:
        error_desc = res.get("description", "Unknown API Error") if res else "Request Failed"
        
        # Display helpful error messages for common issues
        if "not enough rights" in error_desc.lower() or "can't manage tags" in error_desc.lower():
            reason = "ʙᴏᴛ ɴᴇᴇᴅꜱ 'ᴍᴀɴᴀɢᴇ ᴛᴀɢꜱ' ᴏʀ 'ᴘʀᴏᴍᴏᴛᴇ ᴀᴅᴍɪɴꜱ' ᴘᴇʀᴍɪꜱꜱɪᴏɴ."
        elif "emoji" in error_desc.lower():
            reason = "ᴛᴇʟᴇɢʀᴀᴍ ᴅᴏᴇꜱɴ'ᴛ ᴀʟʟᴏᴡ ᴇᴍᴏᴊɪꜱ ɪɴ ᴛᴀɢꜱ/ᴛɪᴛʟᴇꜱ."
        elif "not an administrator" in error_desc.lower():
            reason = "ᴜꜱᴇʀ ᴍᴜꜱᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ʜᴀᴠᴇ ᴀ ᴛɪᴛʟᴇ."
        else:
            reason = error_desc
            
        await load_msg.edit_text(f"❌ **ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴇᴛ {action_name}**\n\n<blockquote>`{reason}`</blockquote>")
      
