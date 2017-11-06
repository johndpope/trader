import time
from settings.tokens import HITBTC_TOKENS, LIQUI_TOKENS, BINANCE_TOKENS
from exchangetools.ethtoken import Token
from exchangetools.report import report,report_with_depth
from account.models import exchange_tokens

def get_profit_tokens_and_report():
    # tokens = TOKENS
    # tokens = set(HITBTC_TOKENS) | set(LIQUI_TOKENS) | set(BINANCE_TOKENS)
    tokens = exchange_tokens.get_tokens()
    items = []
    for token in tokens:
        try:
            exchanges = exchange_tokens.get_token_exchanges(token)
            
            # print token
            if len(exchanges) <2:
                continue
            t = Token(token)
            t.get_token_order_info(exchanges)
            item = t.summary()
            # print item
            print token, exchanges
            if item["profit"] > 2:
                print "__________import__________"
                # print item
                report_with_depth(item)
        except Exception as e:
            print str(e)
            pass

if __name__ == "__main__":
    while True:
        get_profit_tokens_and_report()
        print "-------------sleep---------------"
        time.sleep(100)
