import P2
import math
import numpy as np

def calculate_evolutionary_distance():
    dictionary_of_distances = P2.AlignByDP()
    evolutionary_distance = 0
    distance_dictionary = {}

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

        # this is stupid, need to get rid of
        for i in range(len(sequence1)):
            if sequence1[i] != sequence2[i] and (sequence1[i] == '-' or sequence2[i] == '-'):
                length_without_gap -= 1

        for i in range(len(new_sequence)):
            if new_sequence[i] != new_sequence2[i]:
                difference_count += 1

        # print(length_without_gap) #correct
        # print(difference_count)
        p_value = difference_count / length_without_gap
        # print(p_value)

        if p_value >= 0.75:
            evolutionary_distance = 30
        else:
            evolutionary_distance = -(3 / 4) * math.log(1 - (4 / 3) * p_value)
        print(p_value, evolutionary_distance)
        distance_dictionary[key] = evolutionary_distance

    return distance_dictionary

def ComputeDistMatrix(dictionary_of_distances=None):

    if dictionary_of_distances is None:
        dictionary_of_distances = calculate_evolutionary_distance()

    seq_names = set()
    for key in dictionary_of_distances.keys():
        seq_names.update(key)
    seq_names = sorted(seq_names)
    n = len(seq_names)

    # Initialize matrix
    dist_matrix = np.zeros((n, n))

    name_to_idx = {name: idx for idx, name in enumerate(seq_names)}

    for (seq1_name, seq2_name), dist in dictionary_of_distances.items():
        i, j = name_to_idx[seq1_name], name_to_idx[seq2_name]
        dist_matrix[i][j] = dist
        dist_matrix[j][i] = dist  # ensure symmetry

    print(dist_matrix)

    return dist_matrix

ComputeDistMatrix()