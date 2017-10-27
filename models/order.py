import json
class OrderItem(object):
    def __init__(self, item):
        self.type = item["type"]
        self.price = float(item["price"])
        self.amount = float(item["amount"])

    def worth(self):
        return self.price*self.amount

class Orders(object):
    def __init__(self, token, orders):
        self.token = token
        self.orderitems = [ OrderItem(item) for item in orders]

    def _filter_bids(self, price):
        return filter(lambda x:x.price >= price, self.orderitems)

    def _filter_asks(self, price):
        return filter(lambda x:x.price <= price, self.orderitems)

    @staticmethod
    def get_lowest_asks_price(orderitems):
        orderitems = filter(lambda x:x.type == "asks", orderitems)
        seq = [x.price for x in orderitems ]
        return min(seq)

    @staticmethod
    def get_highist_bids_price(orderitems):
        # print orderitems
        orderitems = filter(lambda x:x.type == "bids", orderitems)
        # print orderitems
        seq = [x.price for x in orderitems ]
        # print "seq,",seq
        return max(seq)