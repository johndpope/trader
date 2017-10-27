import time
from settings.tokens import HITBTC_TOKENS, LIQUI_TOKENS, BITTREX_TOKENS
from exchangetools.ethtoken import Token
from exchangetools.report import report,report_with_depth

def get_profit_tokens_and_report():
    # tokens = TOKENS
    tokens = set(HITBTC_TOKENS) | set(LIQUI_TOKENS) | set(BITTREX_TOKENS)
    items = []
    for token in tokens:
        try:
            exchanges = []
            if token in HITBTC_TOKENS:
                exchanges.append("hitbtc")
            if token in LIQUI_TOKENS:
                exchanges.append("liqui")
            if token in BITTREX_TOKENS:
                exchanges.append("bittrex")
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