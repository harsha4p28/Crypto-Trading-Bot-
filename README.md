# Crypto Trading Bot - Binance Futures Testnet (Python)

##  Overview
This is a **command-line Python trading bot** built using the official `python-binance` library. It connects to the **Binance Futures Testnet**, allowing users to place **market and limit orders**, check balances, and log all trades and errors.


---

## Features

- Place **market buy/sell orders**
- Place **limit buy/sell orders**
- View **futures USDT-M account balances**
- **Log all trades and errors** to a local file (`all_logs.txt`)
- Validates user input for safety
- Rich command-line interface using `rich` library

---

##  Tech Stack

- **Python 3**
- **python-binance** (official Binance API wrapper)
- **rich** (for styled terminal output)

---

##  How to Run

### 1. Install dependencies
` pip install python-binance rich `
### 2. Add binance testnet API cedentials
` API_KEY = 'YOUR_API_KEY'
  API_SECRET = 'YOUR_API_SECRET' `
### 3. Start the bot
` python bot.py`

## File structure 
- chatbot.py
- readme.md
