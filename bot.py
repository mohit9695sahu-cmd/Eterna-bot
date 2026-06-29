import telebot
import requests
import pandas as pd
import time
import threading
import os
from flask import Flask

# --- MASTER CONFIGURATION ---
API_TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'
CHAT_ID = '5126384362' # Aapki sahi numeric ID yahan update kar di hai
bot = telebot.TeleBot(API_TOKEN)

# --- 1. IMMORTAL WEB SERVER (RENDER SHIELD) ---
app = Flask(__name__)
@app.route('/')
def home():
    return "ETERNA SUPREME CORE IS ACTIVE."

def run_web_server():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- 2. THE GOD-LEVEL BRAIN (Volume + Momentum + Sentiment) ---
def get_market_sentiment():
    try:
        response = requests.get("https://api.alternative.me/fng/", timeout=10).json()
        return int(response['data'][0]['value'])
    except:
        return 50

def get_supreme_signal(pair):
    url = f"https://public.coindcx.com/market_data/candles?pair={pair.replace('/', '').lower()}&interval=15m&limit=30"
    try:
        data = requests.get(url, timeout=10).json()
        df = pd.DataFrame(data)
        
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        
        # Advanced Indicators
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()
        
        # Volume Anomaly Detection
        avg_volume = df['volume'].rolling(window=20).mean().iloc[-1]
        current_volume = df['volume'].iloc[-1]
        volume_spike = current_volume > (avg_volume * 1.5)
        
        current_price = df['close'].iloc[-1]
        current_rsi = df['rsi'].iloc[-1]
        ema_20 = df['ema_20'].iloc[-1]
        sentiment = get_market_sentiment()
        
        # SILENT SNIPER LOGIC (Ultra-Strict)
        if current_rsi < 30 and current_price > ema_20 and volume_spike and sentiment > 20:
            return f"🟢 GOD-BUY CONFIRMED\n💰 {pair} @ ${current_price}\n📊 RSI: {current_rsi:.1f} | 📈 Volume Spike Detected!\n🧠 Sentiment: {sentiment} (Whales Accumulating)"
            
        elif current_rsi > 70 and current_price < ema_20 and volume_spike and sentiment < 80:
            return f"🔴 GOD-SELL CONFIRMED\n💰 {pair} @ ${current_price}\n📊 RSI: {current_rsi:.1f} | 📉 Volume Spike Detected!\n🧠 Sentiment: {sentiment} (Whales Dumping)"
            
    except Exception as e:
        print(f"Neural Error on {pair}: {e}")
        pass
    return None

# --- 3. THE SILENT WATCHER (Auto-Pilot) ---
def eterna_core():
    print("🌌 ETERNA V16 SUPREME CORE ONLINE...")
    try:
        bot.send_message(CHAT_ID, "⚡ ETERNA V16 LAUNCHED.\n\nSilent Sniper Mode: ACTIVE.\nVolume Filter: ACTIVE.\n\n(Aapko ab sirf God-Level verified signals hi milenge. Faltu messages band kar diye gaye hain.)")
    except Exception as e:
        print(f"Failed to send welcome message: {e}")
    
    pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']
    
    while True:
        try:
            for pair in pairs:
                signal = get_supreme_signal(pair)
                if signal:
                    bot.send_message(CHAT_ID, f"🔔 **ETERNA SUPREME ALERT** 🔔\n\n{signal}")
                    time.sleep(300)
        except Exception as e:
            print(f"⚠️ ETERNA Core Recovering from shock: {e}")
            time.sleep(60)
            
        time.sleep(300)

# --- IGNITION SEQUENCE ---
if __name__ == "__main__":
    try:
        bot.delete_webhook()
    except:
        pass
        
    threading.Thread(target=run_web_server, daemon=True).start()
    threading.Thread(target=eterna_core, daemon=True).start()
    
    print("🌌 SYSTEM DEPLOYED. WAITING IN SHADOWS.")
    bot.infinity_polling(none_stop=True, timeout=60, long_polling_timeout=60)
