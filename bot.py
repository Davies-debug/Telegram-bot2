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
    "@paradisduscam",
    "@blackwolfgroupe",
    "@chezmyflunch",
    "@vagabod",
    "@commecheztoi",
    "@LaLoiDuTalion",
    "@chezlocalbusnessChat",
    "@Aidefinaciere",
    "@CHEZSMAKA",
    "@aidefinancieres",
    "@chezdalton",
    "@chezbenzema",
    "@cheznyzoo",
    "@chezmekoi",
    "@ChezYtem",
    "@xbetcoupon90",
    "@groupeinfopositive",
    "@argentgratuitparrainage",
    "@prronooos",
    "@LACRIZ_OMIC",
    "@chezelea",
    "@chezelproffesor75",
    "@chezkaisencard"
]

NEW_CAPTION = "Canal du boss"

async def main():
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        print("Modification des messages...")
        for chat_id in CHAT_IDS:
            try:
                async for message in client.iter_messages(chat_id, limit=100):
                    if message.buttons or message.media:
                        try:
                            await client.edit_message(
                                chat_id,
                                message.id,
                                text=NEW_CAPTION,
                                buttons=None,
                                file=message.media
                            )
                            print(f"Message modifie dans {chat_id}")
                            break
                        except Exception as e:
                            print(f"Erreur edition {chat_id}: {e}")
                            break
            except Exception as e:
                print(f"Erreur pour {chat_id}: {e}")
            await asyncio.sleep(5)
        print("Termine!")

asyncio.run(main())
