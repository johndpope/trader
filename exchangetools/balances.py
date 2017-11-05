import time
from account.scanner import account_scanner
from exchangetools.report import report_balance

def main():
    while True:
        # account_scanner.scan_all_account_and_save()
        # time.sleep(1)
        # token_pairs = account_scanner.get_transfer_token_pairs()
        # ret = []
        balances = account_scanner.get_balances()
        items = []
        for item in balances:
            if item["amount"] !=0:
                items.append(item)
        # for exchange in ["hitbtc", "binance"]:
            # ret.extends(account_scanner.get_balances(exchange))
        report_balance(items)
        print "time to sleep...."
        time.sleep(100)
        # for token_pair in token_pairs:
        #     balance._balance_between_account(token_pair["from"], token_pair["to"], token_pair["amount"])

if __name__ == "__main__":
    main()