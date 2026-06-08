from binance.exceptions import BinanceAPIException
from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            logger.info(
                f"REQUEST -> Symbol={symbol}, "
                f"Side={side}, "
                f"Type={order_type}, "
                f"Qty={quantity}, "
                f"Price={price}"
            )

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Unsupported order type")

            logger.info(f"RESPONSE -> {response}")

            return response

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")

            raise

        except Exception as e:

            logger.error(f"Unexpected Error: {e}")

            raise