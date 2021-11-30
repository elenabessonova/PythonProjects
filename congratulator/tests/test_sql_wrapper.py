import os
import pytest
import sqlite3
from db_controller.sql_wrapper import SQLiteWrapper
from db_controller.db_configure import configure_db
import env


class TestSQLWrapper:

    def test_sql_wrapper(self):
        db_name = os.path.join(os.path.dirname(__file__), 'test_congrat.db')
        db_exists = os.path.exists(db_name)
        if db_exists:
            os.remove(db_name)
        conn = sqlite3.connect(db_name)
        with SQLiteWrapper(conn) as obj:
            configure_db(conn)

            obj.execute("INSERT INTO USERS (ID, NAME, SURNAME, BIRTHDAY, EMAIL)"
                        "VALUES (1, 'Elena', 'B.', '22.11', 'lena_bess@list.ru')")

            users = obj.select('SELECT name, surname, birthday, email FROM USERS')
            user = ['Elena', 'B.', '22.11', 'lena_bess@list.ru']
            assert(user in users)

        os.remove(db_name)


if __name__ == '__main__':
    pytest.main()
