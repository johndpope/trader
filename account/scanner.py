from libs.utils import create_exchange
from account.models import exchange_tokens
class AccountScanner(object):
    def __init__(self):
        self._exchange_tokens = exchange_tokens
    def scan_exchange(self, exchange):
        exchange = create_exchange(exchange)
        balance = exchange.get_balances()


    def scan_local_balance(self, exchange):
        return self._exchange_tokens.get_balance_record_by_exchange(exchange)
    def scan_all_account_and_save(self):
        for exchange in ["binance","hitbtc"]:
            balance = self.scan_exchange(exchange)
            local_balance = self.scan_local_balance(exchange)

account_scanner = AccountScanner()