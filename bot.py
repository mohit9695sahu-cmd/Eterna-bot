if __name__ == "__main__":
    # Naya Cleanup Mechanism
    try:
        bot.remove_webhook()
        # Telegram ko thoda time dein purana session hatane ke liye
        time.sleep(2) 
    except Exception as e:
        print(f"Cleanup error: {e}")
    
    # ... baki ka code yahan rahega ...
import telebot
import requests
import time
import threading
import os
import json
import websocket
from flask import Flask

# --- CONFIGURATION ---
API_TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'
CHAT_ID = '5126384362'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "ETERNA V18 SHADOW-NODE IS ACTIVE."

def run_web_server():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- GLOBAL SYSTEM MEMORY ---
class SystemState:
    def __init__(self):
        self.whale_alerts_count = 0
        self.market_chaos_level = "LOW"
        self.last_heartbeat = time.time()
        self.heartbeat_interval = 10800 

system_state = SystemState()

# --- COMMANDS FOR STABILITY ---
@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "🌌 **SHADOW-NODE IS ONLINE & SCANNING...**\nSystem is stable.")

# --- PHASE 1: GHOST WALLET TRACKING ---
def on_message(ws, message):
    try:
        data = json.loads(message)
        if 'data' in data:
            trade = data['data']
            symbol = trade['s']
            price = float(trade['p'])
            quantity = float(trade['q'])
            is_buyer_maker = trade['m'] 
            usd_value = price * quantity
            
            if usd_value > 150000:
                system_state.whale_alerts_count += 1
                action = "🔴 SHORTS" if is_buyer_maker else "🟢 LONGS"
                alert_msg = f"🚨 **GHOST WALLET** 🚨\nAsset: {symbol}\nValue: ${usd_value:,.2f}\nAction: {action}"
                bot.send_message(CHAT_ID, alert_msg)
    except Exception as e:
        print(f"Stream Error: {e}")

def on_error(ws, error): print(f"⚠️ Websocket Error: {error}")
def on_close(ws, close_status_code, close_msg): 
    time.sleep(5)
    start_quantum_websocket()

def start_quantum_websocket():
    stream_url = "wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade/ethusdt@aggTrade/solusdt@aggTrade/bnbusdt@aggTrade"
    ws = websocket.WebSocketApp(stream_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever()

# --- PHASE 2: ADAPTIVE HEARTBEAT ---
def eterna_heartbeat_core():
    while True:
        try:
            current_time = time.time()
            if current_time - system_state.last_heartbeat >= system_state.heartbeat_interval:
                bot.send_message(CHAT_ID, "🔄 **ETERNA STATUS: ACTIVE**\nMonitoring market bloodline.")
                system_state.last_heartbeat = time.time()
        except: pass
        time.sleep(60)

# --- SYSTEM IGNITION ---
if __name__ == "__main__":
    # 1. Kill old connections
    try: bot.remove_webhook()
    except: pass
    
    # 2. Launch Threads
    threading.Thread(target=run_web_server, daemon=True).start()
    threading.Thread(target=eterna_heartbeat_core, daemon=True).start()
    threading.Thread(target=start_quantum_websocket, daemon=True).start()
    
    # 3. Final Polling
    print("🚀 ETERNA V18: SYSTEM LIVE.")
    bot.infinity_polling(none_stop=True, interval=0)
