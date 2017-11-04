from libs.utils import create_exchange
from account.models import exchange_tokens
from transaction.balance import transaction_balance
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
            # local_balances = self.scan_local_balance(exchange)
            for balance in balances:
                self._exchange_tokens.save_token_record(balance)

    def get_transfer_token_pairs(self):
        tokens = self._exchange_tokens.get_tokens()
        pairs = []
        for token in tokens:
            token_records = self._exchange_tokens.get_balance_records_by_token(token)
            if token_records != 2:
                continue
            token_record_1 = token_records[0]
            token_record_2 = token_records[1]
            rt,amount = transaction_balance.balance_between_account_with_hardcode_policy(token_record_1, token_record_2)
            if rt:
                print amount
                pairs.append(token_records)
        return pairs

account_scanner = AccountScanner()