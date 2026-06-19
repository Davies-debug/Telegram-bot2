import requests
import json

TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"

CHAT_ID = -1004291062323
MESSAGE_ID = 21

NEW_CAPTION = """@brokeonpaperr aka Fayz le c*alleur et sp*ammeur le plus uhq, est de retour ! \U0001F4DE

\u00c0 PROPOS DES C*C ?

T'as b'soin d'buy des c*c fr, \u00e9trang\u00e8res, DOM-TOM, etc\u2026 j'ai tout c'qu'il te faut, mon fr\u00e9rot ! \U0001F61C 

- Des rez qui sell full c*c chaque matin, pas d'no rep ou d'c*c dead, j'ai uniquement d'la qualit\u00e9 ! \U0001F4B3

- Jeune spammeur actif 24/7, vous pouvez r\u00e9sa tous les jours, chaque matin y'a un nouvel arrivage, je cautionne aucun retard donc ne vous inqui\u00e9tez pas, vous serez servi (j'fais pas l'taff \u00e0 moiti\u00e9). \U0001F3C3

(BOT EN COURS DE CR\u00c9ATION)\u2026. \u23F3\uFE0F

\u00c0 PROPOS DU C*ALL ?

T'as d'la c*c fresh \u00e0 call, tu c*all pas ou t'as pas d'calleur dispo aux environs ? Viens directement en mp ! @brokeonpaperr \u2709\uFE0F

- J'call sous onoff 01 w/sender mail & sms, j'ai tout c'qu'il me faut niveau rib, etc\u2026 donc niveau matos ne vous inqui\u00e9tez pas ! \U0001F634

- CALL LIVE ON ! \u2705"""

result = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/editMessageCaption",
    data={
        "chat_id": CHAT_ID,
        "message_id": MESSAGE_ID,
        "caption": NEW_CAPTION,
        "reply_markup": json.dumps({"inline_keyboard": []})
    }
).json()

print(result)
