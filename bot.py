import os
import json
import subprocess
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))

# Load commands from external file
with open("commands.json", "r") as f:
    COMMANDS = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send button list with available commands"""
    user_id = update.effective_user.id
    if user_id != ALLOWED_USER_ID:
        await update.message.reply_text("❌ Unauthorized access!")
        return

    keyboard = [
        [InlineKeyboardButton(cmd["label"], callback_data=key)]
        for key, cmd in COMMANDS.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a command:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks and execute commands"""
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    if user_id != ALLOWED_USER_ID:
        await query.edit_message_text("❌ Unauthorized access!")
        return

    command_key = query.data
    if command_key not in COMMANDS:
        await query.edit_message_text("⚠️ Invalid command!")
        return

    label = COMMANDS[command_key]["label"]
    command = COMMANDS[command_key]["command"]

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=20
        )
        if result.returncode == 0:
            output = result.stdout.strip() or f"✅ Successfully executed: {label}"
        else:
            output = f"❌ Error:\n{result.stderr}"
    except Exception as e:
        output = f"❌ Exception: {str(e)}"

    if len(output) > 3500:
        output = output[:3500] + "\n... (output truncated)"

    await query.edit_message_text(output)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
