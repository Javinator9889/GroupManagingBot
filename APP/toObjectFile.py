import sys
import pickle

telegram = {'TOKEN': sys.argv[1]}
with open("TOKEN.dat", "wb") as file:
    pickle.dump(telegram, file)
    file.close()
print("Token correctly written")
