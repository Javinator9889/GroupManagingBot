from Data import Constants
import logging
import time

from Utils.token import getToken
from telegram.ext.updater import Updater


def initLog():
    current_date = time.strftime("%d_%m_%Y")
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.WARNING,
                        filename="botLog" + current_date + ".log",
                        filemode='w')


initLog()
updater = Updater(getToken(), workers=Constants.workers)
dispatcher = updater.dispatcher

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    updater.idle()
