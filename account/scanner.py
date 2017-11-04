from libs.utils import create_exchange
from account.models import exchange_tokens
class AccountScanner(object):
    def __init__(self):
        self._exchange_tokens = exchange_tokens
    def scan_exchange(self, exchange):
        exchange = create_exchange(exchange)
        balances = exchange.get_balances()
        return balances


    def scan_local_balance(self, exchange):
        return self._exchange_tokens.get_balance_record_by_exchange(exchange)
    def scan_all_account_and_save(self):
        for exchange in ["binance","hitbtc"]:
            balances = self.scan_exchange(exchange)
            local_balances = self.scan_local_balance(exchange)
            for balance in balances:
                self._exchange_tokens.save_token_record(balance)

account_scanner = AccountScanner()