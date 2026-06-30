import telebot
import threading
from flask import Flask
import os

# --- INITIALIZATION ---
# Token ko yahan hardcode karein ya Render ke Environment Variables mein set karein
TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- WEB SERVER ---
@app.route('/')
def home():
    return "ETERNA V18 IS ACTIVE"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

# --- BOT LOGIC ---
@bot.message_handler(commands=['start', 'status'])
def send_welcome(message):
    bot.reply_to(message, "System is online and running smoothly.")

if __name__ == "__main__":
    # 1. Web server ko background mein start karein
    threading.Thread(target=run_web, daemon=True).start()
    
    # 2. Cleanup (Webhook hatana)
    try:
        bot.delete_webhook()
    except Exception as e:
        print(f"Cleanup error: {e}")
    
    # 3. Polling start karein
    print("🚀 ETERNA V18: SYSTEM LIVE.")
    bot.infinity_polling(none_stop=True, skip_pending=True)
