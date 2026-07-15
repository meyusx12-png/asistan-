import os
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Media

# Değişkenleri ortam değişkenlerinden (environment variables) çekeriz
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "music_session")
CHAT_ID = int(os.getenv("CHAT_ID")) # Grup ID'si

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

@app.on_ready()
async def start_bot(client):
    print("Bot hazır! Müzik başlatılıyor...")
    
    # Örnek müzik linki (Kendi linkini değiştirebilirsin)
    song_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    
    try:
        await pytgcalls.play(
            chat_id=CHAT_ID,
            stream=Media(song_url)
        )
        print("Müzik grubuna gönderildi.")
    except Exception as e:
        print(f"Hata: {e}")

async def main():
    await app.start()
    await pytgcalls.start()
    
    # Sonsuz döngü ile botu canlı tut
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
