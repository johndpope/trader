import json
import models
import hmac
import hashlib
import time
# import requests
from exchanges.common import Exchange
from settings.account import BINANCE
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Bithumb(Exchange):
    def __init__(self):
        self._prefix = "https://api.bithumb.com"

    def get_symbols(self):
        url = self._prefix  + "/public/ticker/ALL"
        symbols = [ item for item,v in json.loads(self._fetch(url))["data"].items() if isinstance(v,dict)]
        #raw_items = filter(lambda x:x.endswith("ETH"), symbols)
        return [ item.lower() for item in symbols ]


if __name__ == "__main__":
    b = Bithumb()
    # b.withdraw("enj","0x7f59fbfe6C2cBA95173d69B4B0B00E09c76501FC",1000)
    # b.order("enj","buy","0.00005","1000")
    print b.get_symbols()
    # print b.get_token_orders("eos")
    #print b.get_all_price()
