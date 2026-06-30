import telebot
import time
import threading
import os
import json
import websocket
from flask import Flask

# --- CONFIGURATION ---
API_TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'  # Apna original Token yahan rakhein
CHAT_ID = '5126384362'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# --- WEB SERVER (Render ke liye zaroori) ---
@app.route('/')
def home():
    return "ETERNA V18 - STATUS: ONLINE"

def run_web_server():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- GHOST WALLET TRACKING ---
def on_message(ws, message):
    try:
        data = json.loads(message)
        if 'data' in data:
            trade = data['data']
            # USD Value calculation
            usd_value = float(trade['p']) * float(trade['q'])
            if usd_value > 150000:
                action = "🔴 SHORTS" if trade['m'] else "🟢 LONGS"
                bot.send_message(CHAT_ID, f"🚨 **WHALE ALERT**\nAsset: {trade['s']}\nValue: ${usd_value:,.2f}\nAction: {action}")
    except: pass

def start_quantum_websocket():
    # Binance streaming URL
    stream_url = "wss://data.binance.vision/ws/btcusdt@aggTrade/ethusdt@aggTrade/solusdt@aggTrade"
    ws = websocket.WebSocketApp(stream_url, on_message=on_message)
    ws.run_forever()

# --- SYSTEM IGNITION ---
if __name__ == "__main__":
    # 1. Cleanup old webhook (Conflict se bachne ke liye)
    try: bot.remove_webhook()
    except: pass
    
    # 2. Start Web Server in background
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # 3. Start WebSocket Tracking in background
    threading.Thread(target=start_quantum_websocket, daemon=True).start()
    
    # 4. Start Bot Polling
    print("🚀 ETERNA V18: SYSTEM LIVE.")
    bot.infinity_polling(none_stop=True)
