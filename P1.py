

def ParseSeqFile(string):

    text_file = open(string, 'r')

    lines = text_file.readlines()
    dictionary_of_lines = {}

    try:
        for line in lines:
            if not (line[0].startswith('>') or line[0].startswith('\n')):
                raise ValueError("malformed input at:", line)
            else:
                if not line[0].startswith('\n'):
                    parts = line.split()
                    header = parts[0]
                    sequence = "".join(parts[1:])
                    dictionary_of_lines[header] = sequence

    except ValueError as ve:
        print(ve)

    try:
        for words in dictionary_of_lines.values():
            for char in words:
                if char not in ('A', 'C', 'T', 'G') and not char.isspace():
                    raise ValueError(f"malformed input at: {char}")
    except ValueError as ve2:
        print(ve2)

    print(dictionary_of_lines)

ParseSeqFile("dummy file.txt")


