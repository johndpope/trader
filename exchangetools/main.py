import time
from exchangetools.ethtoken import Token
from exchangetools.report import report,report_with_depth
from trade.trade import auto_trader
from account.models import exchange_tokens

def get_profit_tokens_and_report():
    # tokens = TOKENS
    # tokens = set(HITBTC_TOKENS) | set(LIQUI_TOKENS) | set(BITTREX_TOKENS)
    tokens = exchange_tokens.get_tokens()
    items = []
    for token in tokens:
        try:
            # exchanges = []
            exchanges = exchange_tokens.get_token_exchanges(token)

            # if token in HITBTC_TOKENS:
                # exchanges.append("hitbtc")
            # if token in LIQUI_TOKENS:
                # exchanges.append("liqui")
            #if token in BITTREX_TOKENS:
            #    exchanges.append("bittrex")
            # print token
            if len(exchanges) <2:
                continue
            # if token != "snm":
                # continue
            t = Token(token)
            t.get_token_order_info(exchanges)
            item = t.summary()
            # print item
            print token, exchanges
            if item["profit"] > 1:
                print "__________import__________"
                #print item
                #report_with_depth(item)
                auto_trader.order(token,item["auto_order"])

        except Exception as e:
            print str(e)
            pass

if __name__ == "__main__":
    while True:
        get_profit_tokens_and_report()
        print "-------------sleep---------------"
        time.sleep(10)
