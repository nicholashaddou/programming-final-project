import P2
import math

def ComputeDistMatrix():

    dictionary_of_distances = P2.AlignByDP()

    for key, (seq1, seq2) in dictionary_of_distances.items():
        sequence1 = seq1
        sequence2 = seq2
        difference_count = 0
        length_without_gap = len(sequence1)

        new_sequence = ""
        new_sequence2 = ""

        for i, j in zip(seq1, seq2):
            if i != "-" and j != "-":
                new_sequence += i
                new_sequence2 += j

        #this is stupid, need to get rid of
        for i in range(len(sequence1)):
            if sequence1[i] != sequence2[i] and (sequence1[i] == '-' or sequence2[i] == '-'):
                length_without_gap -= 1

        for i in range(len(new_sequence)):
            if new_sequence[i] != new_sequence2[i]:
                difference_count += 1

        print(length_without_gap) #correct
        #print(difference_count)
        p_value = difference_count / length_without_gap
        print(p_value)

        if p_value >= 0.75:
            evolutionary_distance = 30
        else:
            evolutionary_distance= -(3/4) * math.log(1 - (4/3) * p_value)
        print(evolutionary_distance)

ComputeDistMatrix()