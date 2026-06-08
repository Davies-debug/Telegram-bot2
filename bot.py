import requests
import json

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

IMAGE_URL = "https://i.ibb.co/9H9W2Bht/image.jpg"

message = u"""\U0001F525 <b>Marre de ne pas faire d argent ? Le canal de Arjeen est votre solution</b> \U0001F525

\U00002705 <b>PAS ENORMEMENT DE PREREQUIS NECESSAIRES</b>
\U0001F5E3 <b>SUPPORT REACTIF 24/7</b>

<blockquote>\U0001F4DA FORMATIONS INCLUS
- \U0001F4DD Formation cheque (suivi complet)
- \U0001F4DE Formation call (suivi complet)
- \U0001F4E7 Formation spam (suivi complet)
- \U0001F4F1 Tech Iphone (suivi accompagne)
- \U0001F4B3 Tech amex (suivi complet)
- \U0001F682 Tech sncf - 90% (forma complete)</blockquote>

\U0001F4B0 COMBIEN JE PEUX FAIRE?
\U0001F4B6 Investissement : entre 50 - 150 euros
\U0001F4B8 Gains potentiels: 1-10k/day"""

keyboard = {
    "inline_keyboard": [
        [{"text": "\U0001F4F2 SUPPORT", "url": "https://t.me/arjeenuhq"}],
        [{"text": "\U0001F4E2 CANAL 1", "url": "https://t.me/arjeenasauter"}],
        [{"text": "\U0001F3C6 CANAL 2", "url": "https://t.me/arjeenvouches1"}]
    ]
}

for chat_id in CHAT_IDS:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": chat_id,
            "photo": IMAGE_URL,
            "caption": message,
            "parse_mode": "HTML",
            "reply_markup": json.dumps(keyboard)
        }
    )
    print(f"Message envoye a {chat_id}")
