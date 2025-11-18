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
genomic_sequence = P1.ParseSeqFile("dummy file alignment.txt") # this is a list

#method to extract the string of sequence and label from the list
def get_sequence_string():

    list_of_sequences = []

    for sequence in genomic_sequence:
        string_sequence = sequence[1]
        list_of_sequences.append(string_sequence)

    # print(list_of_sequences)
    return list_of_sequences

def get_label():

    list_of_labels = []
    for labels in genomic_sequence:
        string_sequence = labels[0]
        list_of_labels.append(string_sequence)

    #print(list_of_labels)
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

class Alignment:
    def __init__(self, sequence1, sequence2, match = 2 ,mismatch = -1,gap = -2):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.matrix = []

    def make_matrix(self):
        row = len(self.sequence1) + 1
        col = len(self.sequence2) + 1

        self.matrix = [[Cell(i,j) for i in range(col) for j in range(row)]]

        for i in range(0,row):
            self.matrix[i][0].score += self.gap
        for j in range(0,col):
            self.matrix[0][j].score += self.gap

    def align_sequences(self):
        self.make_matrix()
        for i in self.matrix:
            for j in self.matrix:
                if self.sequence1[i-1] == self.sequence2[j-1]:
                    diag_score = self.matrix[i-1][j-1].get_score() + self.match
                if self.sequence1[i-1] != self.sequence2[j-1]:
                    diag_score = self.matrix[i-1][j-1].get_score() + self.mismatch
                else:
                    diag_score = self.matrix[i-1][j-1].get_score() + self.gap
        pass

def match_length():

    # Only for two sequences, need to fix for more, not sure how Manuel will input the sequences
    sorted_sequence_list = get_sequence_string()
    for i in range(len(sorted_sequence_list) - 1):
        sorted_sequence_list = [s.replace(" ", "-") for s in sorted_sequence_list]
        if len(sorted_sequence_list[i]) == len(sorted_sequence_list[i + 1]):
            break
        if len(sorted_sequence_list[i]) < len(sorted_sequence_list[i + 1]):
            sorted_sequence_list[i] += "-" * (len(sorted_sequence_list[i + 1]) - len(sorted_sequence_list[i]))
        else:
            sorted_sequence_list[i + 1] += "-" * (len(sorted_sequence_list[i]) - len(sorted_sequence_list[i + 1]))

    print(sorted_sequence_list)

def AlignByDP():

    labels_list = get_label()

    match_length()
    # alignment = Alignment(sorted_sequence_list[0], sorted_sequence_list[1])
    #
    # alignment.align_sequences()


AlignByDP()