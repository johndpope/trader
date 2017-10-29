import copy
import traceback
from models.order import OrderItem


class Depth(object):

    @staticmethod
    def parse_depth(asks, bids):
        asks = sorted(asks, key= lambda ask: ask.price)
        bids = sorted(bids, key= lambda bid: bid.price, reverse=True)
        bid_bucket = None
        ask_bucket = None
        total = {
            "depth":0,
            "ask_eth":0,
            "bid_eth":0
        }
        depth = []
        while True:
            try:
                if not ask_bucket or ask_bucket.amount == 0:
                    ask_bucket = asks[0]
                    asks = asks[1:]
                if not bid_bucket or bid_bucket.amount == 0:
                    bid_bucket = bids[0]
                    bids = bids[1:]
            except:
                return depth
            if ask_bucket.price >= bid_bucket.price:
                return depth
            decrese_amount = min(bid_bucket.amount, ask_bucket.amount)
            trade_ask_bucket = copy.copy(ask_bucket)
            trade_bid_bucket = copy.copy(bid_bucket)
            trade_ask_bucket.amount = decrese_amount
            trade_bid_bucket.amount = decrese_amount
            bid_bucket.amount -= decrese_amount
            ask_bucket.amount -= decrese_amount
            total["depth"] += decrese_amount
            total["ask_eth"] += decrese_amount*ask_bucket.price
            total["bid_eth"] += decrese_amount*bid_bucket.price
            total["profit"] = "{0:.2f}%".format((total["bid_eth"] - total["ask_eth"])/total["bid_eth"]*100)
            print trade_ask_bucket.price, trade_bid_bucket.price, amount
            t = copy.copy(total)
            # print t
            depth.append(t)
    @staticmethod
    def parse_auto_order(asks, bids):
        print 1
        asks = sorted(asks, key= lambda ask: ask.price)
        print 2
        bids = sorted(bids, key= lambda bid: bid.price, reverse=True)
        print 3
        trade_ask_bucket = None
        trade_bid_bucket = None
        pairs = []
        while True:
            try:
                if not trade_ask_bucket:
                    trade_ask_bucket = asks[0]
                    asks = asks[1:]
                if not trade_bid_bucket:
                    trade_bid_bucket = bids[0]
                    bids = bids[1:]
                print trade_ask_bucket.price*trade_ask_bucket.amount,trade_bid_bucket.price*trade_bid_bucket.amount,trade_ask_bucket.amount, trade_bid_bucket.amount
                if trade_ask_bucket.price*trade_ask_bucket.amount >= 0.1 and trade_bid_bucket.price*trade_bid_bucket.amount >= 0.1:
                    amount = min([trade_ask_bucket.amount,trade_bid_bucket.amount])
                    bid_eth = trade_bid_bucket.price*amount
                    ask_eth = trade_ask_bucket.price*amount
                    # print trade_ask_bucket.price
                    # print trade_bid_bucket.price
                    print "pass...",bid_eth - ask_eth
                    pair = {
                        "bid":trade_bid_bucket,
                        "ask":trade_ask_bucket,
                        "amount":min([trade_ask_bucket.amount,trade_bid_bucket.amount]),
                        "profit":"{0:.2f}".format((bid_eth - ask_eth)/bid_eth*100)
                    }
                    pairs.append(pair)
                    if amount == trade_ask_bucket.amount:
                        trade_ask_bucket = asks[0]
                        asks = asks[1:]
                    else:
                        trade_bid_bucket = bids[0]
                        bids = bids[1:]
                elif trade_ask_bucket.price*trade_ask_bucket.amount < 0.1:
                    trade_ask_bucket = asks[0]
                    asks = asks[1:]
                elif trade_bid_bucket.price*trade_bid_bucket.amount < 0.1:
                    trade_bid_bucket = bids[0]
                    bids = bids[1:]
            except:
                traceback.print_exc()
                return pairs

token_depth = Depth()