import requests

TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"

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

message = """Marre de galerer toute la journee? 
Le canal d Arjeen est votre solution !

PAS ENORMEMENT DE PREREQUIS NECESSAIRES
SUPPORT REACTIF 24/7

FORMATIONS INCLUS
- Formation cheque (suivi complet)
- Formation call (suivi complet)
- Formation spam (suivi complet)
- Tech Iphone (suivi accompagne)
- Tech amex (suivi complet)
- Tech sncf - 90% (forma complete)

COMBIEN JE PEUX FAIRE?
Investissement : entre 50 - 150 euros
Gains potentiels: 1-10k/day

CONTACT : @arjeenuhq
CANAL : @arjeenasauter
CANAL VOUCHES : @arjeenvouches1"""

for chat_id in CHAT_IDS:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": message
        }
    )
    print(f"Message envoye a {chat_id}")
