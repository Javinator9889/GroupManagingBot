import pymysql
import Constants


class DatabaseConnection:
    PyMySQL_Connection = ""

    def __init__(self):
        self.PyMySQL_Connection = pymysql.connect(Constants.db_host, Constants.db_username, Constants.db_password,
                                                  Constants.db_database, charset=Constants.db_charset)

    def saveGroupID(self, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("""INSERT INTO `group` (chat_id) VALUE (?)""", chat_id)
        self.PyMySQL_Connection.commit()

    def closeDB(self):
        self.PyMySQL_Connection.close()
