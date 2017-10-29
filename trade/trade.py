class Trade(object):
    def arrange_order(ask, bid):
        print ask, bid
        print "eeeeee"
        # bid_exchange = create_exchange(ask.exchange)
        # ask_exchange = create_exchange(bid.exchange)
        # bid_exchange.order(ask.token,"sell" ask.amount, ask.price)
        # ask_exchange.order(bid.token, "buy", bid.amount, bid.price)
        pass
    @classmethod
    def order(cls,pairs):
        for pair in pairs:
            profit = pair["profit"]
            ask = pair["ask"]
            bid = pair["bid"]
            amount = pair["amount"]
            print profit, ask.price,ask.amount, ask.exchange, ask.type, bid.price, bid.amount, bid.exchange,bid.type, amount
        #cls.arrange_order(ask, bid)

        # bid_queue = token_item["depth"]
auto_trader = Trade()
if __name__ == "__main__":
    t = Trade()
    t.order(pairs)
