#Required modules
from binance.client import Client
from binance.enums import *
from rich import print

#API keys
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

client = Client(API_KEY, API_SECRET, testnet=True)

#Market order function
def market_operation(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"[bold green]{side} order placed successfully[/bold green]")
        print(f"[cyan]Order ID:[/cyan] {order['orderId']}")
        print(f"[cyan]Symbol:[/cyan] {order['symbol']}")
        print(f"[cyan]Side:[/cyan] {order['side']}")
        order_log(order)
    except Exception as e:
        error_log(e)
        print(f"[bold red]Error placing {side} order:[/bold red] {e}")

#Balance function
def show_balance():
    try:
        account_info = client.futures_account()
        balances = account_info['assets']

        print("[bold magenta]==== Account Balances ====[/bold magenta]")
        for asset in balances:
            print(f"[yellow]Asset:[/yellow] {asset['asset']} [green]Wallet Balance:[/green] {asset['walletBalance']}")
    except Exception as e:
        print("[bold red]Error fetching account balance:[/bold red]", e)

#Limit order function
def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price
        )
        print(f"[bold green]{side} LIMIT order placed successfully:[/bold green] ")
        print(f"[cyan]Order ID:[/cyan] {order['orderId']}")
        print(f"[cyan]Symbol:[/cyan] {order['symbol']}")
        print(f"[cyan]Side:[/cyan] {order['side']}")
        order_log(order)
    except Exception as e:
        print(f"[bold red]Error placing {side} LIMIT order:[/bold red] {e}")
        error_log(str(e))

#Order logging
def order_log(order):
    with open('all_logs.txt', 'a') as file:
        file.write(f"ORDER: {order}\n")

#error logging
def error_log(error):
    with open('all_logs.txt', 'a') as file:
        file.write(f"ERROR: {error}\n")

#Main
while True:
    print("\n[bold yellow]Welcome, I am your Trading Bot[/bold yellow]")
    print("[bold blue]MENU[/bold blue]")
    print("[cyan]1.[/cyan] Place a Market Order")
    print("[cyan]2.[/cyan] Show Balance")
    print("[cyan]3.[/cyan] Limit Order")
    print("[cyan]4.[/cyan] Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        symbol = input("Enter trading pair (Ex: BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        if side not in ['BUY', 'SELL']:
            print("[bold red]Invalid input! Enter BUY or SELL.[/bold red]")
            continue
        quantity = float(input("Enter quantity: "))
        market_operation(symbol, side, quantity)

    elif choice == '2':
        show_balance()

    elif choice == '3':
        symbol = input("Enter trading pair (Example :  BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        if side not in ['BUY', 'SELL']:
            print("[bold red]Invalid side. Use BUY or SELL.[/bold red]")
            continue
        try:
            quantity = float(input("Enter quantity: "))
            price = float(input("Enter limit price: "))
            place_limit_order(symbol, side, quantity, price)
        except ValueError:
            print("[bold red]Invalid input. Please enter numeric values.[/bold red]")

    elif choice == '4':
        print("[bold blue]Exiting... Goodbye![/bold blue]")
        break

    else:
        print("[bold red]Invalid choice. Please select 1, 2, 3 or 4.[/bold red]")
