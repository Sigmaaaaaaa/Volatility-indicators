import numpy as np
import pandas as pd
import MetaTrader5 as mt5
import time

if not mt5.initialize():
    print("initialize() failed:" , mt5.last_error())
    quit()

symbol = "BTCUSD"
n = 10
k = 10
timeframe = mt5.TIMEFRAME_M1

print("Running chaikin volatitlity bot... press ctrl+c to stop the bot")

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol , timeframe , 0 , n + k + 1)
        data = pd.DataFrame(rates)

        data["range"] = data["high"] - data["low"]

        data["ema_range"] = data["close"].ewm(span = n , adjust = False).mean()

        data["cv"] = (data["ema_range"] - data["ema_range"].shift(k)) / data["ema_range"].shift(k) * 100

        latest_cv = data["cv"].iloc[-1]
        prev_cv = data["cv"].iloc[-2]

        # buy and sell signal logic 

        if latest_cv > prev_cv and latest_cv > 0:
            signal = "Buy"
        elif latest_cv < prev_cv and latest_cv < 0:
            signal = "Sell"
        else:
            signal = "Hold"

        print(f" cv: {latest_cv:.2f}% | signal: {signal}")

        time.sleep(2)

except KeyboardInterrupt:
    print("bot stop manually")

finally:
    mt5.shutdown()

