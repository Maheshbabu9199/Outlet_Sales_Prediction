import os
import sys
import logging
from datetime import datetime

log_file = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")+".log"
file_path = os.path.join(os.getcwd(),"Logs")

log_file_path = os.path.join(file_path, log_file)

fmt = '%(asctime)s : %(levelname)s : %(module)s : %(lineno)s : %(message)s'
logging.basicConfig(filename=log_file_path, format=fmt, level=logging.DEBUG, filemode='w')



if __name__ == '__main__':
    logging.info('Starting')