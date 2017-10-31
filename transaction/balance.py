
class Balance(object):
    def __init__(self):
        self.transaction = Transaction

    def _balance_between_account(self, balance_record_a, balance_record_b, amount):
        balance_record_a.amount -= amount
        balance_record_a.withdraw += amount
        balance_record_b.disposit += amount
        self.transaction.withdraw(balance_record_a, balance_record_a, amount)

    def balance_between_account_with_hardcode_policy(self, balance_record_a , balance_record_b):
        """when balance, the balance is from a to b"""
        if balance_record_a.deposit != 0 or balance_record_a.withdraw != 0:
            return
        if balance_record_b.deposit != 0 or balance_record_b.withdraw != 0:
            return
        if balance_record_a.amount*balance_record_a.price + balance_record_b.amount*balance_record_b.price < 5:
            return
        amount = (balance_record_a.amount - balance_record_b.amount)/2
        self._balance_between_account(balance_record_a, balance_record_b, amount)

class Transaction(object):
    def withdraw(self, balance_record_a, balance_record_b, amount):
        """how balance"""
        to_address = TOKEN_ADDR[balance_record_b.exchange][balance_record_b.token]
        from_exchange = libs.utils.create_exchange(balance_record_a.exchange)
        from_exchange.withdraw(balance_record_a.token, to_address ,amount)