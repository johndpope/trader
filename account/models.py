# -*- coding=utf-8 -*-
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
            stmt = "select * from token_record where exchange='{exchange}'".format(exchange=exchange)
            cursor.execute(stmt)
            data = cursor.fetchall()
        if not data:
            return []
        return data

    def get_simple_tokens(self, exchange):
        with aquire_cursor() as cursor:
            stmt = "select token from simple_token where exchange='{exchange}'".format(exchange=exchange)
            cursor.execute(stmt)
            data = cursor.fetchall()
        if not data:
            return []
        return [ item["token"] for item in data ]

    def save_sample_token(self, token_record):
        identify = token_record["identify"]
        token = token_record["token"]
        exchange = token_record["exchange"]
        with aquire_cursor() as cursor:
            stmt  = "INSERT INTO simple_token (identify,token, exchange) VALUES ('{identify}','{token}', '{exchange}')".format(identify=identify,token=token,exchange=exchange)
            cursor.execute(stmt)

    def get_balances(self):
        with aquire_cursor() as cursor:
            stmt = "select * from token_record"
            cursor.execute(stmt)
            data = cursor.fetchall()
        if not data:
            return []
        return data

    def save_token_record(self, token_record):
        token = token_record["token"]
        exchange = token_record["exchange"]
        amount = token_record["amount"]
        price = token_record["price"]
        identify = token + "_" + exchange
        with aquire_cursor() as cursor:
            stmt  = "INSERT INTO token_record (identify,token, exchange, amount, price) VALUES ('{identify}','{token}', '{exchange}', '{amount}','{price}') ON DUPLICATE KEY UPDATE amount={amount},price={price} ".format(identify=identify,token=token, exchange=exchange,amount = amount, price=price)
            print stmt
            cursor.execute(stmt)

    def get_balance_records_by_exchange_and_token(self, exchange, token):
        pass

    def get_balance_records_by_token(self, token):
        with aquire_cursor() as cursor:
            stmt = "SELECT * from token_record WHERE token='{token}'".format(token=token)
            cursor.execute(stmt)
            return cursor.fetchall()

    def get_tokens(self):
        with aquire_cursor() as cursor:
            stmt = "SELECT DISTINCT token from token_record"
            cursor.execute(stmt)
            data = cursor.fetchall()
        if not data:
            return []
        return [ item["token"] for item in data ]

    def get_token_exchanges(self, token):
        with aquire_cursor() as cursor:
            stmt = "SELECT DISTINCT exchange from token_record where token='{token}'".format(token=token)
            cursor.execute(stmt)
            data = cursor.fetchall()
        if not data:
            return []
        return [ item["exchange"] for item in data ]

    def get_exchange_token_amount(self, token, exchange):
        with aquire_cursor() as cursor:
            stmt = "SELECT amount from token_record where token='{token}' and exchange='{exchange}'".format(token=token, exchange=exchange)
            cursor.execute(stmt)
            data = cursor.fetchall()
        print data
        if not data:
            return 0
        return data[0]["amount"]

class TranscationRecords(object):
    def __init__(self):
        pass

    def get_transcation_by_exchange_and_token(self):
        pass
token_recorder = TokenRecoder()
exchange_tokens = ExchangeTokens()
