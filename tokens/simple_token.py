# -*- coding=utf-8 -*-
import tornado.ioloop
import tornado.web
from datetime import date
from libs.db import aquire_cursor

class Tokens(object):

    def get_token_timeline(self, token):
        with aquire_cursor() as cursor:
            stmt = "select * from simple_token where token='{token}'".format(token=token)
            cursor.execute(stmt)
            data = cursor.fetchall()
        return self.as_timeline(data)

    @staticmethod
    def as_timeline(items):
        ret = []
        for item in items:
            d = {}
            d["title"] = item["token"] + " list on " + item["exchange"]
            d["create_time"] = str(item["create_time"])
            ret.append(d)
        return ret

token_model = Tokens()
class TokenTimeLineHandler(tornado.web.RequestHandler):
    def get(self):
        token = self.get_argument("token","knc")
        ret = token_model.get_token_timeline(token)
        # today = date.today()
        self.finish(ret)

def make_app():
    return tornado.web.Application([
        (r"/api/v1/token/timeline", TokenTimeLineHandler),
    ],
    #debug = True,
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    t = Tokens()
    print t.get_token_timeline("rdn")
