""" Super Simple Stock Market """

from stockExchange import *

# Creates instance of a simple stock exchange
stock_exchange = StockExchange("Global Beverage Corporation Exchange")


def main():
    """
    Main method to adds stocks to the stock exchanged , creates stock trades and get the
    expected values i.e PE ratio etc.
    """
    # add stocks to the stock exchanged
    create_stock_exchange()
    # create stocks trades
    create_trades()
    get_dividend_yield_of_all_stock()
    get_pe_ratio_of_all_stock()
    get_weighted_stock_price_last_15mins()
    get_gbce_index()


def create_stock_exchange():
    stock_exchange.add_stock_to_exchange("TEA", "Common", 0.0, 0, 100, 100)
    stock_exchange.add_stock_to_exchange("POP", "Common", 8, 0, 100, 120)
    stock_exchange.add_stock_to_exchange("ALE", "Common", 23, 0, 60, 80)
    stock_exchange.add_stock_to_exchange("GIN", "Preferred", 8, 2, 100, 90)
    stock_exchange.add_stock_to_exchange("JOE", "Common", 13, 0, 250, 150)


def create_trades():
    print("****************************************************")
    print("                 Trade Records                      ")
    print("S.No    Timestamp    Quantity  Buy/Sell  Price      ")
    print("****************************************************")
    stock_exchange.buy_stock(0, 400)
    stock_exchange.buy_stock(1, 300)
    stock_exchange.buy_stock(2, 400)
    stock_exchange.buy_stock(3, 700)
    stock_exchange.buy_stock(4, 500)
    stock_exchange.buy_stock(0, 600)
    stock_exchange.buy_stock(1, 100)
    stock_exchange.buy_stock(2, 400)
    stock_exchange.buy_stock(3, 900)
    stock_exchange.buy_stock(0, 300)
    stock_exchange.buy_stock(1, 100)
    stock_exchange.buy_stock(2, 200)
    stock_exchange.buy_stock(0, 50)
    stock_exchange.buy_stock(0, 370)


def get_dividend_yield_of_all_stock():
    """ Methods to get the dividend yield of all the stocks. """
    print("****************************************************")
    print("               Dividend Yield                       ")
    print("****************************************************")
    for i in range(len(stock_exchange.stocks)):
        print("The Dividend Yield for {} is {}".format(
            stock_exchange.stocks[i].symbol, str(stock_exchange.calculate_dividend_yield(i))))


def get_pe_ratio_of_all_stock():
    """ Methods to get the d P/E Ratio for of all the stocks. """
    print("****************************************************")
    print("                  P/E Ratio                         ")
    print("****************************************************")
    for i in range(len(stock_exchange.stocks)):
        print("The P/E Ratio for " + stock_exchange.stocks[i].symbol + " is " + str(stock_exchange.calculate_pe_ratio(i)))


def get_gbce_index():
    """ Methods to get the GBCE for of all the stocks. """
    print("****************************************************")
    print("              GBCE All Share Index                  ")
    print("****************************************************")
    print("The GBCE all share index is: " + str(stock_exchange.calculate_share_index()))


def get_weighted_stock_price_last_15mins():
    """ Methods to get weighted stock price based on trades in past 15 minutes. """
    print("****************************************************")
    print("        Volume Weighted Stock Price                 ")
    print("****************************************************")

    trade_list = stock_exchange.get_trades_within_duration(datetime.timedelta(minutes=15))

    for i in range(len(stock_exchange.stocks)):
        print("Volume Weighted Stock Price based on trades in past 15 minutes for " +
              stock_exchange.stocks[i].symbol + " is " +
              str(stock_exchange.calculate_weighted_stock_price(stock_exchange.stocks[i].symbol, trade_list)))


if __name__ == "__main__":
    main()
