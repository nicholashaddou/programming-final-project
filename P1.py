import numpy
import string

def ParseSeqFile(string):
    text_file = open(string, 'r')
    #print(text_file.read())
    lines = text_file.readlines()
    list_of_lines = []
    for lines in lines:
        if not (lines[0].startswith('>') or lines[0].startswith('\n')):
            print("malformed input at:", lines)
        # else:
        #     print("valid input at:", lines)
        else:
            list_of_lines.append(lines.strip())
    print(list_of_lines)

ParseSeqFile("dummy file.txt")


