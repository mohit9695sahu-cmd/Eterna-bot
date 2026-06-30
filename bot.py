import telebot
import threading
import os
import time
import json
import websocket
from flask import Flask

# --- CONFIGURATION ---
TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'
CHAT_ID = '5126384362'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- WEB SERVER ---
@app.route('/')
def home():
    return "ETERNA V18: SYSTEM FULLY OPERATIONAL"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

# --- BINANCE TRACKING ---
def on_message(ws, message):
    data = json.loads(message)
    if 'data' in data:
        trade = data['data']
        price = float(trade['p'])
        qty = float(trade['q'])
        if (price * qty) > 150000:
            side = "🟢 LONG" if not trade['m'] else "🔴 SHORT"
            bot.send_message(CHAT_ID, f"🚨 Whale Alert: {trade['s']}\nValue: ${price*qty:,.0f}\nSide: {side}")

def start_ws():
    ws = websocket.WebSocketApp("wss://data.binance.vision/ws/btcusdt@aggTrade", on_message=on_message)
    ws.run_forever()

# --- BOT POLLING ---
def run_bot():
    bot.infinity_polling(none_stop=True, skip_pending=True)

if __name__ == "__main__":
    # 1. Start Web Server
    threading.Thread(target=run_web, daemon=True).start()
    
    # 2. Start Binance WebSocket
    threading.Thread(target=start_ws, daemon=True).start()
    
    # 3. Start Bot Polling
    print("🚀 ETERNA V18: FULL SYSTEM ONLINE.")
    run_bot()
