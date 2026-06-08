import asyncio
from telethon import TelegramClient

API_ID = 37266230
API_HASH = "c9f95b37dd021863d56426d500cc7227"

CHAT_IDS = [
    "@ChezMendoza",
    "@avietalpacino_pub",
    "@quadblade",
    "@chezkanoe",
    "@chezyatsu",
    "@chezalpha",
    "@chezz9",
    "@chezphineasesimsfr",
    "@chezdsavv",
    "@chezrass",
    "@chezdh",
    "@ChezObsidianV2",
    "@chezqui",
    "@creditviro261",
    "@pedrofabiente",
    "@chezZurgkennedy",
    "@plans_sous92",
    "@Chez_DuckLand",
    "@ChezHouse",
    "@chezlasolucee",
    "@onpaiepaslatva",
    "@chezlenfoiree",
    "@in_heisenberg_house",
    "@CvbienspasserUHQ",
    "@paradisduscam"
]

SOURCE_CHANNEL = "@testbotsp"

async def main():
    async with TelegramClient("session", API_ID, API_HASH) as client:
        messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
        last_message = messages[0]
        for chat_id in CHAT_IDS:
            try:
                await client.forward_messages(chat_id, last_message)
                print(f"Message transfere a {chat_id}")
            except Exception as e:
                print(f"Erreur pour {chat_id}: {e}")

asyncio.run(main())
