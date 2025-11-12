"""
Module for parsing sequence files.

This module provides functions to read sequence files, extract headers and sequences,
and validate the input data. Functions in this module raise `ValueError` for
malformed inputs, such as incorrect headers or invalid characters in sequences.
"""
def ParseSeqFile(string):

    text_file = open(string, 'r')

    lines = text_file.readlines()
    dictionary_of_lines = {}

    try:
        for line in lines:
            if not (line[0].startswith('>') or line[0].startswith('\n')):
                raise ValueError(f"malformed input at: {line}")
            else:
                if not line[0].startswith('\n'):
                    parts = line.split()
                    label = parts[0]
                    sequence = "".join(parts[1:])
                    dictionary_of_lines[label] = sequence

    except ValueError:
        raise ValueError("Malformed input")

    #This is not efficient, works for now but we should make it more efficient later
    try:
        for words in dictionary_of_lines.values():
            for char in words:
                if char not in ('A', 'C', 'T', 'G') and not char.isspace():
                    raise ValueError(f"malformed input due to: {char} at {words}")
    except ValueError:
        raise ValueError("Malformed input")

    text_file.close()
    return dictionary_of_lines

def dictionary_to_list(string):
    ParseSeqFile(string)
    list_from_dictionary = list(ParseSeqFile(string).items())
    print (list_from_dictionary)
    return list_from_dictionary

dictionary_to_list("dummy file.txt")