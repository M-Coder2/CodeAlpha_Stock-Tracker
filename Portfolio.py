stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 140
}

portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Enter stock symbols and quantity. Type 'done' to finish.\n")

while True:
    symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
    if symbol == "DONE":
        break

    if symbol not in stock_prices:
        print("Unknown stock symbol. Available symbols:", ', '.join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {symbol}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid number. Try again.")
        continue

    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

print("\n🧾 Investment Summary:")
total_value = 0

for symbol, qty in portfolio.items():
    price = stock_prices[symbol]
    value = price * qty
    total_value += value
    print(f"{symbol}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

save = input("Do you want to save this summary to a file? (yes/no): ").lower()

if save == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = price * qty
            file.write(f"{symbol}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")

    print(f"Summary saved to '{filename}'")