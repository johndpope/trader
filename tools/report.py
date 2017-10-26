from bot.telegram import telegram_bot
"""
{'profit': 2.885652173913046, 'token': u'net', 'bids': {'price': 0.0023, 'exchange': 'hitbtc'}, 'asks': {'price': 0.00223363, 'exchange': 'liqui'}}
"""
def report(item):
    text = "Token:{token}\nProfit:{profit}%\nBids:price:{bprice} exchange:{bexchange}\nAsks:price:{aprice} exchange:{aexchange}".format(
        token = item["token"], profit = "{0:.2f}".format(float(item["profit"])), bprice = item["bids"]["price"], bexchange = item["bids"]["exchange"],
        aprice = item["asks"]["price"], aexchange = item["asks"]["exchange"]
        )
    telegram_bot.sendmsg(-1001121650710,text)

def report_with_depth(item):
    depth = item["depth"]
    depth_text = ""
    for item in depth:
        depth += "Profit:" + item["profit"] + " Depth:" + item["depth"] + "Ask_eth:" + item["ask_eth"] + "Bid_eth:" + item["bid_eth"] + "\n"
    text = "Token:{token}\nProfit:{profit}%\nBids:price:{bprice} exchange:{bexchange}\nAsks:price:{aprice} exchange:{aexchange}\nDepth:{depth}".format(
        token = item["token"], profit = "{0:.2f}".format(float(item["profit"])), bprice = item["bids"]["price"], bexchange = item["bids"]["exchange"],
        aprice = item["asks"]["price"], aexchange = item["asks"]["exchange"],depth = depth_text
        )
    telegram_bot.sendmsg(-1001121650710,text)
if __name__ == "__main__":
    report("x")
