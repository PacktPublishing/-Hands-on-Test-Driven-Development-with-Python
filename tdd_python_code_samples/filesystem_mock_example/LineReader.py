import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad path!")
    infile = open(filename, "r")
    line = infile.readline()
    return line

