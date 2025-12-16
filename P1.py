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
                raise ValueError(f"malformed input at: {line}") #fine

            if line.startswith('>'):
                parts = line[1:].split()
                if len(parts) < 2:
                    raise ValueError(f"malformed input at: {line}")

                label = parts[0]
                sequence = parts[1]
                dictionary_of_lines[label] = sequence

        for words in dictionary_of_lines.values():
            for char in words:
                if char not in ('A', 'C', 'T', 'G', 'a', 'c', 't', 'g') and not char.isspace():
                    raise ValueError(f"malformed input due to: {char} at {words}")

    except ValueError:
        text_file.close()
        raise ValueError("Malformed input")

    text_file.close() #probably should just use 'with open' instead but whatevs it works for now
    list_from_dictionary = list(dictionary_of_lines.items())

    print(list_from_dictionary)
    return list_from_dictionary

def get_label():

    genomic_sequence = ParseSeqFile("dummy file alignment.txt")
    list_of_labels = []
    for labels in genomic_sequence:
        string_sequence = labels[0]
        list_of_labels.append(string_sequence)

    print(list_of_labels)
    return list_of_labels

get_label()