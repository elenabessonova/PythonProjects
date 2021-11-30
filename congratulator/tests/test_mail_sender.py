import env
from mail_controller.mail_sender import send
import pytest


class TestSQLWrapper:

    def test_false_mail_sender(self):
        res = send('unknown_addr@unknown_mail.ru', 'NoName')
        assert(not res)


if __name__ == '__main__':
    pytest.main()
