class Trade(object):
    def arrange_order(ask, bid):
        print ask, bid
        # bid_exchange = create_exchange(ask.exchange)
        # ask_exchange = create_exchange(bid.exchange)
        # bid_exchange.order(ask.token,"sell" ask.amount, ask.price)
        # ask_exchange.order(bid.token, "buy", bid.amount, bid.price)
        pass
    @classmethod
    def order(cls,pairs):
        profit = pairs["profit"]
        ask = pairs["ask"]
        bid = pairs["bid"]
        cls.arrange_order(ask, bid)

        # bid_queue = token_item["depth"]
auto_trader = Trade()
if __name__ == "__main__":
    t = Trade()
    t.order(pairs)