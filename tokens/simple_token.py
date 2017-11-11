# -*- coding=utf-8 -*-
from libs.db import aquire_cursor

class Tokens(object):
    """docstring for Tokens"""
    def __init__(self, arg):
        super(Tokens, self).__init__()
        self.arg = arg

    def get_token_timeline(self, token):
        with aquire_cursor() as cursor:
            stmt = "select exchange from simple_token where token='{token}'".format(token=token)
            cursor.execute(stmt)
            data = cursor.fetchall()
        self.as_timeline(data)

    @staticmethod
    def as_timeline(items):
        ret = []
        for item in items:
            d = {}
            d["title"] = item["token"] + " list on " + item["exchange"]
            d["create_time"] = str(item["create_time"])
            ret.append(d)
        return ret
