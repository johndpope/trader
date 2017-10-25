from settings.tokens import TOKENS
from tools.ethtoken import Token
from tools.report import report

def get_profit_tokens_and_report():
    tokens = TOKENS
    items = []
    for token in tokens:
        try:
            t = Token(token)
            t.get_token_order_info(["liqui","hitbtc"])
            item = t.summary()
            if item["profit"] > 1:
                report(item)
        except:
            pass

if __name__ == "__main__":
    get_profit_tokens_and_report()