

def ParseSeqFile(string):

    text_file = open(string, 'r')

    lines = text_file.readlines()
    dictionary_of_lines = {}

    try:
        for lines in lines:
            if not (lines[0].startswith('>') or lines[0].startswith('\n')):
                raise ValueError("malformed input at:", lines)
            else:
                if not lines[0].startswith('\n'):
                    text = lines[1:]
                    species = text.split()[0]
                    the_rest = text.split()[1:]

                    #print(species)
                    #print(the_rest)
                    dictionary_of_lines[species] = the_rest

    except ValueError as ve:
        print(ve)

    print(dictionary_of_lines)

ParseSeqFile("dummy file.txt")


