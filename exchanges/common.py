import tornado.gen
import tornado.httpclient

import models


class Exchange(object):
    @staticmethod
    def _sync_fetch(url):
        httpclient = tornado.httpclient.HTTPClient()
        response = httpclient.fetch(url)
        return response.body

    @classmethod
    def _fetch(cls, url):
        # print url
        return cls._sync_fetch(url)