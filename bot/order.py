import logging

def create_order(client, symbol, side, order_type, quantity, price=None):
    try:
        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        
        if order_type == "LIMIT":
            if price is None:
                # auto price logic
                current_price = float(client.client.futures_mark_price(symbol=symbol)["markPrice"])

                if side == "BUY":
                    price = current_price * 1.01  # 1% above current price for BUY orders
                else:  # SELL
                    price = current_price * 0.99  # 1% below current price for SELL orders

                print(f"Auto price used: {price}")

            # now assign (either user price OR auto price)
            order_params["price"] = round(price, 2)
            order_params["timeInForce"] = "GTC" # Good Till Cancelled for LIMIT orders
        
        logging.info(f"Request: {order_params}")
        
        response = client.place_order(**order_params) # calls the place_order method from client.py and passes the order parameters as keyword arguments
        logging.info(f"Response: {response}")
        
        return response
        
    except Exception as e:
        logging.error(f"Error creating order: {e}")
        raise # re-raise the exception after logging it