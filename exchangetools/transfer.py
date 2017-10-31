def main():
    while True:
        scanner.scan_all_account_and_save()
        token_pairs = scanner.get_transfer_token_pairs()
        for token_pair in token_pairs:
            balance._balance_between_account(token_pair["from"], token_pair["to"], token_pair["amount"])