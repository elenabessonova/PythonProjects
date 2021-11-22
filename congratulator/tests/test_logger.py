import pytest
from congratulator.common.logger import Logger


class TestLogger:

    def test_info(self):
        t_logger = Logger('info')
        print_info = t_logger.info('info message')
        print_debug = t_logger.debug('debug message')

        assert(print_info == 'info message')
        assert(print_debug == '')

    def test_debug(self):
        t_logger = Logger('debug')
        print_info = t_logger.info('info message')
        print_debug = t_logger.debug('debug message')

        assert (print_info == 'info message')
        assert (print_debug == 'debug message')

    def test_none(self):
        t_logger = Logger('none')
        print_info = t_logger.info('info message')
        print_debug = t_loger.debug('debug message')

        assert (print_info == '')
        assert (print_debug == '')


if __name__ == '__main__':
    pytest.main()
