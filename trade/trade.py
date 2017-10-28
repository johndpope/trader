class Trade(object):
    @staticmethod
    def order(pairs):
        profit = pairs["profit"]
        ask = pairs["ask"]
        bid = pairs["bid"]
        arrange_order(ask, bid)
        # bid_queue = token_item["depth"]
if __name__ == "__main__":
    t = Trade()
    t.order(itme1, item2)