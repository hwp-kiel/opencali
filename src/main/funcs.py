import datetime
import os

def convert_str_to_0or1(txt: str) -> int:
    if txt.startswith('0'):
        return 0
    else:
        return 1

def log(txt: str):
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"), txt)
    with open("logger.txt", "a") as myfile:
        myfile.write(datetime.datetime.now().strftime("%H:%M:%S.%f") + '\t' + txt + '\n')

def deletelogger():
    # just to get a clean logger
    os.remove("logger.txt")



