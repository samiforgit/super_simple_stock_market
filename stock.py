""" Class, Stock. """


class Stock:
    def __init__(self, symbol, type, last_dividend, fixed_dividend, par_value, price):
        self.symbol = symbol
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.price = price

    def check_stock_is_valid(self, stock_exchange):
        """Validate the stock."""
        # Check if stock symbol is valid by checking if symbol is left blank or not
        # a string(full naming restrictions need specified for further update)
        if self.symbol == "" or type(self.symbol) != str:
            return False

        # Check if stock already exists to prevent duplication
        for stock in stock_exchange:
            if self.symbol == stock.symbol:
                return False

        # check if stock type is valid
        if self.type != "Common" and self.type != "Preferred":
            return False

        # Check if Last Dividend is a float or integer
        if type(self.last_dividend) != int and type(self.last_dividend) != float:
            return False

        # Check if Fixed Dividend is a float or integer
        if type(self.fixed_dividend) != int and type(self.fixed_dividend) != float:
            return False

        # Check if Pat Value is a float or integer
        if type(self.par_value) != int and type(self.par_value) != float:
            return False

        # Check if Pat Value is a float or integer
        if type(self.price) != int and type(self.price) != float or self.price <= 0:
            return False

        return True
