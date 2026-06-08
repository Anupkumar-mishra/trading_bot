import tkinter as tk
from tkinter import ttk, messagebox

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager

def place_order():
    try:
        symbol = symbol_var.get().upper()
        side = side_var.get()
        order_type = type_var.get()
        quantity = float(quantity_var.get())

        price = None
        if order_type == "LIMIT":
            price = float(price_var.get())

        client = BinanceFuturesClient().get_client()
        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        messagebox.showinfo(
            "Success",
            f"Order Placed!\n\n"
            f"Order ID: {response.get('orderId')}\n"
            f"Status: {response.get('status')}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Binance Futures Bot")
root.geometry("400x300")

symbol_var = tk.StringVar(value="BTCUSDT")
side_var = tk.StringVar(value="BUY")
type_var = tk.StringVar(value="MARKET")
quantity_var = tk.StringVar(value="0.001")
price_var = tk.StringVar()

ttk.Label(root, text="Symbol").pack()
ttk.Entry(root, textvariable=symbol_var).pack()

ttk.Label(root, text="Side").pack()
ttk.Combobox(
    root,
    textvariable=side_var,
    values=["BUY", "SELL"]
).pack()

ttk.Label(root, text="Order Type").pack()
ttk.Combobox(
    root,
    textvariable=type_var,
    values=["MARKET", "LIMIT"]
).pack()

ttk.Label(root, text="Quantity").pack()
ttk.Entry(root, textvariable=quantity_var).pack()

ttk.Label(root, text="Price (LIMIT only)").pack()
ttk.Entry(root, textvariable=price_var).pack()

ttk.Button(
    root,
    text="Place Order",
    command=place_order
).pack(pady=10)

root.mainloop()