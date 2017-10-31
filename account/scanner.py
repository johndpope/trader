class AccountScanner(object):
    def scan_exchange(self, exchange):
        exchange = create_exchange(exchange)
        balance = exchange.get_balances()