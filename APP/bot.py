import pickle
import Constants

from telegram.ext.updater import Updater

with open("TOKEN.dat", "rb") as tokenFile:
    TOKEN = pickle.load(tokenFile)["TOKEN"]
    tokenFile.close()
updater = Updater(TOKEN, workers=Constants.workers)
