from libs.utils import create_exchange
class Trade(object):
    @staticmethod
    def arrange_order(token,ask, bid, amount):
        # print ask, bid
        # print "eeeeee"
        bid_exchange = create_exchange(ask.exchange)
        ask_exchange = create_exchange(bid.exchange)
        # symbol, side, price,quantity
        print ask.exchange, token, "buy", ask.price, amount
        print bid.exchange, token,"sell", bid.price, amount
        # bid_exchange.order(token,"buy", ask.price, amount)
        # ask_exchange.order(token,"sell", bid.price, amount)
        # pass
    @classmethod
    def order(cls,token,pairs):
        for pair in pairs:
            profit = pair["profit"]
            if profit <1:
                continue
            ask = pair["ask"]
            bid = pair["bid"]
            amount = pair["amount"]
            # print profit, ask.price,ask.amount, ask.exchange, ask.type, bid.price, bid.amount, bid.exchange,bid.type, amount
            cls.arrange_order(token,ask, bid, amount)
            break

        # bid_queue = token_item["depth"]
auto_trader = Trade()
if __name__ == "__main__":
    t = Trade()
    t.order(pairs)
