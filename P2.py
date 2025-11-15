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

# labels_list = get_label()
# sorted_sequence_list = get_sequence_string()

"""
Setting cells
"""
class Cell:
    def __init__(self, row, col):
        self.prev_cell = None
        self.score = 0
        self.row = row
        self.col = col

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def set_previous_cell(self, prev_cell):
        self.prev_cell = prev_cell

    def get_previous_cell(self):
        return self.prev_cell

#----------------------------------------------------------

def AlignByDP():

    labels_list = get_label()
    sorted_sequence_list = get_sequence_string()

    match = 2
    mismatch = -1
    gap = -2

    sequence1 = sorted_sequence_list[0]
    sequence2 = sorted_sequence_list[1]

AlignByDP()




