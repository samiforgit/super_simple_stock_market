import functools

from stock import *
from trade import *


class StockExchange:
    def __init__(self, name):
        self.name = name
        self.stocks = []
        self.stock_trades = []

    def add_stock_to_exchange(self, symbol, type, last_dividend, fixed_dividend, par_value, price):
        """ Methods for adding stock to exchange. """
        new_stock = Stock(symbol, type, last_dividend, fixed_dividend, par_value, price)
        is_valid = new_stock.check_stock_is_valid(self.stocks)
        if is_valid:
            self.stocks.append(new_stock)
        return is_valid

    def buy_stock(self, stock_number, quantity):
        """ Method, buy stock. """
        if 0 <= stock_number < len(self.stocks):
            new_trade = Trade(self.stocks[stock_number].symbol, quantity, "Buy", self.stocks[stock_number].price)
            is_valid = new_trade.check_trade_is_valid(self.stocks)
            if is_valid:
            	print(stock_number, datetime.datetime.now(), quantity, 'Buy', self.stocks[stock_number].price)
            	self.stock_trades.append(new_trade)
            return is_valid
        else:
            return False

    def sell_stock(self, stock_number, quantity):
        """ Method, sell stock. """
        if 0 <= stock_number < len(self.stocks):
            new_trade = Trade(self.stocks[stock_number].symbol, quantity, "Sell", self.stocks[stock_number].price)
            is_valid = new_trade.check_trade_is_valid(self.stocks)
            if is_valid:
            	print(stock_number, datetime.datetime.now(), quantity, 'Sell', self.stocks[stock_number].price)
            	self.stock_trades.append(new_trade)
            return is_valid
        else:
            return False

    def calculate_weighted_stock_price(self, stock_symbol, trade_list):
        """ Method, calculate weighted stock price. """
        weighted_stock_price = 0.0
        sigma_trade_price_x_quantity = 0.0
        sigma_trade_quantity = 0.0

        for trade in trade_list:
            if trade.symbol == stock_symbol:
                sigma_trade_price_x_quantity += (trade.price * trade.quantity)
                sigma_trade_quantity += trade.quantity

        if sigma_trade_quantity > 0:
            weighted_stock_price = sigma_trade_price_x_quantity / sigma_trade_quantity

        return weighted_stock_price

    def calculate_dividend_yield(self, stock_number):
        """ Method, calculate dividend yield. """

        dividend_yield = 0.0

        if 0 <= stock_number < len(self.stocks):
            if self.stocks[stock_number].type == "Common":
                dividend_yield = self.stocks[stock_number].last_dividend / float(self.stocks[stock_number].price)
            elif self.stocks[stock_number].type == "Preferred":
                dividend_yield = (self.stocks[stock_number].fixed_dividend * self.stocks[stock_number].par_value) / float(
                    self.stocks[stock_number].price)
        return dividend_yield

    def calculate_pe_ratio(self, stock_number):
        """ Method, calculate PE ratio. """
        pe_ratio = 0.0
        dividend_yield = self.calculate_dividend_yield(stock_number)
        if dividend_yield > 0:
            pe_ratio = float(self.stocks[stock_number].price) / dividend_yield

        return pe_ratio

    def get_trades_within_duration(self, duration):
        """ Method, get trades within duration. """
        trade_list = []
        min_trade_datetime = datetime.datetime.now() - duration
        for trade in self.stock_trades:
            trade_time_delta = trade.timestamp - min_trade_datetime
            if trade_time_delta <= duration:
                trade_list.append(trade)
        return trade_list

    def get_geometric_mean(self, n_list):
        """ Method, geometric mean. """
        geometric_mean = lambda n: functools.reduce(lambda x, y: x * y, n) ** (1.0 / len(n))
        return float(geometric_mean(n_list))

    def calculate_share_index(self):
        """ Method, geometric mean. """
        share_index = 0.0
        weighted_stock_price_list = []
        for stock in self.stocks:
            weighted_stock_price_list.append(self.calculate_weighted_stock_price(stock.symbol, self.stock_trades))

        share_index = self.get_geometric_mean(weighted_stock_price_list)

        return share_index
