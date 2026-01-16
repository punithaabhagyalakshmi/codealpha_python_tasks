"""stock_portfolio_tracker
using dictionary, ip/op, basic arithmetic,file handling
"""
import datetime
stock_prices={"AAPL":180,
              "TSLA":250,
              "GOOG":140,
              "MSFT":320,
              "AMZN":130,
              "NTFX":410}
print(f"Available Stocks: {",".join(stock_prices.keys())}")
tot=0
while True:
    stock=input("Enter the stock name(type 'end' to quit): ").upper()
    if stock=="END":
        print("Goodbye!")
        break
    elif stock in stock_prices:
        qty=int(input("Enter quantity: "))
        price=stock_prices[stock]
        tot+=qty*price
        print(f"Total investment: ${tot}")
    else:
        print("Stock not found")
    with open("stock_tracker.txt","a") as file:
        file.write(f"Total investment: ${tot} done in {stock} as of {datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')}")
        file.write("\n")
    print("Saved in stock_tracker.txt file")

        
    

