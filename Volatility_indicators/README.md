#  Chaikin Volatility Bot (BTCUSD, MetaTrader 5)

This Python script calculates Chaikin Volatility (CV) on BTCUSD using MetaTrader 5 data. It monitors price fluctuations on a 1-minute timeframe and generates real-time buy/sell signals based on changes in volatility.

---

##  Features

- Connects to MetaTrader 5 using the `MetaTrader5` Python API
- Calculates:
  - High–Low price range
  - EMA of price range
  - Chaikin Volatility (% change in EMA over k periods)
- Signal logic:
  - 📈 Buy when CV increases and is positive
  - 📉 Sell when CV decreases and is negative
  - ⏸️ Hold otherwise
- Runs continuously with updates every 2 seconds
- Graceful shutdown on `Ctrl + C`

---

##  Requirements

- MetaTrader 5 terminal (installed and logged in)
- Python 3.8+
- Required packages:
  ```bash
  pip install MetaTrader5 pandas numpy
