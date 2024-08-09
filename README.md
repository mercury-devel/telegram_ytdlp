# YtDlp Telegram Bot

![Баннер](https://i.ibb.co/nwnrB9H/icon.png)

# 📖 Description
This bot can download:
- Photos and videos from Instagram, Tik Tok.
- Videos (with quality selection) and audio (in the best quality) from YouTube.
- Music from SoundCloud.

# ⚙️ Project Setup Guide

Welcome to the project setup guide! Follow these steps to configure and run the project, whether you're using Python or Docker.

## Getting Started

### 1. Configure Cookies

To enhance the scraping of YouTube and Instagram, you need to provide Netscape cookies. Place your cookies in the following files:
- `cookies/insta.txt` for Instagram
- `cookies/youtube.txt` for YouTube

### 2. Create and Configure Your Telegram Channel

1. **Create a Telegram Channel:** 
   You need a Telegram channel to make your bot popular. People can use your bot by joining this channel.

2. **Add Your Bot to the Channel:**
   - Create a Telegram bot.
   - Add the bot to your newly created channel.

3. **Create a Telegram App:**
   - Go to [Telegram API Development Tools](https://my.telegram.org/apps).
   - Create your app and get your `API_ID` and `API_HASH`.

### 3. Configure Environment Variables

Add the following information to your `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=your_channel_id (ex. -100123123123) 
CHANNEL_LINK=your_channel_link (ex. t.me/***)
API_ID=your_telegram_app_api_id
API_HASH=your_telegram_app_api_hash
ADMIN_LIST=123, 456(where are 123 and 456 - telegram ids of admins)
```

## Setup Instructions

1. **Install Docker**

   Follow the instructions on [Docker's official installation guide](https://docs.docker.com/engine/install/).

2. **Run Docker Setup Menu**

   Execute the following command to start the Docker setup menu:

   ```bash
   sh run.sh
   ```

   Using Docker, you can:
   - Build the project
   - Create and start a container
   - Stop the container
   - Restart the container
   - Remove the container
   - Show container logs

## Notes

- Ensure that your `.env` file is properly configured with the correct values.
- Follow Docker's documentation for any additional configuration or troubleshooting.

# 🚀 Usage

Type /start then paste your link to video on youtube, instagram, tik tok etc

If you are in admin list, type /admin. There is a message sender. It sends your message to all users in your bot!

# 💰 Support My Work

If you like what I do and want to support me, consider making a Bitcoin donation!

**Bitcoin:**

`bc1qhpegcfz6ynmksff95wj9e4kva89d95syyqk3l4`

**USDT/TRC20:**

`TRJxipxAswjj9A7RuvUFx1ShfmZ3JLhi2r`


**TON:**

`EQCwp7u30xT9gmWfcruTP45gLlG66fi1ySGthYcasAss05uR`
