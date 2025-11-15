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
    for _ in genomic_sequence:
        sequence = genomic_sequence[0]
        string_sequence = sequence[1]
        list_of_sequences.append(string_sequence)

    return list_of_sequences

sorted_sequence = get_sequence_string()

def AlignByDP(string):

    match = 2
    mismatch = -1
    gap = -2


