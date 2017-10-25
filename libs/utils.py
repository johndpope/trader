def create_exchange(exchange):
    if exchange == "liqui":
        from exchanges.liqui import Liqui
        return Liqui()
    if exchange == "hitbtc":
        from exchanges.hitbtc import Hitbtc
        return Hitbtc()