class Balance(object):
    def __init__(self):
        self.transaction = Transaction

    def balance_between_account(self, account_a, account_b, token):
        if account_a[token].lock or account_b[token].lock:
            return
        if account_a[token].amount >= 3*account_b[token].amount:
            desc_token = (account_a[token].amount - account_b[token].amount)/2
            account_a[token].amount -= desc_token
            account_a[token].withdraw += desc_token
            account_b[token].disposit += disposit
            account_b[token].lock = True
            account_a[token].lock = True
            self.transaction.transact(account_a, account_b, token, amount)

class Transaction(object):
    def transcate(account_from, account_to, token, amount):
        to_address = TOKEN_ADDR[account_to.exchange][token]