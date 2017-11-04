from libs.db import aquire_cursor
class TokenRecoder(object):
    """
        item:
        token:
        exchange:
        withdraw:
        deposit:
        amount:
    """
    def get_token_info(self,token, exchange=None):
        self.lock = False #lock 的token 表示这几天不适合转账
        self.token = token
        self.exchange = exchange
        self.withdraw = withdraw
        self.deposit = deposit
        self.amount = amount
        self.price = price
        self.withdraw_fee = {
            "min":"",
            "value":"",
            "max":""
        }
        self.deposit_fee = {
            "min":"",
            "value":"",
            "max":""
        }

    def save_token_info(self, token, exchange, withdraw, deposit, amount):
        pass

class ExchangeTokens(object):
    def __init__(self):
        pass

    def get_balance_record_by_exchange(self, exchange):
        with aquire_cursor() as cursor:
            stmt = "select * from "

    def get_balance_records_by_exchange_and_token(self, exchange, token):
        pass

    def get_balance_records_by_token(self, token):
        pass

class TranscationRecords(object):
    def __init__(self):
        pass

    def get_transcation_by_exchange_and_token(self):
        pass
exchange_tokens = ExchangeTokens()