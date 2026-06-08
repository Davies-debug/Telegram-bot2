import requests
import json

TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"

CHAT_IDS = [
    "@fltangohawai",
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

message = (
    "<b>Marre de ne pas savoir c**all ou poser des ch*eques, "
    "le canal de Arjeen est votre solution.</b> \U0001F624\n\n"
    "\U0001F381 <b>PAS ENORMEMENT DE PREREQUIS NECESSAIRES</b>\n"
    "\U0001F4DE <b>SUPPORT REACTIF 24/7</b>\n\n"
    "<blockquote>FORMATIONS INCLUS</blockquote>\n\n"
    "- Formation ch*eque (suivi complet)\n"
    "- Formation c**all (suivi complet)\n"
    "- Formation spam (suivi complet)\n"
    "- Tech Iphone (suivi accompagne)\n"
    "- Tech amex (suivi complet)\n"
    "- Tech sncf - 90% (forma complete)\n\n"
    "<blockquote>COMBIEN JE PEUX FAIRE ?</blockquote>\n\n"
    "\U0001F4B6 Investissement : entre 50 - 150 euros\n"
    "\U0001F4B0 Gains potentiels : 1-10k/day"
)

keyboard = {
    "inline_keyboard": [
        [{"text": "SUPPORT", "url": "https://t.me/arjeenuhq"}],
        [{"text": "CANAL 1", "url": "https://t.me/arjeenasauter"}],
        [{"text": "CANAL 2", "url": "https://t.me/arjeenvouches1"}]
    ]
}

for chat_id in CHAT_IDS:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML",
            "reply_markup": json.dumps(keyboard)
        }
    )
    print(f"Message envoye a {chat_id}")
