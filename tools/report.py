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
    depth_text = "___________________________"
    for i in depth[0:6]:
        depth_text += "\nProfit:" + str(i["profit"]) + "  Depth:" + str(i["depth"]) + "  Ask_eth:" + str(i["ask_eth"]) + " Bid_eth:" + str(i["bid_eth"])
    depth_text += "\n__________________________"
    text = "Token:{token}\nProfit:{profit}%\nBids:price:{bprice} exchange:{bexchange}\nAsks:price:{aprice} exchange:{aexchange}\n{depth}".format(
        token = item["token"], profit = "{0:.2f}".format(float(item["profit"])), bprice = item["bids"]["price"], bexchange = item["bids"]["exchange"],
        aprice = item["asks"]["price"], aexchange = item["asks"]["exchange"],depth = depth_text
        )
    telegram_bot.sendmsg(-1001121650710,text)
if __name__ == "__main__":
    report("x")