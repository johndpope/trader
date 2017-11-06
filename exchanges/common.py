import tornado.gen
import tornado.httpclient

import models


class Exchange(object):
    @staticmethod
    def _sync_fetch(url,method="GET",headers=None,data=None):
        httpclient = tornado.httpclient.HTTPClient()
        if method == "GET":
            try:
                response = httpclient.fetch(url, headers= headers)
                return response.body
            except tornado.httpclient.HTTPError as e:
                print e.response
        else:
            try:
                client = tornado.httpclient.HTTPClient()
                print url, method, headers,data 
                response = client.fetch(url,method="POST",headers=headers,body=data)
                return response
            except tornado.httpclient.HTTPError as e:
                print e.response

    @classmethod
    def _fetch(cls, url, headers=None):
        # print url
        return cls._sync_fetch(url, headers=headers)

    @classmethod
    def post(cls, url, data=None, headers=None):
        return cls._sync_fetch(url,method="POST",headers=headers, data=data)
