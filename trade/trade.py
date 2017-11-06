from libs.utils import create_exchange
from account.models import exchange_tokens
class Trade(object):
    # @staticmethod
    def arrange_order(self,token,ask, bid, amount):
        # print ask, bid
        # print "eeeeee"
        my_bid_exchange = create_exchange(ask.exchange)
        my_ask_exchange = create_exchange(bid.exchange)
        # symbol, side, price,quantity
        print ask.exchange, token, "buy", ask.price, amount
        print bid.exchange, token,"sell", bid.price, amount
        # if not self.check_enough_token(ask.exchange, "eth", ask.price*amount):
            # return 
        # if not self.check_enough_token(bid.exchange, token, amount):
            # return
        amount = self.get_smallest_amount(token, ask.exchange, ask.price, bid.exchange, amount)
        print ask.exchange, token, "buy", ask.price, amount
        print bid.exchange, token,"sell", bid.price, amount
        my_bid_exchange.order(token,"buy", ask.price, amount)
        my_ask_exchange.order(token,"sell", bid.price, amount)

    def get_smallest_amount(self, token,ask_exchange,ask_price, bid_exchange, amount ):
        ask_eth = exchange_tokens.get_exchange_token_amount("eth", ask_exchange)
        ask_amount = ask_eth/ask_price
        bid_amount = exchange_tokens.get_exchange_token_amount(token, bid_exchange)
        return min([ask_amount, bid_amount, amount])
        # pass
    # @classmethod
    def order(self,token,pairs):
        for pair in pairs:
            profit = pair["profit"]
            if profit <1:
                continue
            ask = pair["ask"]
            bid = pair["bid"]
            amount = pair["amount"]
            # print profit, ask.price,ask.amount, ask.exchange, ask.type, bid.price, bid.amount, bid.exchange,bid.type, amount
            self.arrange_order(token,ask, bid, amount)
            break

        # bid_queue = token_item["depth"]
auto_trader = Trade()
if __name__ == "__main__":
    t = Trade()
    t.order(pairs)
