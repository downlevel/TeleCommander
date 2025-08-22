# Telecommander

A simple Telegram bot to run predefined system commands on your server via button clicks.

⚠️ **Warning:** This bot can control your server. Only use it for safe, predefined commands and restrict it to your own Telegram ID.

---

## 🚀 Features
- Secure access (restricted to your Telegram user ID).
- Easy to extend by editing `commands.json`.
- Uses Telegram inline buttons (no free text commands).
- Keeps sensitive data in `.env`.

---

## 📂 Project Structure

telecommander/
│── bot.py # Main bot code
│── commands.json # List of allowed commands
│── .env # Secrets (bot token & allowed user ID)
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## ⚙️ Setup Instructions

1. **Clone the repo** (or copy files):
   ```bash
   git clone https://github.com/downlevel/TeleCommander.git
   cd TeleCommander


2. **Install dependencies**:

pip install -r requirements.txt


3. **Create .env**:

BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
ALLOWED_USER_ID=123456789


4. **Edit commands.json to define allowed commands**:

{
  "start_nginx": {
    "label": "Start Nginx",
    "command": "systemctl start nginx"
  },
  "stop_nginx": {
    "label": "Stop Nginx",
    "command": "systemctl stop nginx"
  }
}


5. **Run the bot**:

python bot.py
