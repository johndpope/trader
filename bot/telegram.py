import json
import tornado.httpclient

from settings.telegram import API_TOKEN

class Bot(object):
    def __init__(self):
        self.prefix = "https://api.telegram.org/bot" + API_TOKEN

    @staticmethod
    def _sync_fetch(url, method, data):
        try:
            client = tornado.httpclient.HTTPClient()
            response = client.fetch(url,method="POST",body=data)
        except tornado.httpclient.HTTPError as e:
            print e.response

    @classmethod
    def post(cls, url, data):
        return cls._sync_fetch(url,"POST", data)

    def sendmsg(self, chat_id, msg):
        url = self.prefix + '/' + 'sendMessage'
        data = "chat_id={chat_id}&text={msg}".format(chat_id = chat_id, msg = msg)
        self.post(url, data)

telegram_bot = Bot()
if __name__ == "__main__":
    b = Bot()
    b.sendmsg(-1001121650710,"a test")