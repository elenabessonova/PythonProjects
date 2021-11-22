# -*- coding: utf-8 -*-
import sqlite3


class SQLiteWrapper:
    def __init__(self, conn):
        self.__conn = conn

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.__conn.close()

    def execute(self, sql_req):
        self.__conn.execute(sql_req)
        self.__conn.commit()

    def select(self, sql_req):
        self.__conn.row_factory = sqlite3.Row
        cursor = self.__conn.execute(sql_req)
        result = list()
        for row in cursor:
            result.append(list(row))
        return result


