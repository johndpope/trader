import time
from account.scanner import account_scanner

def main():
    while True:
        # account_scanner.scan_all_account_and_save()
        # time.sleep(1)
        # token_pairs = account_scanner.get_transfer_token_pairs()
        for exchange in ["hitbtc", "binance"]:
            account_scanner.scan_local_balance(exchange)
        print "time to sleep...."
        time.sleep(100)
        # for token_pair in token_pairs:
        #     balance._balance_between_account(token_pair["from"], token_pair["to"], token_pair["amount"])

if __name__ == "__main__":
    main()