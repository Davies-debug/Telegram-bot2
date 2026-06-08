import requests

TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"

CHAT_IDS = [
    "@testbotsp",
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

IMAGE_URL = "https://i.ibb.co/HvDPwwk/image.jpg"

message = u"""
\U0001F525 Marre de galerer toute la journee? \U0001F525

Le canal d Arjeen est votre solution ! \U0001F4AA

\U00002705 PAS ENORMEMENT DE PREREQUIS NECESSAIRES
\U0001F5E3 SUPPORT REACTIF 24/7

\U0001F4DA FORMATIONS INCLUS
- Formation cheque (suivi complet)
- Formation call (suivi complet)
- Formation spam (suivi complet)
- Tech Iphone (suivi accompagne)
- Tech amex (suivi complet)
- Tech sncf - 90% (forma complete)

\U0001F4B0 COMBIEN JE PEUX FAIRE?
\U0001F4B6 Investissement : entre 50 - 150 euros
\U0001F4B8 Gains potentiels: 1-10k/day

\U0001F4F2 CONTACT : @arjeenuhq
\U0001F4E2 CANAL : @arjeenasauter
\U0001F3C6 CANAL VOUCHES : @arjeenvouches1"""

for chat_id in CHAT_IDS:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": chat_id,
            "photo": IMAGE_URL,
            "caption": message
        }
    )
    print(f"Message envoye a {chat_id}")
