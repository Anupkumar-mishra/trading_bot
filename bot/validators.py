VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_side(side: str):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side '{side}'. Allowed values: {VALID_SIDES}"
        )

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type '{order_type}'. Allowed values: {VALID_ORDER_TYPES}"
        )

    return order_type


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price):
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")

    return price

def validate_tick_size(price, tick_size):
    return round(price / tick_size) * tick_size