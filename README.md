# Trading Bot (Binance Futures Testnet)

## Setup

1. Clone repo
2. Create virtual env
3. Install requirements:
   pip install -r requirements.txt

4. Create a .env file and add api details like this:
        ```BINANCE_API_KEY="xxx"
        BINANCE_API_SECRET="xxx"```

## Run

Market Order:
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Limit Order:
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```
