from Data import Constants
import pickle


def getToken():
    with open(Constants.values_path, "rb") as tokenFile:
        token = pickle.load(tokenFile)["TOKEN"]
        tokenFile.close()
    return token
