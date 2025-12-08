from sympy import sequence

import P2

def get_sequences():
    pass

def ComputeDistMatrix():

    dictionary_of_distances = P2.AlignByDP()
    sequences_to_compare = []

    for (key, value), (seq1, seq2) in dictionary_of_distances.items():
        sequence1 = seq1
        sequence2 = seq2
        sequences_to_compare.append((sequence1, sequence2))
        p_value = 0
        count = 0

        #only works with smaller first sequence
        for i in sequence1:
            for char in i:
                if char == '-':
                    count += 1
                    length_without_gap = len(i) - count
                    if length_without_gap != 0:
                        p_value = count / length_without_gap
                    else:
                        p_value = 30
        print(count)
        print(p_value)

ComputeDistMatrix()