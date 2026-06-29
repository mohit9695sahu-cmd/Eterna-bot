# ====================================================================
# 🌌 ETERNA APEX v13.2: THE OMNIPOTENT WORLD #1 CORE
# ====================================================================

import telebot
import requests
import pandas as pd
import time
import threading

# CONFIGURATION
API_TOKEN = '8774381712:AAEHsnyXkoCB0ASKh_6EGUQHHTkf35fsR0o'
CHAT_ID = '8774381712:AAEHsnyXkoCB0ASKh_6EGUQHHTkf35fsR0o' # <-- Yahan apni sahi ID daalein
bot = telebot.TeleBot(API_TOKEN)

# 1. SENTIMENT ENGINE (Fear & Greed)
def get_market_sentiment():
    try:
        response = requests.get("https://api.alternative.me/fng/").json()
        return int(response['data'][0]['value'])
    except:
        return 50

# 2. OMNIPOTENT ANALYSIS ENGINE
def get_advanced_signal(pair):
    url = f"https://public.coindcx.com/market_data/candles?pair={pair.replace('/', '').lower()}&interval=5m&limit=20"
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    prices = df['close'].astype(float)
    
    # Technical Indicators
    rsi = 100 - (100 / (1 + (prices.diff().clip(lower=0).rolling(14).mean() / -prices.diff().clip(upper=0).rolling(14).mean())))
    ema = prices.ewm(span=20, adjust=False).mean()
    sentiment = get_market_sentiment()
    
    # GOD-LOGIC: Signal + Sentiment Confluence
    # Buy only if RSI < 35, Price > EMA (Trend), and Sentiment is safe
    if rsi.iloc[-1] < 35 and prices.iloc[-1] > ema.iloc[-1] and sentiment > 25:
        return f"⚡ GOD-BUY | RSI: {rsi.iloc[-1]:.1f} | Sentiment: {sentiment}", "BUY"
    elif rsi.iloc[-1] > 65 and prices.iloc[-1] < ema.iloc[-1] and sentiment < 75:
        return f"⚠️ GOD-SELL | RSI: {rsi.iloc[-1]:.1f} | Sentiment: {sentiment}", "SELL"
    return None, None

# 3. IMMORTAL AUTO-PILOT LOOP
def auto_pilot():
    print("🚀 ETERNA V13.2 CORE ONLINE...")
    while True:
        try:
            for pair in ['BTC/USDT', 'ETH/USDT']:
                signal, action = get_advanced_signal(pair)
                if signal:
                    bot.send_message(CHAT_ID, f"🔔 **ETERNA SUPREME ALERT**\n🔹 {pair}: {signal}")
        except Exception as e:
            print(f"⚠️ ETERNA Recovering: {e}")
        time.sleep(60) # 1 minute heartbeat

# STARTING THE SYSTEMS
if __name__ == "__main__":
    threading.Thread(target=auto_pilot, daemon=True).start()
    print("🌌 SYSTEM FULLY DEPLOYED.")
    bot.infinity_polling(none_stop=True)
