TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"
CHAT_ID = "@ChezMendoza"  # ID du groupe ou canal
CHAT_ID = "@avietalpacino_pub". # ID du groupe ou canal
CHAT_ID = "@quadblade" # ID du groupe ou canal
CHAT_ID = "@chezkanoe" # ID du groupe ou canal
CHAT_ID = "@chezyatsu" # ID du groupe ou canal
CHAT_ID = "@chezalpha" # ID du groupe ou canal
CHAT_ID = "@chezz9" # ID du groupe ou canal
CHAT_ID = "@chezphineasesimsfr" # ID du groupe ou canal
CHAT_ID = "@chezdsavv" # ID du groupe ou canal
CHAT_ID = "@chezrass" # ID du groupe ou canal
CHAT_ID = "@chezdh" # ID du groupe ou canal
CHAT_ID = "@ChezObsidianV2" # ID du groupe ou canal
CHAT_ID = "@chezqui" # ID du groupe ou canal
CHAT_ID = "@creditviro261" # ID du groupe ou canal
CHAT_ID = "@pedrofabiente" # ID du groupe ou canal
CHAT_ID = "@chezZurgkennedy" # ID du froupe ou canal
CHAT_ID = "@plans_sous92" # ID du groupe ou canal
CHAT_ID = "@Chez_DuckLand" # ID du groupe ou canal
CHAT_ID = "@ChezHouse" # ID du groupe ou canal
CHAT_ID = "@chezlasolucee" # ID du groupe ou canal
CHAT_ID = "@onpaiepaslatva" # ID du groupe ou canal
CHAT_ID = "@chezlenfoiree" # ID du groupe ou canal
CHAT_ID = "in_heisenberg_house" # ID du groupe ou canal
CHAT_ID = "@CvbienspasserUHQ" # ID du groupe ou canal
CHAT_ID = "@paradisduscam" # ID du groupe ou canal


message = """Marre de galérer toute la journée? 😮‍💨"""
Le canal d'Arjeen est votre solution !

🎁 PAS ÉNORMÉMENT DE PRÉREQUIS NÉCESSAIRES
🗣️ SUPPORT REACTIF 24/7

FORMATIONS INCLUS
- Formation ch*èque (suivi complet)
- Formation c**all (suivi complet)
- Formation spam (suivi complet)
- Tech Iphone (suivi accompagné)
- Tech amex (suivi complet)
- Tech sncf - 90% (forma complète)

COMBIEN JE PEUX FAIRE?
💶 Investissement : ~ entre (50€ - 150€)
💰 Gains potentiels: ~1-10k/day

CONTACT : @arjeenuhq
CANAL : @arjeenasauter
CANAL VOUCH’S : @arjeenvouches1"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
