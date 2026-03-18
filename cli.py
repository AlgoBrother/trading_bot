import argparse
from bot.client import BinanceClient
from bot.order import create_order
from bot.validator import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Place an order on Binance Futures")
    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT orders)")
    
    args = parser.parse_args()  
    
    try: 
        # Validate the order parameters before placing the order
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
        
        # set up the Binance client
        client = BinanceClient()
        
        # Placing the order plus logging the request and response
        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
        
        print("✅ Order placed successfully:", response)
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        
if __name__ == "__main__":
    main()