# -*- coding=utf-8 -*-
from libs.utils import create_exchange
from settings.tokens import TOKENS

class Tokens(object):
    @staticmethod
    def get_common_tokens(primary,secondary,*others):
        common_tokens = set()
        exchanges = [primary, secondary]
        exchanges.extend(others)
        for exchange in exchanges:
            exchange = create_exchange(exchange)
            tokens = exchange.get_symbols()
            # print tokens
            if not common_tokens:
                common_tokens = set(tokens)
            tokens = set(tokens)
            common_tokens = common_tokens & tokens
        return list(common_tokens)

class Token(object):
    def __init__(self, token):
        self.token = token
        self.orders = {}
        self.token_orders = {}

    def get_token_order_info(self, exchanges):
        for exchange in exchanges:
            i = exchange
            exchange = create_exchange(exchange)
            token_orders = exchange.get_token_orders(self.token)
            token_orders = exchange.parser_order_items(self.token, token_orders)
            self.token_orders[i] = token_orders
            # print self.token_orders

    def get_lowest_asks_price(self):
        """最低买入价"""
        prices = []
        for exchange ,token_orders in self.token_orders.items():
            item = {}
            item["price"] = token_orders.get_lowest_asks_price(token_orders.orderitems)
            item["exchange"] = exchange
            prices.append(item)
        # print prices
        seq = [x["price"] for x in prices]
        price = min(seq)
        for item in prices:
            if item["price"] == price:
                return item

    def get_highist_bids_price(self):
        """最高卖出价"""
        prices = []
        for exchange ,token_orders in self.token_orders.items():
            item = {}
            item["price"] = token_orders.get_highist_bids_price(token_orders.orderitems)
            item["exchange"] = exchange
            prices.append(item)
        seq = [x["price"] for x in prices]
        price = max(seq)
        for item in prices:
            if item["price"] == price:
                return item

    def summary(self):
        item = {}
        item["token"] = self.token
        item["bids"] = self.get_highist_bids_price()
        item["asks"] = self.get_lowest_asks_price()
        # print self.get_lowest_bid_price(),self.get_highist_ask_price()
        item["profit"] = (self.get_highist_bids_price()["price"]- self.get_lowest_asks_price()["price"])/self.get_highist_bids_price()["price"]*100
        return item
if __name__ == "__main__":
    # tokens = Tokens.get_common_tokens("liqui","hitbtc")
    tokens = TOKENS
    items = []
    for token in tokens:
        try:
            t = Token(token)
            t.get_token_order_info(["liqui","hitbtc"])
            item = t.summary()
            if item["profit"] > 1:
                print item
        except:
            pass
    # print items