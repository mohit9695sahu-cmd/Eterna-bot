import telebot
import requests
import pandas as pd
import time
import threading
import os
import numpy as np
from flask import Flask

# --- MASTER CONFIGURATION ---
API_TOKEN = '8774381712:AAGepJ_bG_ovvg9JfO6oHWU8lAXS_wugSe0'
CHAT_ID = '5126384362'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "ETERNA QUANTUM BRAIN ACTIVE."

def run_web_server():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- ADVANCED QUANTUM & MATHEMATICAL SCANNER ---
def get_quantum_signals(pair):
    url = f"https://public.coindcx.com/market_data/candles?pair={pair.replace('/', '').lower()}&interval=15m&limit=40"
    try:
        data = requests.get(url, timeout=10).json()
        df = pd.DataFrame(data)
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        
        # 1. MATHEMATICAL PROBABILITY (Standard Deviation & Z-Score)
        # Calculates how far price is stretched from mean - statistical extreme
        df['mean'] = df['close'].rolling(window=20).mean()
        df['std'] = df['close'].rolling(window=20).std()
        df['z_score'] = (df['close'] - df['mean']) / df['std']
        
        # 2. PHYSICS QUANTUM MOMENTUM (Price Velocity)
        # Tracking kinetic energy of price velocity over last 3 periods
        velocity = df['close'].diff(3).iloc[-1]
        
        # 3. CLASSIC MOMENTUM FOR CONVERGENCE
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        df['rsi'] = 100 - (100 / (1 + (gain / loss)))
        
        # Volume Spike Detector
        avg_vol = df['volume'].rolling(window=20).mean().iloc[-1]
        current_vol = df['volume'].iloc[-1]
        
        current_z = df['z_score'].iloc[-1]
        current_rsi = df['rsi'].iloc[-1]
        
        # THE APEX TRADING CRITERIA (Ultra-Advanced Convergence)
        if current_z < -2.0 and current_rsi < 28 and current_vol > (avg_vol * 1.6) and velocity > 0:
            return f"🌌 **ETERNA QUANTUM BUY**\n💎 Asset: {pair}\n📈 Statistical Z-Score: {current_z:.2f} (Extreme Undervalued)\n⚡ Velocity Force: Positive\n📊 RSI: {current_rsi:.1f} | Whales Confirmed."
            
        elif current_z > 2.0 and current_rsi > 72 and current_vol > (avg_vol * 1.6) and velocity < 0:
            return f"⚠️ **ETERNA QUANTUM SELL**\n💎 Asset: {pair}\n📉 Statistical Z-Score: {current_z:.2f} (Extreme Overvalued)\n⚡ Velocity Force: Negative\n📊 RSI: {current_rsi:.1f} | Market Exhausted."
            
    except Exception as e:
        print(f"Quantum Math Error: {e}")
    return None

# --- CORE HEARTBEAT & AUTOMATION ---
def eterna_quantum_core():
    print("🌌 ETERNA V17 QUANTUM ENGINE STARTED...")
    bot.send_message(CHAT_ID, "⚡ **ETERNA V17 SYSTEM RE-ENGINEERED** ⚡\n\n- Quantum Velocity Filter: ONLINE\n- Advanced Z-Score Probability: ACTIVE\n- 3-Hour Heartbeat Monitor: ARMED\n\n*System is scanning space-time market vectors in absolute silence.*")
    
    pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']
    scan_count = 0
    last_heartbeat = time.time()
    
    while True:
        try:
            for pair in pairs:
                signal = get_quantum_signals(pair)
                if signal:
                    bot.send_message(CHAT_ID, signal)
                    time.sleep(300)
            
            scan_count += 1
            
            # 3-Hour Heartbeat Logic (Bina system kamzor kiye assurance)
            if time.time() - last_heartbeat >= 10800: # 10800 seconds = 3 hours
                bot.send_message(CHAT_ID, f"🔄 **ETERNA HEARTBEAT REPORT**\nStatus: Secure & Online 🟢\nScans Performed in last 3h: {scan_count}\nVerdict: Market conditions monitored. Standing by for high-probability mathematical setup.")
                last_heartbeat = time.time()
                scan_count = 0
                
        except Exception as e:
            print(f"Engine Core Shock Recovery: {e}")
            time.sleep(60)
            
        time.sleep(300) # Balanced Vector Scan Every 5 Minutes

if __name__ == "__main__":
    try:
        bot.delete_webhook()
    except:
        pass
    threading.Thread(target=run_web_server, daemon=True).start()
    threading.Thread(target=eterna_quantum_core, daemon=True).start()
    bot.infinity_polling(none_stop=True, timeout=60, long_polling_timeout=60)
