
import asyncio
import aiohttp
import json

def dummy_article(index):
    return {
        "title": f"Inter vs Barça - Noticia {index}",
        "date": "2025-05-09T21:00:00",
        "content": f"Resumen del partido Inter vs Barça número {index}..."
    }

CENTRAL_SERVER_URL = "http://localhost:8000/submit_article"

async def send_article(session, article):
    try:
        async with session.post(CENTRAL_SERVER_URL, json=article) as resp:
            print(await resp.text())
    except Exception as e:
        print(f"Failed to send article: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_article(session, dummy_article(i)) for i in range(3)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
