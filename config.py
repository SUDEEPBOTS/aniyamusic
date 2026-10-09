# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ── Telegram Credentials ───────────────────────────────────────────────────
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Kaito_3_2")
BOT_USERNAME = getenv("BOT_USERNAME", "IAM_MIMBOT")
BOT_NAME = getenv("BOT_NAME", "AniyaMusic")
ASSUSERNAME = getenv("ASSUSERNAME", "Kaito_3_2")
GROQ_API_KEY = getenv("GROQ_API_KEY", "")

# ── Database ───────────────────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# ── Playback Limits ────────────────────────────────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", "0"))
OWNER_ID = int(getenv("OWNER_ID", "0"))

# ── Cloud & Deployment ─────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SUDEEPBOTS/aniyamusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+N08m5L1mCTU2NTE1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/heartstealer_x")

# ── Assistant & Autoplay ───────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# ── Spotify API ────────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ── Pyrogram String Sessions ───────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ── UI Images ──────────────────────────────────────────────────────────────
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/ah5y0f.jpeg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/bj5s8s.jpeg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/5346f8d3e34f85855176b-8f3a38df6c805fb7d7.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8rmrd9.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2vq8oz.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2vq8oz.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/2vq8oz.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
