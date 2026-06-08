import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )

        # Binance Futures Testnet endpoint
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client

    def get_symbol_info(self, symbol):
        return self.client.futures_exchange_info()