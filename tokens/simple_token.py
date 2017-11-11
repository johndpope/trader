# -*- coding=utf-8 -*-
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
if __name__ == "__main__":
    t = Tokens()
    print t.get_token_timeline("rdn")
