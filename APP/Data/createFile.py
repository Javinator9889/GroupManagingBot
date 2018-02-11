import pickle
from pprint import pprint

outputData = {"TOKEN": None,
              "DATABASE": {
                  "DB_USER": None,
                  "DB_PASS": None,
                  "DB_DATABASE": None,
                  "DB_HOST": None,
                  "DB_CHARSET": "utf8"
              }
              }
# Add your keys in "outputData" and then, create the file calling it by "python createFile"


def inputData():
    filename = input("Filename: ")
    for key in outputData:
        if not isinstance(outputData[key], dict):
            outputData[key] = input("Enter value for \"" + key + "\": ")
        else:
            for inKey in outputData[key]:
                outputData[key][inKey] = input("Enter value for \"" + inKey + "\": ")
    putOutData(filename)


def putOutData(filename):
    print("\n")
    pprint(outputData)
    if input("Is this data correct? (Y/n): ").lower() == 'y':
        with open(filename, "wb") as outputFile:
            pickle.dump(outputData, outputFile)
            outputFile.close()
            print("Values saved into file: " + filename)
    else:
        print("\n")
        inputData()


inputData()
