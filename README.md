<div align="center">

<img src="https://raw.githubusercontent.com/SUDEEPBOTS/aniyamusic/main/assets/banner.png" alt="AniyaMusic Banner" width="100%" style="border-radius: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);" />

# 🌸 AniyaMusic Engine
### Next-Generation Telegram Voice Chat Music & Video Streaming Platform

[![CI Status](https://github.com/SUDEEPBOTS/aniyamusic/actions/workflows/ci.yml/badge.svg)](https://github.com/SUDEEPBOTS/aniyamusic/actions)
[![Docker Validation](https://github.com/SUDEEPBOTS/aniyamusic/actions/workflows/docker.yml/badge.svg)](https://github.com/SUDEEPBOTS/aniyamusic/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pyrogram v2](https://img.shields.io/badge/Pyrogram-v2.0-blue?logo=telegram)](https://github.com/KurimuzonAkuma/pyrogram)
[![PyTgCalls](https://img.shields.io/badge/PyTgCalls-v0.9.7-orange)](https://github.com/pytgcalls/pytgcalls)
[![Database](https://img.shields.io/badge/MongoDB-Atlas%20Ready-47A248?logo=mongodb&logoColor=white)](https://cloud.mongodb.com)
[![Support Group](https://img.shields.io/badge/Community-Telegram-0088cc?logo=telegram&logoColor=white)](https://t.me/+N08m5L1mCTU2NTE1)
[![Channel](https://img.shields.io/badge/Updates-Telegram-0088cc?logo=telegram&logoColor=white)](https://t.me/heartstealer_x)

<p align="center">
  <a href="#-key-features"><b>Features</b></a> •
  <a href="#-architecture--audio-pipeline"><b>Architecture</b></a> •
  <a href="#-one-click-deployment"><b>Deploy</b></a> •
  <a href="#-vps-manual-installation"><b>VPS Guide</b></a> •
  <a href="#-environment-configuration"><b>Config</b></a> •
  <a href="#-command-catalog"><b>Commands</b></a> •
  <a href="https://sudeepbots.github.io/aniyamusic/"><b>Web Studio</b></a>
</p>

---

</div>

## 📖 Overview

**AniyaMusic** is an ultra-fast, asynchronous, enterprise-grade music and video bot engine engineered specifically for Telegram Voice Chats and Video Streams. Built on top of **Pyrogram v2** and **PyTgCalls**, it bridges YouTube, Spotify, Apple Music, SoundCloud, and raw direct HTTP media streams straight into group calls with pristine **48kHz / 320kbps Opus stereo fidelity** and zero audio stutter.

Designed for scalability, AniyaMusic supports clusters with hundreds of thousands of concurrent community members, backed by **MongoDB Atlas**, automated queue persistence, multi-language localization, dynamic live seeking, and anti-flood protection.

---

## ✨ Key Features

- ⚡ **Zero-Buffering Raw Stream Pipeline**: Employs FFmpeg multi-threaded asynchronous pipe streaming for instantaneous voice chat playback.
- 🌐 **Multi-Platform Audio Resolvers**:
  - **YouTube & YouTube Music**: Seamless track, artist, album, and public playlist parsing.
  - **Spotify**: Resolves tracks, albums, artist catalogues, and private/public playlists.
  - **Apple Music & SoundCloud**: Deep audio scraper resolvers.
  - **Telegram Direct Audio**: Stream audio/video files directly uploaded to any Telegram chat or channel.
  - **Live Streams**: Supports 24/7 radio streams, M3U8 IPTV manifests, and YouTube live broadcasts.
- 📹 **1080p Full HD Video Streaming**: Native group video chat broadcasting with dynamic frame scaling and hardware-accelerated transcoding.
- 🎛️ **Precision Playback Controls**: Real-time seeking (`/seek`), dynamic playback speed modulation (`/speed 0.5x - 2.0x`), volume scaling, shuffle, and instant track skipping.
- 🛡️ **Intelligent Anti-Flood Shield**: Defends bot infrastructure against voice chat spammers, rate-limit bans, and unauthorized token abuse.
- 🍃 **MongoDB Atlas State Storage**: Stores custom prefixes, chat language settings, sudoers, assistant session states, and saved user playlists.
- 🐳 **Containerized & Cloud Native**: Native Docker, Docker Compose, PM2, Heroku, and Render compatibility.

---

## 🏗️ Architecture & Audio Pipeline

The following diagram illustrates how AniyaMusic resolves incoming media queries into low-latency raw Opus streams inside Telegram voice calls:

```mermaid
flowchart TD
    User["👤 Telegram User (/play)"] --> Dispatcher["⚡ Pyrogram v2 Dispatcher"]
    Dispatcher --> Resolver{"🔍 Platform Resolver"}
    
    Resolver -->|YouTube Link / Query| YTDL["yt-dlp Extractor Engine"]
    Resolver -->|Spotify URL| Spot["Spotipy API Resolver"]
    Resolver -->|Apple / SoundCloud| Safone["Safone & Scraper Engine"]
    Resolver -->|Telegram File / URL| TGMedia["Telegram MTProto File Downloader"]
    
    YTDL --> FFmpeg["🎛️ FFmpeg Transcoding Pipeline (48kHz, Opus Stereo)"]
    Spot --> FFmpeg
    Safone --> FFmpeg
    TGMedia --> FFmpeg
    
    FFmpeg --> PyTgCalls["📡 PyTgCalls WebRTC Engine"]
    PyTgCalls --> VoiceChat["🔊 Telegram Group Voice Chat (Zero Latency)"]
    
    Dispatcher -.-> StateDB[("🍃 MongoDB Atlas State & Queues")]
    Dispatcher -.-> FloodShield["🛡️ Anti-Flood / Rate Limiter"]
```

---

## 🚀 One-Click Deployment

Deploy your personal instance of AniyaMusic instantly using our pre-configured cloud templates:

<div align="center">

### Deploy to Heroku
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/SUDEEPBOTS/aniyamusic)

### Deploy to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

</div>

---

## 🐳 Docker Deployment

Run AniyaMusic locally or on any server with a single command:

```bash
# 1. Clone repository
git clone https://github.com/SUDEEPBOTS/aniyamusic.git
cd aniyamusic

# 2. Configure environment
cp sample.env .env
nano .env  # Enter your credentials

# 3. Start container with Docker Compose
docker compose up -d --build

# 4. View live logs
docker compose logs -f
```

---

## 🖥️ VPS Manual Installation

### 1. Prerequisites (Ubuntu / Debian)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git ffmpeg aria2 curl nodejs npm -y
```

### 2. Clone & Setup Repository

```bash
git clone https://github.com/SUDEEPBOTS/aniyamusic.git
cd aniyamusic

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip & install dependencies
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

### 3. Generate Pyrogram String Session

You need a Pyrogram v2 string session for your assistant account. Run:
```bash
python3 -c '
from pyrogram import Client
api_id = int(input("API_ID: "))
api_hash = input("API_HASH: ")
with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
    print("\nYOUR STRING_SESSION:\n", app.export_session_string())
'
```

### 4. Configure Variables

```bash
cp sample.env .env
nano .env
```

### 5. Launch using PM2 Process Manager

```bash
# Install PM2 globally
npm install -g pm2

# Start AniyaMusic
pm2 start start --name "aniyamusic"

# Save configuration to survive system reboots
pm2 save
pm2 startup
```

---

## ⚙️ Environment Configuration

All settings can be declared inside your `.env` file or cloud platform environment dashboard:

| Variable | Description | Mandatory | Example |
| :--- | :--- | :---: | :--- |
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) | **Yes** | `1234567` |
| `API_HASH` | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | **Yes** | `a1b2c3d4e5f6g7h8...` |
| `BOT_TOKEN` | Bot token created with [@BotFather](https://t.me/BotFather) | **Yes** | `7123456789:AAF...` |
| `MONGO_DB_URI` | MongoDB Atlas database connection string | **Yes** | `mongodb+srv://user:pass@cluster...` |
| `STRING_SESSION` | Pyrogram v2 String Session for assistant account | **Yes** | `BQB...` |
| `OWNER_ID` | Telegram user ID of the primary bot developer/owner | **Yes** | `6889753421` |
| `LOGGER_ID` | Telegram log group ID (with `-100` prefix) | **Yes** | `-1001234567890` |
| `SPOTIFY_CLIENT_ID` | Spotify Developer Client ID | Optional | `4c8...` |
| `SPOTIFY_CLIENT_SECRET` | Spotify Developer Client Secret | Optional | `91e...` |
| `DURATION_LIMIT` | Maximum permitted track length in minutes | Optional | `300` |
| `AUTO_LEAVING_ASSISTANT` | Automatically leave chats when inactive | Optional | `True` |

---

## 🎮 Command Catalog

### 🎵 Playback Commands (All Members)

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `/play` | `<song / query / url>` | Streams the requested song into active voice chat |
| `/vplay` | `<video / query / url>` | Streams high-definition video synced with audio |
| `/queue` | — | Displays the pending track queue with timestamps |
| `/song` | `<name>` | Downloads an MP3 audio file straight to the chat |
| `/video` | `<name>` | Downloads an MP4 video file straight to the chat |
| `/cplay` | `<channel_id> <song>` | Streams audio into a linked channel voice chat |

### 🛠️ Admin Voice Chat Controls

| Command | Description |
| :--- | :--- |
| `/pause` | Temporarily pauses current stream |
| `/resume` | Resumes paused stream |
| `/skip` | Skips current track to the next queued item |
| `/end` or `/stop` | Terminates streaming and clears current queue |
| `/seek` `<seconds>` | Seeks forward or backward in current track |
| `/speed` `<0.5 - 2.0>` | Adjusts active playback speed dynamically |
| `/shuffle` | Randomizes track order in playlist |
| `/loop` `<count>` | Loops current song or active playlist |

### 👑 Sudo / Owner Commands

| Command | Description |
| :--- | :--- |
| `/stats` | Displays bot resource usage, CPU, RAM, active voice chats |
| `/broadcast` `<text>` | Broadcasts announcement across all registered groups |
| `/restart` | Restarts bot process and reconnects voice clients |
| `/maintenance` | Toggles maintenance lock mode |

---

## 🛡️ Security & Disclosures

If you discover a security vulnerability within AniyaMusic, please review our [Security Policy](.github/SECURITY.md). Do not file public GitHub issues for security matters. Instead, contact [@heartstealer_x](https://t.me/heartstealer_x) directly.

---

## 💖 Contributing & Sponsorship

We love community contributions! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

To support ongoing development and server infrastructure, consider sponsoring through:
- **GitHub Sponsors**: [SUDEEPBOTS](https://github.com/sponsors/SUDEEPBOTS)
- **Telegram Support Community**: [Join Community](https://t.me/+N08m5L1mCTU2NTE1)

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for complete terms.

```text
Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
```
