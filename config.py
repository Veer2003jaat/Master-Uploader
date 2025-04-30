import os

class Config(object):
    BOT_TOKEN = os.environ.get("7610944579:AAHG3CTF9zWo2mRGXuXpRhcGdKkTXU1m6Qc")
    API_ID = int(os.environ.get("12475131"))
    API_HASH = os.environ.get("719171e38be5a1f500613837b79c536f")
    AUTH_USER = os.environ.get('AUTH_USERS', '5121141243').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ 𝐉𝐨𝐡𝐧 𝐖𝐢𝐜𝐤 ꧂](https://t.me/Dc5txt_bot)"
