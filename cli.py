import typer

from binance.exceptions import BinanceAPIException
from requests.exceptions import ConnectionError

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):

    try:

        side = validate_side(side)

        order_type = validate_order_type(order_type)

        quantity = validate_quantity(quantity)

        price = validate_price(price)

        if order_type == "LIMIT" and price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        client = BinanceFuturesClient().get_client()

        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\nORDER REQUEST")
        print("-" * 40)
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        print("\nORDER RESPONSE")
        print("-" * 40)

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(
            f"Executed Qty: {response.get('executedQty')}"
        )
        print(
            f"Average Price: {response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except ValueError as e:
        print(f"\nValidation Error: {e}")

    except BinanceAPIException as e:
        print(f"\nBinance API Error: {e}")

    except ConnectionError as e:
        print(f"\nNetwork Error: {e}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    app()