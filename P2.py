import P1

"""
compare two sequences of two different species, which come in the form of a list of pairs

we have to iterate through the string, compare each char, and give the corresponding values
values:
        match = 2
        mismatch = -1
        gap = -2
choose the best outcome for the end sequence

if there is a gap, put " - " so the end sequences would have the same length
"""
genomic_sequence = P1.dictionary_to_list("dummy file.txt") # this is a list

#method to extract the string of sequence from the list, label is stored elsewhere
def get_sequence_string():

    list_of_sequences = []

    for sequence in genomic_sequence:
        string_sequence = sequence[1]
        list_of_sequences.append(string_sequence)

    print(list_of_sequences)
    return list_of_sequences

def get_label():

    list_of_labels = []
    for labels in genomic_sequence:
        string_sequence = labels[0]
        list_of_labels.append(string_sequence)

    print(list_of_labels)
    return list_of_labels

get_label()
sorted_sequence = get_sequence_string()

def AlignByDP(string):

    match = 2
    mismatch = -1
    gap = -2


