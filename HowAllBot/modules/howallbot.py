import random 
from HowAllBot import app
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)



@app.on_inline_query()
async def _app(_, inlinequery):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
    results=[
        InlineQueryResultArticle(
        title = "💋 ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",
        input_message_content=InputTextMessageContent(
          f"💋 I ᴀᴍ {random.randint(1,100)}% ʜᴏʀɴʏ .",)
        
        description = "ғɪɴᴅ ᴏᴜᴛ ʜᴏᴡ ʜᴏʀɴʏ ʏᴏᴜ ᴀʀᴇ !",        
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Share your hornyness! 🔥",switch_inline_query="")]])
                                                                                                                                                                                                                                                                                                                                                            
     )],
     cache_time=1)
    
    
