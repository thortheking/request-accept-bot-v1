from pyrogram import Client, filters
# Assuming you have a database instance imported as 'db'
# from database import db 

@Client.on_message(filters.command("latest") & filters.incoming)
async def get_latest_movies(client, message):
    # 1. Define the languages you want to track
    languages = ["Malayalam", "Tamil", "Telugu", "Hindi", "English", "Kannada"]
    
    response_text = "🎬 **Latest Movies by Language:**\n\n"
    
    for lang in languages:
        # 2. Fetch latest 7 movies for each language from your DB
        # This is a placeholder for your actual DB query logic
        movies = await db.get_latest_files(query={"language": lang}, limit=7)
        
        if movies:
            response_text += f"**{lang}:**\n"
            for movie in movies:
                # Assuming movie object has 'title' and 'year' attributes
                response_text += f"• {movie['title']} ({movie['year']})\n"
            response_text += "\n"
    
    # 3. Handle Uncategorized or others
    response_text += "**Uncategorized:**\n"
    # Fetch movies where language is missing
    others = await db.get_latest_files(query={"language": None}, limit=7)
    for other in others:
        response_text += f"• {other['title']} ({other['year']})\n"

    await message.reply_text(response_text)
