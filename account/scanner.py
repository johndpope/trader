from libs.utils import create_exchange
from account.models import exchange_tokens
from transaction.balance import transaction_balance
class AccountScanner(object):
    def __init__(self):
        self._exchange_tokens = exchange_tokens
    def scan_exchange(self, exchange):
        exchange = create_exchange(exchange)
        balances = exchange.get_balances()
        prices = exchange.get_all_price()
        prices["eth"] = {}
        prices["eth"]["price"] = "1"
        ret = []
        for balance in balances:
            # print balance
            try:
                balance["price"] = prices[balance["token"]]["price"]
                ret.append(balance)
            except Exception as e:
                print str(e)
                pass
        return ret

    def scan_simple_tokens(self, exchange):
        exchange = create_exchange(exchange)
        symbols = exchange.get_symbols()
        return symbols


    def scan_local_balance(self, exchange):
        return self._exchange_tokens.get_balance_record_by_exchange(exchange)
    def get_balances(self):
        return self._exchange_tokens.get_balances()
    def scan_all_account_and_save(self):
        for exchange in ["binance","hitbtc","liqui"]:
            balances = self.scan_exchange(exchange)
            # local_balances = self.scan_local_balance(exchange)
            for balance in balances:
                self._exchange_tokens.save_token_record(balance)
    def scan_all_exchanges(self):
        ret = {}
        for exchange in ["binance","hitbtc","liqui","bithumb","bitfinex", "poloniex",
        "bitstamp","huobi","wex","yobit"]:
            try:
                exchange_tokens = self.scan_simple_tokens(exchange)
                local_tokens = self._exchange_tokens.get_simple_tokens(exchange)
                #local_tokens = []
                ret[exchange] = []
                token_records = []
                for token in exchange_tokens:
                    if token not in local_tokens:
                        r = {}
                        r["token"] = token
                        r["exchanges"] = self._exchange_tokens.get_simple_token_exchanges(token)
                        ret[exchange].append(r)
                        item = {}
                        item["token"] = token
                        item["exchange"] = exchange
                        item["identify"] = exchange + "_" + token
                        try:
                            self._exchange_tokens.save_sample_token(item)
                        except:
                            pass
            except:
                pass
        print ret
        return ret

    def get_transfer_token_pairs(self):
        tokens = self._exchange_tokens.get_tokens()
        pairs = []
        for token in tokens:
            token_records = self._exchange_tokens.get_balance_records_by_token(token)
            if len(token_records) != 2:
                continue
            token_record_1 = token_records[0]
            token_record_2 = token_records[1]
            rt,amount = transaction_balance.balance_between_account_with_hardcode_policy(token_record_1, token_record_2)
            if rt:
                if amount > 0:
                    print "Token:{token} from {from_exchange} to {to_exchange} amount {amount}".format(token = token,from_exchange=token_record_1["exchange"],
                        to_exchange=token_record_2["exchange"], amount=amount)
                else:
                    print "Token:{token} from {from_exchange} to {to_exchange} amount {amount}".format(token = token,from_exchange=token_record_2["exchange"],
                        to_exchange=token_record_1["exchange"], amount=abs(amount))
                pairs.append(token_records)
        return pairs

account_scanner = AccountScanner()
