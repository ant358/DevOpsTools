# set up logging
import logging
from datetime import datetime
# fileops is in this DevOpsRepo too!
from fileops import get_abs_path

# get todays date
datestamp = datetime.now().strftime('%Y%m%d')

# append date to logfile name
log_name = f'log-{datestamp}.txt'
# path = './logs/'
# replace get_abs_path with path above for a simpler setup
log_filename = get_abs_path(['logs', log_name])
# print(log_filename)
# create log if it does not exist
if not log_filename.exists():
    # check the  logs dir exists - create it
    get_abs_path(['logs']).mkdir(exist_ok=True)
    # create the file
    log_filename.touch(exist_ok=True)


# create logger
logger = logging.getLogger()
# set minimum output level
logger.setLevel(logging.DEBUG)
# Set up the file handler
file_logger = logging.FileHandler(log_filename)

# create console handler and set level to debug
ch = logging.StreamHandler()
# set minimum output level
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('[%(levelname)s] -'
                              ' %(asctime)s - '
                              '%(name)s : %(message)s')
# add formatter
file_logger.setFormatter(formatter)
ch.setFormatter(formatter)
# add a handler to logger
logger.addHandler(file_logger)
logger.addHandler(ch)
# mark the run
logger.info('Logging Started')
