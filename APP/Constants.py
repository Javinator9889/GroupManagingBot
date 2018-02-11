from Utils.database import getDBPassword
"""
File that contains constants that will be used in the bot
"""

# bot.py values
workers = 200
token_path = "Data/TOKEN.dat"

# Database values
db_password_path = "Data/DB_PASSWORD.dat"
db_username = "Bots"
db_password = getDBPassword()
db_database = "groupmanaging"
db_host = "localhost"
db_charset = "utf8"
