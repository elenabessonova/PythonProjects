import logging
import os


logger = logging.getLogger('congratulator')
logger.setLevel(logging.DEBUG)

logfilepath = os.path.dirname(os.path.dirname(__file__))
logfile = os.path.join(logfilepath, 'congratulator.log')

file_handler = logging.FileHandler(logfile)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
