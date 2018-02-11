from Utils.database import DatabaseData
"""
File that contains constants that will be used in the bot
"""
# Bot values path
values_path = "Data/BOT_VALUES.dat"

# bot.py values
workers = 200

# Database values
db_data = DatabaseData()
db_username = db_data.getDBUser()
db_password = db_data.getDBPassword()
db_database = db_data.getDBDatabase()
db_host = db_data.getDBHost()
db_charset = db_data.getDBCharset()
db_data.closeFile()
