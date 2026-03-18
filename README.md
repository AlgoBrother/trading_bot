# Trading Bot (Binance Futures Testnet)

A Python CLI application to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## ⚙️ Features

Place MARKET and LIMIT orders

Supports BUY and SELL

CLI-based input using argparse

Logging of requests and responses available

Robust error handling for invalid inputs and API failures

Auto price adjustment for LIMIT orders (optional enhancement)

## 🔐 Setup

Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

Install dependencies
```
pip install -r requirements.txt
```

Create a .env file in root:
```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

## ▶️ Usage
MARKET order
```
python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.009
```
LIMIT order
```
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.009
```
### Note: Price is auto-adjusted if not provided

📝 Logs

Logs are saved in:

```
trading_bot.log
```

### Log Includes:

Request details

Response data

Errors

# ⚠️ Notes

Uses Binance Futures Testnet

<b>Some LIMIT orders may remain NEW due to testnet liquidity</b>

MARKET orders are used to ensure execution
