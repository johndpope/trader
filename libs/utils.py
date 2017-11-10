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
