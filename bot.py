import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 37266230
API_HASH = "c9f95b37dd021863d56426d500cc7227"
SESSION_STRING = "1BJWap1sBuyzcNSHdTsnCH--Dpkzr8i2DwNRl9lpMpMcjl-gEe_mKfdahQzc1PQdv5EW-eHbNngi3Os1Ap2Rqy8g5sd2mzEMjvqC8Rxp3xKujADHimNYdUkUAuna0-gtx-wX_LscedcI1sRo1pTtMa2_Rqjmc9Y6gWAt8GJXSOOgOSVccnqKOyt_N9aYcpFjkWarwTAdScngk2wJrqXLPdFNKVInyojgSlFvG22Oa5lME7NBnCje8u9-VPhRAuWurlldUOuIIda79ratu2Nuef_3jZ4A6ZhvPdG0-JqFEzqs9i8JK_ppuPE_fktROaF7rjPr_Zz-6a2XGnLhC2_z5FFXuINQVObw="

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
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
        last_message = messages[0]
        for chat_id in CHAT_IDS:
            try:
                await client.forward_messages(chat_id, last_message)
                print(f"Message transfere a {chat_id}")
            except Exception as e:
                print(f"Erreur pour {chat_id}: {e}")

asyncio.run(main())
