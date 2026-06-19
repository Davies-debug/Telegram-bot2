import requests
import json

TOKEN = "8808320751:AAF2CgbA6Yszn8kTP2nJMTiT8r1efbff-_M"

CHAT_ID = -1004291062323
USER = "@brokeonpaperr"

result = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/promoteChatMember",
    data={
        "chat_id": CHAT_ID,
        "user_id": USER,
        "is_anonymous": False,
        "can_manage_chat": True,
        "can_post_messages": True,
        "can_edit_messages": True,
        "can_delete_messages": True,
        "can_manage_video_chats": True,
        "can_restrict_members": True,
        "can_promote_members": True,
        "can_change_info": True,
        "can_invite_users": True,
        "can_pin_messages": True,
        "can_post_stories": True,
        "can_edit_stories": True,
        "can_delete_stories": True
    }
).json()

print(result)
