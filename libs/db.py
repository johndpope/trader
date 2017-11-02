# -*- coding=utf-8-*-

from contextlib import contextmanager
from functools import partial

import MySQLdb
import MySQLdb.cursors
from DBUtils.PooledDB import PooledDB

from settings import ENV, MYSQLCONF



class Db(object):

    def __init__(self, host, user, password, database, port, min_thr, max_thr):
        self.__pool = PooledDB(
            creator=MySQLdb,
            mincached=min_thr,
            maxcached=max_thr,
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=database,
            use_unicode=False,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor)

    def conn(self):
        return self.__pool.connection()


@contextmanager
def common_cursor(database):
    conn = database.conn()
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    yield cursor
    conn.commit()
    cursor.close()
    conn.close()

env = ENV

db = Db(
    MYSQLCONF[env]["host"],
    MYSQLCONF[env]["user"],
    MYSQLCONF[env]["password"],
    MYSQLCONF[env]["database"],
    MYSQLCONF[env]["port"],
    MYSQLCONF[env]["min_thr"],
    MYSQLCONF[env]["max_thr"]
)