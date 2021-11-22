class Logger:
    '''
    High loging level 'debug' - print all messages
    Low loging level  'info'  - print only info messages
    '''
    def __init__(self, level):
        self._level = level

    def debug(self, msg):
        if self._level == 'debug':
            print(msg)
            return msg
        else:
            return ''

    def info(self, msg):
        if self._level == 'info' or self._level == 'debug':
            print(msg)
            return msg
        else:
            return ''


if __name__ == '__main__':
    logger = Logger('info')
    logger.debug('debug msg')
    logger.info('info msg')
