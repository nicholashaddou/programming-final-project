import itertools
import P1

genomic_sequence = P1.ParseSeqFile("sequences2.txt") # this is a list

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
"""
Alignment class for the sequences
"""
class Alignment:
    def __init__(self, sequence1, sequence2, match = 5 ,mismatch = -2,gap = -6):
        self.sequence1 = sequence1.upper()
        self.sequence2 = sequence2.upper()
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.matrix = []
    """
    the scoring matrix
    """
    def make_matrix(self):

        row = len(self.sequence1) + 1
        col = len(self.sequence2) + 1

        self.matrix = [[Cell(i, j) for j in range(col)] for i in range(row)] #chatgpt was used here, prompt: what is wrong with this? [block of code]

        for i in range(row):
            self.matrix[i][0].set_score(i * self.gap)
            if i > 0:
                self.matrix[i][0].set_previous_cell(self.matrix[i - 1][0])
        for j in range(col):
            self.matrix[0][j].set_score(j * self.gap)
            if j > 0:
                self.matrix[0][j].set_previous_cell(self.matrix[0][j - 1])
    """
    Sequence Alignment function
    """
    def align_sequences(self):

        self.make_matrix()
        row = len(self.sequence1) + 1
        col = len(self.sequence2) + 1

        aligned_sequences = []

        # might work better
        for i in range(1, row):
            for j in range(1, col):
                diag_score = self.matrix[i - 1][j - 1].get_score() + (
                    self.match if self.sequence1[i - 1] == self.sequence2[j - 1] else self.mismatch
                )
                up_score = self.matrix[i - 1][j].get_score() + self.gap
                left_score = self.matrix[i][j - 1].get_score() + self.gap

                max_score = max(diag_score, up_score, left_score)
                self.matrix[i][j].set_score(max_score)

                # Set prev_cell with tie-aware logic: favor diagonal over gaps
                if max_score == diag_score: #copilot fixed logic here
                    self.matrix[i][j].set_previous_cell(self.matrix[i - 1][j - 1])
                elif max_score == up_score:
                    self.matrix[i][j].set_previous_cell(self.matrix[i - 1][j])
                else:
                    self.matrix[i][j].set_previous_cell(self.matrix[i][j - 1])

        aligned_sequence1 = ""
        aligned_sequence2 = ""
        cell = self.matrix[row - 1][col - 1]

        while cell.get_previous_cell() is not None:
            i, j = cell.get_row(), cell.get_col()
            prev_cell = cell.get_previous_cell()
            prev_i, prev_j = prev_cell.get_row(), prev_cell.get_col()

            if i - 1 == prev_i and j - 1 == prev_j:  # diagonal
                aligned_sequence1 = self.sequence1[i - 1] + aligned_sequence1
                aligned_sequence2 = self.sequence2[j - 1] + aligned_sequence2
            elif i - 1 == prev_i:  # up (gap in seq2)
                aligned_sequence1 = self.sequence1[i - 1] + aligned_sequence1
                aligned_sequence2 = "-" + aligned_sequence2
            else:
                aligned_sequence1 = "-" + aligned_sequence1
                aligned_sequence2 = self.sequence2[j - 1] + aligned_sequence2

            cell = prev_cell

        aligned_sequences.append(aligned_sequence1)
        aligned_sequences.append(aligned_sequence2)

        #print(aligned_sequences)
        return aligned_sequences
"""
This function aligns the P1 sequences based on dynamic programming
"""
def AlignByDP(sequence_list=None):

    if sequence_list is None:
        sequence_list = P1.get_sequence_string()
    # labels_list = get_label()

    # alignment = Alignment(sequence_list[0], sequence_list[1])
    # alignment.align_sequences()

    if sequence_list is None:
        sequence_list = P1.get_sequence_string()
    results = {}

    for i, j in itertools.combinations(range(len(sequence_list)), 2):
        seq1 = sequence_list[i]
        seq2 = sequence_list[j]

        aligner = Alignment(seq1, seq2)
        aligned1, aligned2 = aligner.align_sequences()

        results[(i, j)] = (aligned1, aligned2)

    print(results)
    return results

AlignByDP()