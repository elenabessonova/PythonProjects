from common.logger import logger as log
from common.logger import logfilepath
import os
import re


MAX_LOGFILE_SIZE = 1024 * 1024


def log_rotation():
    logfile_pattern = re.compile(r'.*\.log')

    for root, dirs, files in os.walk(logfilepath):

        for file in files:
            if len(re.findall(logfile_pattern, file)):
                if os.path.getsize(os.path.join(logfilepath, file)) > MAX_LOGFILE_SIZE:
                    with open(os.path.join(logfilepath, file), 'w+'):
                        log.info(f'Logfile {file} rotated')


if __name__ == '__main__':
    log_rotation()
