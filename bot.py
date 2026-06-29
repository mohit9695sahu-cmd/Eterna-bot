# ====================================================================
# 🌌 ETERNA APEX v13.4: THE FORCE-FIX CLOUD CORE
# ====================================================================

import telebot
import requests
import pandas as pd
import time
import threading

# CONFIGURATION
API_TOKEN = '8774381712:AAEHsnyXkoCB0ASKh_6EGUQHHTkf35fsR0o'
CHAT_ID = '1987515437' 
bot = telebot.TeleBot(API_TOKEN)

# 1. SENTIMENT ENGINE
def get_market_sentiment():
    try:
        response = requests.get("https://api.alternative.me/fng/").json()
        return int(response['data'][0]['value'])
    except:
        return 50

# 2. ANALYSIS ENGINE
def get_advanced_signal(pair):
    url = f"https://public.coindcx.com/market_data/candles?pair={pair.replace('/', '').lower()}&interval=5m&limit=20"
    try:
        data = requests.get(url, timeout=10).json()
        df = pd.DataFrame(data)
        prices = df['close'].astype(float)
        
        rsi = 100 - (100 / (1 + (prices.diff().clip(lower=0).rolling(14).mean() / -prices.diff().clip(upper=0).rolling(14).mean())))
        ema = prices.ewm(span=20, adjust=False).mean()
        sentiment = get_market_sentiment()
        
        if rsi.iloc[-1] < 35 and prices.iloc[-1] > ema.iloc[-1] and sentiment > 25:
            return f"⚡ GOD-BUY | RSI: {rsi.iloc[-1]:.1f} | Sentiment: {sentiment}", "BUY"
        elif rsi.iloc[-1] > 65 and prices.iloc[-1] < ema.iloc[-1] and sentiment < 75:
            return f"⚠️ GOD-SELL | RSI: {rsi.iloc[-1]:.1f} | Sentiment: {sentiment}", "SELL"
    except:
        pass
    return None, None

# 3. AUTO-PILOT
def auto_pilot():
    while True:
        try:
            for pair in ['BTC/USDT', 'ETH/USDT']:
                signal, action = get_advanced_signal(pair)
                if signal:
                    bot.send_message(CHAT_ID, f"🔔 **ETERNA SUPREME ALERT**\n🔹 {pair}: {signal}")
        except Exception as e:
            print(f"⚠️ ETERNA Recovering: {e}")
        time.sleep(60)

# STARTING THE SYSTEMS
if __name__ == "__main__":
    try:
        bot.delete_webhook() # Purane connection todne ka final tareeka
        print("🌌 Webhook deleted successfully.")
    except:
        pass
        
    threading.Thread(target=auto_pilot, daemon=True).start()
    print("🌌 SYSTEM FULLY DEPLOYED.")
    bot.infinity_polling(none_stop=True, interval=0, timeout=20)
