from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        if not api_key or not api_secret:
            raise ValueError(
                "API keys not found. Please create a .env file with:\n"
                "BINANCE_API_KEY=your_key\n"
                "BINANCE_API_SECRET=your_secret\n"
            )
        
        self.client = Client(api_key, api_secret, testnet=True) # Initialize the Binance client with testnet=True for testing purposes
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **params):
        return self.client.futures_create_order(**params)