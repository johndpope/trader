import json
import models
from exchanges.common import Exchange

class Bittrex(Exchange):
    def __init__(self):
        self._prefix = "https://bittrex.com/api/v1.1/"

    def get_symbols(self):
        url = self._prefix  + "/public/getmarkets"
        symbols = json.loads(self._fetch(url))["result"]
        raw_items = filter(lambda x:x["BaseCurrency"] == "ETH", symbols)
        return [ item["MarketCurrency"].lower() for item in raw_items ]

    def get_token_orders(self, token):
        # url = self._prefix + '/depth/' + token.lower() + "_eth"
        url = self._prefix + '/public/getorderbook?market=ETH-{token}&type=both'.format(token = token.upper())
        return self._fetch(url)
    def parser_order_items(self, token, response):
        orders = json.loads(response)["result"]
        new_orders = []
        TYPE = {
            "buy":"bids",
            "sell":"asks"
        }
        for _type,values in orders.items():
            for item in values:
                i = {
                    "type":TYPE[_type],
                    "price":item["Rate"],
                    "amount":item["Quantity"]
                }
                new_orders.append(i)

        token_orders = models.order.Orders(token.lower(),new_orders)
        return token_orders
    def order(self,symbol, side, price,quantity):
        """/api/1/trading/new_order"""
        key = HITBTC["key"]
        secret = HITBTC["secret"]
        nonce = str(int(time.mktime(datetime.datetime.now().timetuple()) * 1000 + datetime.datetime.now().microsecond / 1000))
        clientOrderId = "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))
        path = "/api/1/trading/new_order?apikey=" + key + "&nonce=" + nonce
        newOrder = "clientOrderId=" + clientOrderId + "&symbol={symbol}&side={side}&price={price}&quantity={quantity}&type=limit"
        signature = hmac.new(secret, path + newOrder, hashlib.sha512).hexdigest()
        result = self.post("http://api.hitbtc.com" + path, headers={"Api-Signature": signature}, data=newOrder)
        # print result.body['ExecutionReport']
        print result
if __name__ == "__main__":
    b = Bittrex()
    print b.get_symbols()
