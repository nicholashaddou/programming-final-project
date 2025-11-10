import numpy
import string

def ParseSeqFile(string):
    text_file = open(string, 'r')
    #print(text_file.read())
    lines = text_file.readlines()
    dictionary_of_lines = {}

    try:
        for lines in lines:
            if not (lines[0].startswith('>') or lines[0].startswith('\n')):
                raise ValueError("malformed input at:", lines)
            else:
                text = lines[1:]
                species = text.split()[0]
                the_rest = text.split()[1:]
                #print(species)
                #print(the_rest)

    except ValueError as ve:
        print(ve)

ParseSeqFile("dummy file.txt")


