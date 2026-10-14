stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "NVDA" : 150,
    "MSFT" : 300
}

total_investment = 0

num_stocks = int(input("how many different stock want to enter: "))

for i in range(num_stocks):
    stock = input("Enter the stock name: ").upper()
    if stock in stock_prices:
        quantity = int(input("Enter the quantity: "))
        prices = stock_prices[stock]
        investment = quantity * prices
        total_investment += investment
    else:
        print("Stock not found!")

print("total investment",total_investment)

save = input("Do you want to save result  (yes/no): ")
if save == "yes":
    with open("portfolio.txt", "a") as file:
        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment: {investment}\n")
        file.write(f"Total investment: {total_investment}\n")
        file.write("--------------------\n")

