import numpy
import string

def ParseSeqFile(string):
    textFile = open(string, 'r')
    print(textFile.read())

ParseSeqFile("dummy file.txt")


