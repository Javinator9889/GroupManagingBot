import pickle
import Constants


def getDBPassword():
    with open(Constants.db_password_path, "rb") as passFile:
        password = pickle.load(passFile)["password"]
        passFile.close()
    return password
