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
            if not (line[0].startswith('>') or line[0].isspace()):
                raise ValueError(f"malformed input at: {line}")
            else:
                if not line[0].isspace():
                    parts = line.split()
                    label = parts[0]
                    sequence = " ".join(parts[1:]) #depending on P2, we can change this to a " " to leave the gap and later on put a - for genomic gap
                    dictionary_of_lines[label] = sequence

    except ValueError:
        text_file.close()
        raise ValueError("Malformed input")

    #This is not efficient, works for now but we should make it more efficient later
    try:
        for words in dictionary_of_lines.values():
            for char in words:
                if char not in ('A', 'C', 'T', 'G', 'a', 'c', 't', 'g') and not char.isspace():
                    raise ValueError(f"malformed input due to: {char} at {words}")

    except ValueError:
        text_file.close()
        raise ValueError("Malformed input")

    text_file.close()
    list_from_dictionary = list(dictionary_of_lines.items())
    return list_from_dictionary

ParseSeqFile("dummy file alignment.txt")