import telebot
import requests
import time
import threading
import os
import json
import websocket
from flask import Flask

# ==========================================
# ETERNA V18 - THE SHADOW-NODE GENESIS
# ==========================================

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
        self.heartbeat_interval = 10800  # Default 3 hours

system_state = SystemState()

# ==========================================
# PHASE 1: GHOST WALLET TRACKING ENGINE
# ==========================================

def on_message(ws, message):
    """Microsecond data capture for Whale Volume (Mempool/AggTrade Snipe)"""
    try:
        data = json.loads(message)
        if 'data' in data:
            trade = data['data']
            symbol = trade['s']
            price = float(trade['p'])
            quantity = float(trade['q'])
            is_buyer_maker = trade['m'] # True = Sell (Red), False = Buy (Green)
            
            # Calculate Total USD Value of the single trade
            usd_value = price * quantity
            
            # 🚨 GHOST WALLET THRESHOLD: Order > $150,000 in a single millisecond
            if usd_value > 150000:
                system_state.whale_alerts_count += 1
                action = "🔴 SHORTS (Dumping)" if is_buyer_maker else "🟢 LONGS (Pumping)"
                force = "NEGATIVE (Bearish)" if is_buyer_maker else "POSITIVE (Bullish)"
                
                alert_msg = (
                    f"🚨 **GHOST WALLET DETECTED** 🚨\n\n"
                    f"💎 Asset: {symbol}\n"
                    f"💥 Action: Whale {action}\n"
                    f"💰 Value: ${usd_value:,.2f}\n"
                    f"🎯 Executed Price: ${price:,.2f}\n"
                    f"⚡ Vector Force: {force}\n\n"
                    f"*System Note: Smart Money is moving. Prepare for volatility.*"
                )
                bot.send_message(CHAT_ID, alert_msg)
                
                # ADAPTIVE HEARTBEAT TRIGGER: If whales are active, chaos is high
                if system_state.whale_alerts_count >= 3:
                    system_state.market_chaos_level = "HIGH (Whale Warfare)"
                    system_state.heartbeat_interval = 1800  # Shift heartbeat to 30 mins
                
    except Exception as e:
        print(f"Data Stream Error: {e}")

def on_error(ws, error):
    print(f"⚠️ Websocket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("🔴 Websocket closed. Auto-reconnecting in 5 seconds...")
    time.sleep(5)
    start_quantum_websocket()

def start_quantum_websocket():
    """Connects directly to Binance Live Trade Stream for Zero-Latency"""
    print("🌌 ETERNA V18: IGNITING QUANTUM WEBSOCKET LINK...")
    # Tracking BTC, ETH, SOL, BNB aggregated trades
    stream_url = "wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade/ethusdt@aggTrade/solusdt@aggTrade/bnbusdt@aggTrade"
    
    ws = websocket.WebSocketApp(stream_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

# ==========================================
# PHASE 2: ADAPTIVE HEARTBEAT & ENTROPY MONITOR
# ==========================================

def eterna_heartbeat_core():
    bot.send_message(CHAT_ID, "⚡ **ETERNA V18: SHADOW-NODE GENESIS DEPLOYED** ⚡\n\n- Quantum Websocket: ONLINE\n- Ghost Wallet Tracking: ACTIVE (>$150k limit)\n- Adaptive Heartbeat: ARMED\n- Latency: < 50ms\n\n*The system is now an apex predator. Monitoring live bloodline of the market.*")
    
    while True:
        try:
            current_time = time.time()
            time_elapsed = current_time - system_state.last_heartbeat
            
            if time_elapsed >= system_state.heartbeat_interval:
                interval_str = "30 Mins (Action Mode)" if system_state.heartbeat_interval == 1800 else "3 Hours (Stealth Mode)"
                
                status_msg = (
                    f"🔄 **ETERNA V18 STATUS REPORT**\n"
                    f"Status: Invisible & Secure 🛡️\n"
                    f"Chaos Level: {system_state.market_chaos_level}\n"
                    f"Ghost Wallets Tracked (Since last ping): {system_state.whale_alerts_count}\n"
                    f"Heartbeat Rate: Every {interval_str}\n\n"
                    f"*Verdict: Entropy is contained. Core algorithms running perfectly.*"
                )
                bot.send_message(CHAT_ID, status_msg)
                
                # Reset counters for the next cycle
                system_state.last_heartbeat = time.time()
                system_state.whale_alerts_count = 0
                system_state.market_chaos_level = "LOW"
                system_state.heartbeat_interval = 10800 # Reset to 3 hours by default
                
        except Exception as e:
            print(f"Heartbeat Core Shock: {e}")
            
        time.sleep(60) # Check conditions every 1 minute

# ==========================================
# SYSTEM IGNITION SEQUENCE
# ==========================================

if __name__ == "__main__":
    try:
        bot.delete_webhook()
    except:
        pass
    
    # 1. Start Server for Render
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # 2. Start Adaptive Heartbeat
    threading.Thread(target=eterna_heartbeat_core, daemon=True).start()
    
    # 3. Start Zero-Latency Websocket Engine
    threading.Thread(target=start_quantum_websocket, daemon=True).start()
    
    # 4. Start Telegram Command Listener
    bot.infinity_polling(none_stop=True, timeout=60, long_polling_timeout=60)
