import datetime


class Trade:
    def __init__(self, symbol, quantity, buy_or_sell, price):
        self.symbol = symbol
        self.quantity = quantity
        self.buy_or_sell = buy_or_sell
        self.price = price
        self.timestamp = datetime.datetime.now()

    def check_trade_is_valid(self, stock_exchange):
        # check if stock is valid
        is_valid = False
        for stock in stock_exchange:
            if self.symbol == stock.symbol:
                is_valid = True

        if is_valid:
            # Check if quantity is an integer and is greater than 0
            if type(self.quantity) != int or self.quantity < 1:
                return False
            # Check if type of trade is either buy or sell
            if self.buy_or_sell != "Buy" and self.buy_or_sell != "Sell":
                return False
        else:
            return False

        return True
