import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] > shares:
                self.portfolio[symbol] -= shares
            elif self.portfolio[symbol] == shares:
                del self.portfolio[symbol]
            else:
                print("You don't have enough shares to remove")
    
    def view_portfolio(self):
        print("Current portfolio: ")
        for symbol, shares in self.portfolio.items():
            print(f"{symbol}: {shares} shares")  # Correct typo

    def get_stock_price(self, symbol):
        url = f"https://dummy-stock-api.com/{symbol}"  # Correct URL
        response = requests.get(url)  # Correct requests usage
        data = response.json()
        return data["price"]

    def portfolio_value(self):
        total_value = 0
        for symbol, shares in self.portfolio.items():
            stock_price = self.get_stock_price(symbol)  # Fix typo "seelf"
            total_value += stock_price * shares
        return total_value  # Correct indentation

# Correct entry point
if __name__ == "__main__":
    tracker = StockPortfolio()
    tracker.add_stock('AAPL', 10)
    tracker.view_portfolio()
    print(f"Total Portfolio Value: ${tracker.portfolio_value()}")
