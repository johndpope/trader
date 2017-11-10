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

def report_balance(items):
    report_text = ""
    total_value = 0
    for item in items:
        report_text += "Token:{token} Exchange:{exchange} Values_in_eth:{values} Amount:{amount} Price:{price}\n".format(
            token=item["token"], exchange=item["exchange"], amount=item["amount"], price=item["price"], values="{0:.2f}".format(float(item["price"])*float(item["amount"])))
        total_value +=float(item["price"])*float(item["amount"])

    report_text +="------------------\nTotal value in eth:{total_value}\n".format(total_value=total_value)
    telegram_bot.sendmsg(-1001205170565, report_text)

def report_token(exchange, tokens):
    report_text = "Exchange:" + exchange 
    for token in tokens:
        report_text += "\n" + token
    telegram_bot.sendmsg(-1001205170565, report_text)
if __name__ == "__main__":
    report("x")
