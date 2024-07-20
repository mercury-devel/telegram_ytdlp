# YtDlp Telegram Bot

![Баннер](https://i.ibb.co/nwnrB9H/icon.png)

# 📖 Description
This bot can download:
- Photos and videos from Instagram and Twitter.
- Videos (with quality selection) and audio (in the best quality) from YouTube.
- Music from SoundCloud.
- Videos and clips from VKontakte.

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
CHANNEL_ID=your_channel_id
CHANNEL_LINK=your_channel_link
API_ID=your_telegram_app_api_id
API_HASH=your_telegram_app_api_hash
```

## Setup Instructions

![Python](https://img.shields.io/badge/Python-%2314354C?logo=python&logoColor=white)
### Python Way

1. **Download and Install Python 3.11.9**

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   ```

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

![Docker](https://img.shields.io/badge/Docker-%232496ED?logo=docker&logoColor=white)
### Docker Way

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

