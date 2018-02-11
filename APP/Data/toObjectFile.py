import sys
import pickle

''' Use this file for initializing your token file.
    In command line, write: "python toObjectFile.py <YOUR_TELEGRAM_TOKEN>" (without < >)
    And your file will be created for using the bot
'''

try:
    if sys.argv[1] == "-h":
        print("Usage: \n"
              "python toObjectFile.py <filename> <key> <value>\n"
              "    ■ filename: filename of the created file\n"
              "    ■ key: identifier of the value (data is stored as a dictionary)\n"
              "    ■ value: what is going to be written at the specified key\n"
              "    ■ -h: for showing the current menu")
    else:
        filename = sys.argv[1]
        key = sys.argv[2]
        value = sys.argv[3]
        pDict = {key: value}

        with open(filename, "wb") as file:
            pickle.dump(pDict, file)
            file.close()
        print("Data correctly written")
except IndexError:
    print("Write \"python toObjectFile.py -h\" for getting help")
