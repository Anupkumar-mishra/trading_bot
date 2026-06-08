# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M). The application allows users to place MARKET and LIMIT orders through a command-line interface (CLI) with input validation, logging, and error handling.

The project was developed as part of a Python Developer assessment task.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL sides
* Binance Futures Testnet (USDT-M) integration
* CLI-based order placement using Typer
* Input validation
* Structured project architecture
* Logging of requests, responses, and errors
* Exception handling for validation, API, and network errors
* Optional lightweight GUI using Tkinter

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── gui.py
├── .env
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Anupkumar-mishra/trading_bot.git

cd trading_bot
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

Generate API credentials from Binance Futures Testnet.

---

## Running the Application

### MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

### LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
```

### LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 65000
```

### CLI Help

```bash
python cli.py --help
```

---

## GUI (Optional)

Run the lightweight Tkinter desktop interface:

```bash
python gui.py
```

The GUI allows users to:

* Select symbol
* Select BUY/SELL
* Select MARKET/LIMIT
* Enter quantity
* Enter price for LIMIT orders
* Place orders directly from a desktop window

---

## Logging

All API requests, responses, and errors are logged to:

```text
logs/trading.log
```

Example log entries:

```text
REQUEST -> Symbol=BTCUSDT, Side=BUY, Type=MARKET, Qty=0.001

RESPONSE -> OrderId=14493184015

ERROR -> Binance API Error: Price not increased by tick size
```

---

## Assumptions

* The application uses Binance Futures Testnet (USDT-M) only.
* Users provide valid Binance Testnet API credentials.
* Sufficient virtual balance is available in the testnet account.
* Quantity and price values follow Binance Futures trading rules.
* Internet connectivity is available while placing orders.

---

## Technologies Used

* Python 3.x
* python-binance
* Typer
* python-dotenv
* Tkinter
* Logging

---

## Author

AnupKumar Mishra
