import time
from settings.tokens import TOKENS
from tools.ethtoken import Token
from tools.report import report,report_with_depth

def get_profit_tokens_and_report():
    tokens = TOKENS
    items = []
    for token in tokens:
        try:
            t = Token(token)
            t.get_token_order_info(["liqui","hitbtc"])
            item = t.summary()
            print item
            if item["profit"] > 2:
                report_with_depth(item)
        except Exception as e:
            print str(e)
            pass

if __name__ == "__main__":
    while True:
        get_profit_tokens_and_report()
        time.sleep(100)