def validate_order(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Must be 'BUY' or 'SELL'.")
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type. Must be 'MARKET' or 'LIMIT'.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if order_type == "LIMIT" and price is not None and price <= 0:
        raise ValueError("Price must be greater than 0 for LIMIT orders.")