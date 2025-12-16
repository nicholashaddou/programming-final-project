import P3
import P2
import numpy as np
from collections import defaultdict

import P1
matrix = P3.ComputeDistMatrix()
#print("matrix from P3:", matrix)

labels = P1.get_label()

def input_validation (matrix,labels):
    # Type checks
    if not isinstance(matrix, np.ndarray):
        raise ValueError("malformed input")
    if not isinstance(labels, list) or not all(isinstance(label, str) for label in labels):
        raise ValueError("malformed input")
    
    # Shape check
    n = len(labels)
    if matrix.shape != (n, n):
        raise ValueError("Malform Input: Distance matrix shape != number of labels")
    
    #diagonal Check
    for i in range(n):
        if matrix[i, i] != 0:
            raise ValueError(f"Distance matrix diagonal element at index {i} != zero")
    
    #symmetry check
    for i in range(n):
        for j in range(n):
            if matrix[i, j] != matrix[j, i]:
                raise ValueError(f"Distance matrix != symmetric @ indices {i}, {j}")
            

def conv_to_2d_dict(matrix, labels):
    conv_dict = defaultdict(dict)
    n = len(labels)
    for i in range(n):
        for j in range(n):
            conv_dict[labels[i]][labels[j]] = matrix[i, j]
    return conv_dict                                                               

#printing converted 2d dict
#cnverted_dict = conv_to_2d_dict(matrix, labels)
#print(cnverted_dict)

def finding_min_distance(conv_dict):
    minimum_dist = float('inf') #initializing to infinity was suggested by Co-pilot after I was struggling with setting it to first value 
    minimum_pair = None
    for label1 in conv_dict:
        for label2 in conv_dict[label1]:
            if label1 != label2:
                if conv_dict[label1][label2] < minimum_dist:
                    minimum_dist = conv_dict[label1][label2]
                    minimum_pair = (label1, label2)
    return minimum_pair

#printing minimum distance pair
#conv_dict = conv_to_2d_dict(matrix, labels)
#minimumr = finding_min_distance(conv_dict)
#print("minimum distance", minimumr)

def updating_2d_dict(conv_dict, clster1, clster2):
    new_clster = f"({clster1},{clster2})"
    new_distnces = {}
    
    # Calculating  distances for the new cluster using WPGMA
    for label in conv_dict:
        if label != clster1 and label != clster2:
            new_distnce = (conv_dict[clster1][label] + conv_dict[clster2][label]) / 2
            new_distnces[label] = new_distnce
            conv_dict[label][new_clster] = new_distnce

    conv_dict[new_clster] = new_distnces

    # Remove old clusters so that they are not used again, simlar to the suggestion given in the project instruction file.
    del conv_dict[clster1]
    del conv_dict[clster2]
    for label in conv_dict:
        if clster1 in conv_dict[label]:
            del conv_dict[label][clster1]
        if clster2 in conv_dict[label]:
            del conv_dict[label][clster2]

    return conv_dict

#print updated 2d dictionary
#conv_dict = conv_to_2d_dict(matrix, labels)
#updated_dict = updating_2d_dict(conv_dict, labels[0], labels[1]) 
#print("updated dict:", updated_dict)

def main_function(matrix, labels):

    input_validation(matrix, labels)


    #  suggested by Gemini to include scenario where only one element is provided
    if len(matrix) == 1:
        return labels[0]
    
    conv_dict = conv_to_2d_dict(matrix, labels)
    clusters = labels[:]

    
    # Perform clustering until one cluster remains
    while len(conv_dict) > 1:
        # to find the two closest clusterd
        cluster1, cluster2 = finding_min_distance(conv_dict)
        
        # Create a new cluster by merging the two closest clusters
        merg_cluster = f"({cluster1},{cluster2})"
        
        # Updating the dictionary 
        updating_2d_dict(conv_dict, cluster1, cluster2)
        
    # the root of the tree
    return list(conv_dict.keys())[0]



#printing final tree
final_tree = main_function(matrix, labels)
print("Final tree:", final_tree)
  
