class Loger:
    '''
    High loging level 'debug' - print all messages
    Low loging level  'info'  - print only info messages
    '''
    def __init__(self, level):
        self._level = level

    def debug(self, msg):
        if self._level == 'debug':
            print(msg)

    def info(self, msg):
        if self._level == 'info' or self._level == 'debug':
            print(msg)


if __name__ == '__main__':
    loger = Loger('info')
    loger.debug('debug msg')
    loger.info('info msg')
