import copy
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
            # if "auto_order" not in total:
            #     total["auto_order"] = []
            # if decrese_amount*ask_bucket.price >= 0.1:
            #     pair = {
            #         "bid":trade_bid_bucket,
            #         "ask":trade_ask_bucket,
            #         "profit":"{0:.2f}".format((bid_bucket.price - ask_bucket.price)*100/bid_bucket.price)
            #     }
            #     total["auto_order"].append(pair)
            t = copy.copy(total)
            # print t
            depth.append(t)
    @staticmethod
    def parse_auto_order(asks, bids):
        asks = sorted(asks, key= lambda ask: ask.price)
        bids = sorted(bids, key= lambda bid: bid.price, reverse=True)
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
                if trade_ask_bucket.price*trade_ask_bucket.amount >= 0.1 && trade_bid_bucket.price*trade_bid_bucket*amount >= 0.1:
                    pair = {
                        "bid":trade_bid_bucket,
                        "ask":trade_ask_bucket,
                        "amount":min([trade_ask_bucket.amount,trade_bid_bucket.amount]),
                        "profile":"{0:.2f}".format((total["bid_eth"] - total["ask_eth"])/total["bid_eth"]*100)
                    }
                    pairs.append(pair)
                elif trade_ask_bucket.price*trade_ask_bucket.amount < 0.1:
                    trade_ask_bucket = asks[0]
                    asks = asks[1:]
                elif trade_bid_bucket.price*trade_bid_bucket.amount < 0.1:
                    trade_bid_bucket = bids[0]
                    bids = bids[1:]
            except:
                return pairs

token_depth = Depth()