from bot.telegram import telegram_bot
"""
{'profit': 2.885652173913046, 'token': u'net', 'bids': {'price': 0.0023, 'exchange': 'hitbtc'}, 'asks': {'price': 0.00223363, 'exchange': 'liqui'}}
"""
def report(item):
    text = "Token:{token}\nProfit:{profit}\nBids:price:{bprice} exchange:{bexchange}\nAsks:price:{aprice} exchange:{aexchange}".format(
        token = item["token"], profit = item["profit"], bprice = item["bids"]["price"], bexchange = item["bids"]["exchange"],
        aprice = item["asks"]["price"], aexchange = item["asks"]["exchange"]
        )
    telegram_bot.sendmsg(-1001121650710,text)
if __name__ == "__main__":
    report("x")