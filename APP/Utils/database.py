import pickle
from Data import Constants


class DatabaseData:
    def __init__(self):
        self.file = open(Constants.values_path, "rb")

    def getDBUser(self):
        return pickle.load(self.file)["DATABASE"]["DB_USER"]

    def getDBPassword(self):
        return pickle.load(self.file)["DATABASE"]["DB_PASS"]

    def getDBDatabase(self):
        return pickle.load(self.file)["DATABASE"]["DB_DATABASE"]

    def getDBHost(self):
        return pickle.load(self.file)["DATABASE"]["DB_HOST"]

    def getDBCharset(self):
        return pickle.load(self.file)["DATABASE"]["DB_CHARSET"]

    def closeFile(self):
        self.file.close()
