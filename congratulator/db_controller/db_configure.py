# -*- coding: utf-8 -*-
import sqlite3
from congratulator.db_controller.sql_wrapper import SQLiteWrapper
import os
from congratulator.common.loger_config import loger


def configure_db(connection_db):
    cur = connection_db.cursor()
    cur.execute('CREATE TABLE USERS'
                '    (ID       INT   PRIMARY KEY  NOT NULL,'
                '     NAME     TEXT               NOT NULL,'
                '     SURNAME  TEXT               NOT NULL,'
                '     BIRTHDAY TEXT               NOT NULL,'
                '     EMAIL    TEXT               NOT NULL);')


def load_users():
    db_name = 'congrats_db.db'
    db_exists = os.path.exists(db_name)
    if db_exists:
        os.remove(db_name)
    conn = sqlite3.connect(db_name)
    with SQLiteWrapper(conn) as obj:
        configure_db(conn)
        loger.info(f'Data base {db_name} is configured')

        obj.execute("INSERT INTO USERS (ID, NAME, SURNAME, BIRTHDAY, EMAIL)"
                    "VALUES (1, 'Elena', 'B.', '22.11', 'lena_bess@list.ru')")
        obj.execute("INSERT INTO USERS (ID, NAME, SURNAME, BIRTHDAY, EMAIL)"
                    "VALUES (2, 'Tatiana', 'M.', '24.11', 'bessonov@bk.ru')")

        return obj.select('SELECT name, birthday, email FROM USERS')
