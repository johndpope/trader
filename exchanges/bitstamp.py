import json
import models
import hmac
import hashlib
import time
from exchanges.common import Exchange


class Bitstamp(Exchange):
    def __init__(self):
        self._prefix = "https://www.bitstamp.net"

    def get_symbols(self):
        url = self._prefix  + "/api/v2/trading-pairs-info/"
        symbols = [ item["name"].lower() for item in json.loads(self._fetch(url)) ]
        raw_items = filter(lambda x:x.endswith("usd"), symbols)
        return [ item[:-4].lower() for item in raw_items ]
        # return symbols


if __name__ == "__main__":
    b = Bitstamp()
    # b.withdraw("enj","0x7f59fbfe6C2cBA95173d69B4B0B00E09c76501FC",1000)
    # b.order("enj","buy","0.00005","1000")
    print b.get_symbols()
    # print b.get_token_orders("eos")
    #print b.get_all_price()
