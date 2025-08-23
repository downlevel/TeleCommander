# 🤖 Telecommander

A simple Telegram bot to run predefined system commands on your server via button clicks.

⚠️ **Warning:** This bot can control your server. Only use it for safe, predefined commands and restrict it to your own Telegram ID.

---

## 🚀 Features

- ✅ Secure access (restricted to your Telegram user ID)
- ✅ Easy to extend by editing `commands.json`
- ✅ Uses Telegram inline buttons (no free text commands)
- ✅ Keeps sensitive data in `.env`

---

## 📂 Project Structure

```
telecommander/
├── bot.py              # Main bot code
├── commands.json       # List of allowed commands
├── .env               # Secrets (bot token & allowed user ID)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/downlevel/TeleCommander.git
cd TeleCommander
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Telegram Bot

1. **Start a chat with BotFather:**
   - Open Telegram and search for `@BotFather`
   - Start a conversation with `/start`

2. **Create a new bot:**
   ```
   /newbot
   ```

3. **Follow the prompts:**
   - Choose a name for your bot (e.g., "My Server Commander")
   - Choose a username ending in "bot" (e.g., "myserver_commander_bot")

4. **Save your bot token:**
   - BotFather will provide you with a token like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`
   - Keep this token secure!

### 4. Get Your Telegram User ID

**Method 1: Using @userinfobot**
1. Search for `@userinfobot` in Telegram
2. Start a chat and send any message
3. The bot will reply with your user ID

**Method 2: Using @myidbot**
1. Search for `@myidbot` in Telegram
2. Send `/getid`
3. The bot will return your user ID

### 5. Create Environment File

Create a `.env` file in the project root:

```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
ALLOWED_USER_ID=123456789
```

Replace:
- `123456789:ABCdefGHIjklMNOpqrsTUVwxyz` with your actual bot token
- `123456789` with your actual Telegram user ID

### 6. Configure Commands

Edit `commands.json` to define your allowed commands:

```json
{
  "start_nginx": {
    "label": "🟢 Start Nginx",
    "command": "systemctl start nginx"
  },
  "stop_nginx": {
    "label": "🔴 Stop Nginx",
    "command": "systemctl stop nginx"
  },
  "restart_nginx": {
    "label": "🔄 Restart Nginx",
    "command": "systemctl restart nginx"
  },
  "check_disk": {
    "label": "💾 Check Disk Usage",
    "command": "df -h"
  }
}
```

### 7. Run the Bot

```bash
python bot.py
```

---

## 🔧 Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to see available commands
3. Click on the inline buttons to execute commands
4. The bot will show the command output

---

## 🛡️ Security Notes

- **Only you can use the bot** - Access is restricted to your Telegram user ID
- **Predefined commands only** - No arbitrary command execution
- **Keep your `.env` file secure** - Never commit it to version control
- **Test commands carefully** - Ensure they're safe before adding them

---

## 📝 Example Commands

Add these to your `commands.json` for common server tasks:

```json
{
  "system_status": {
    "label": "📊 System Status",
    "command": "uptime && free -h && df -h /"
  },
  "check_processes": {
    "label": "🔍 Top Processes",
    "command": "ps aux --sort=-%cpu | head -10"
  },
  "network_info": {
    "label": "🌐 Network Info",
    "command": "ip addr show"
  }
}
```

---

## 🐛 Troubleshooting

- **Bot not responding?** Check if the bot token is correct
- **Access denied?** Verify your user ID in the `.env` file
- **Commands not working?** Test them manually in your terminal first
- **Permission errors?** Some commands may require sudo privileges

---

## 📄 License

This project is open source. Use at your own risk.
