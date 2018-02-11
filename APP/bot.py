import pickle
import Constants

from telegram.ext.updater import Updater

with open(Constants.token_path, "rb") as tokenFile:
    TOKEN = pickle.load(tokenFile)["TOKEN"]
    tokenFile.close()
updater = Updater(TOKEN, workers=Constants.workers)
