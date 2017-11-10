import time
from account.scanner import account_scanner
from exchangetools.report import report_token

def main():
    while True:
        new_tokens = account_scanner.scan_all_exchanges()
        for exchange, tokens in new_tokens.items():
            if tokens:
                report_token(exchange, tokens)
        time.sleep(4)
        # for token_pair in token_pairs:
        #     balance._balance_between_account(token_pair["from"], token_pair["to"], token_pair["amount"])

if __name__ == "__main__":
    main()
