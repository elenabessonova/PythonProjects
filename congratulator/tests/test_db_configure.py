import env
import os
import pytest
from db_controller.db_configure import load_users


class TestDB:

    def test_db_rows(self):
        temp_db_path = os.path.join(os.path.dirname(__file__), 'test_congrat.db')
        test_users = load_users(temp_db_path)
        test_user1 = ['Elena', '22.11', 'lena_bess@list.ru']
        test_user2 = ['Tatiana', '24.11', 'bessonov@bk.ru']

        assert(test_user1 in test_users)
        assert(test_user2 in test_users)
        os.remove(temp_db_path)


if __name__ == '__main__':
    pytest.main()
