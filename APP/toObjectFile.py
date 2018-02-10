import sys
import pickle

''' Use this file for initializing your token file.
    In command line, write: "python toObjectFile.py <YOUR_TELEGRAM_TOKEN>" (without < >)
    And your file will be created for using the bot
'''
telegram = {'TOKEN': sys.argv[1]}
with open("TOKEN.dat", "wb") as file:
    pickle.dump(telegram, file)
    file.close()
print("Token correctly written")
