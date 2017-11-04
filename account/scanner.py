from libs.utils import create_exchange
class AccountScanner(object):
    def scan_exchange(self, exchange):
        exchange = create_exchange(exchange)
        balance = exchange.get_balances()

    def scan_all_account_and_save(self):
        for exchange in ["binance","hitbtc"]:
            self.scan_exchange(exchange)

account_scanner = AccountScanner()