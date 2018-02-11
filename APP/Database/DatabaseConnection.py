import pymysql
from Data import Constants


class DatabaseConnection:
    def __init__(self):
        self.PyMySQL_Connection = pymysql.connect(Constants.db_host, Constants.db_username, Constants.db_password,
                                                  Constants.db_database, charset=Constants.db_charset)

    def saveGroupID(self, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("INSERT INTO `group` (chat_id) VALUE (?)", chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupRules(self, rules, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET rules = ? WHERE chat_id = ?", rules, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupLink(self, url, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET link = ? WHERE chat_id = ?", url, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupName(self, name, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET name = ? WHERE chat_id = ?", name, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupStickersEnabled(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET sitckers_enabled = ? WHERE chat_id = ?", enabled, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupBotsEnabled(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET bots_enabled = ? WHERE chat_id = ?", enabled, chat_id)
        self.PyMySQL_Connection.commit()

    def setGroupAutoShortenLinks(self, enabled, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `group` SET auto_shorten_links = ? WHERE chat_id = ?", enabled, chat_id)
        self.PyMySQL_Connection.commit()

    def setUserInGroup(self, user_id, chat_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("INSERT INTO `user_has_group` (user_id, chat_id, in_revision, spam, is_admin) VALUES (?, ?, ?, ?, ?)",
                  user_id, chat_id, False, False, False)
        self.PyMySQL_Connection.commit()

    def setUserInRevision(self, user_id, chat_id, in_revision):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `user_has_group` SET in_revision = ? WHERE chat_id = ? AND user_id = ?", in_revision, chat_id,
                  user_id)
        self.PyMySQL_Connection.commit()

    def setUserAdmin(self, user_id, chat_id, is_admin):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `user_has_group` SET is_admin = ? WHERE chat_id = ? AND user_id = ?", is_admin, chat_id,
                  user_id)
        self.PyMySQL_Connection.commit()

    def setUserSpam(self, user_id, chat_id, spam):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `user_has_group` SET spam = ? WHERE chat_id = ? AND user_id = ?", spam, chat_id, user_id)
        self.PyMySQL_Connection.commit()

    def setUser(self, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("INSERT INTO `user` (user_id) VALUE (?) ON DUPLICATE KEY UPDATE user_id = ?", user_id, user_id)
        self.PyMySQL_Connection.commit()

    def setUserUsername(self, username, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `user` SET username = ? WHERE user_id = ?", username, user_id)
        self.PyMySQL_Connection.commit()

    def setUserName(self, name, user_id):
        c = self.PyMySQL_Connection.cursor()
        c.execute("UPDATE `user` SET name = ? WHERE user_id = ?", name, user_id)
        self.PyMySQL_Connection.commit()

    def closeDB(self):
        self.PyMySQL_Connection.close()
