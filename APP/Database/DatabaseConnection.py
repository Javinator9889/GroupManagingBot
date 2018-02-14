import pymysql
from Data import Constants
from Data import SQLQueries as SQL_q


class DatabaseConnection:
    def __init__(self):
        self.PyMySQL_Connection = pymysql.connect(Constants.db_host, Constants.db_username, Constants.db_password,
                                                  Constants.db_database, charset=Constants.db_charset)

    def saveGroupID(self, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.saveGroupID, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupRules(self, rules, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupRules, (rules, chat_id))
        self.PyMySQL_Connection.commit()

    def setGroupLink(self, url, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupLink, (url, chat_id))
        self.PyMySQL_Connection.commit()

    def setGroupName(self, name, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupName, (name, chat_id))
        self.PyMySQL_Connection.commit()

    def setGroupStickersEnabled(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupStickersEnabled, (enabled, chat_id))
        self.PyMySQL_Connection.commit()

    def setGroupBotsEnabled(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupBotsEnabled, (enabled, chat_id))
        self.PyMySQL_Connection.commit()

    def setGroupAutoShortenLinks(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setGroupAutoShortenLinks, (enabled, chat_id))
        self.PyMySQL_Connection.commit()

    def setUserInGroup(self, user_id, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserInGroup, (user_id, chat_id, False, False, False))
        self.PyMySQL_Connection.commit()

    def setUserInRevision(self, user_id, chat_id, in_revision):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserInRevision, (in_revision, chat_id, user_id))
        self.PyMySQL_Connection.commit()

    def setUserAdmin(self, user_id, chat_id, is_admin):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserAdmin, (is_admin, chat_id, user_id))
        self.PyMySQL_Connection.commit()

    def setUserSpam(self, user_id, chat_id, spam):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserSpam, (spam, chat_id, user_id))
        self.PyMySQL_Connection.commit()

    def setUser(self, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUser, (user_id, user_id))
        self.PyMySQL_Connection.commit()

    def setUserUsername(self, username, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserUsername, (username, user_id))
        self.PyMySQL_Connection.commit()

    def setUserName(self, name, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute(SQL_q.setUserName, (name, user_id))
        self.PyMySQL_Connection.commit()

    def closeDB(self):
        self.PyMySQL_Connection.close()
