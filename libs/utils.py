import datetime
import time
def create_exchange(exchange):
    if exchange == "liqui":
        from exchanges.liqui import Liqui
        return Liqui()
    if exchange == "hitbtc":
        from exchanges.hitbtc import Hitbtc
        return Hitbtc()
    if exchange == "bittrex":
        from exchanges.bittrex import Bittrex
        return Bittrex()
    if exchange == "binance":
        from exchanges.binance import Binance
        return Binance()
    if exchange == "bithumb":
        from exchanges.bithumb import Bithumb
        return Bithumb()
    if exchange == "bitfinex":
        from exchanges.bitfinex import Bitfinex
        return Bitfinex()
    if exchange == "poloniex":
        from exchanges.poloniex import Poloniex
        return Poloniex()
    if exchange == "bitstamp":
        from exchanges.bitstamp import Bitstamp
        return Bitstamp()
    if exchange == "huobi":
        from exchanges.huobi import Huobi
        return Huobi()
    if exchange == "wex":
        from exchanges.wex import Wex
        return Wex()
    if exchange == "yobit":
        from exchanges.yobit import Yobit
        return Yobit()
def timestamp_to_string(timestamp):
    tmp = datetime.datetime.fromtimestamp(int(timestamp))
    str1 = tmp.strftime("%Y-%m-%d %H:%M:%S.%f")
    return str1
def timestamp_to_mysql_string(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def mysql_string_to_timestamp(mysql_string):
    mysql_string = datetime.datetime.strptime(mysql_string, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(mysql_string.timetuple()))
