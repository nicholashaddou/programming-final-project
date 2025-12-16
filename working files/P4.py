import P3
import P2
import numpy as np
from collections import defaultdict

import P1
matrix = P3.ComputeDistMatrix()
#print("matrix from P3:", matrix)

labels = P1.get_label()

"""
Checking if the input for P4 is valid for the use case here.
"""
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
            
"""
Converting the numpy array matrix and the label list to a 2D dictionary for easy manipulation as stated by the project instruction.
"""
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

"""
The function below is used to find close pairs from the dictionary.
"""
def finding_min_distance(conv_dict):
    minimum_dist = float('inf') #initializing to infinity was suggested by Co-pilot after I was struggling with this for a while.
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

"""
merges two selected clusters and the dictionary is updated according to the WPGMA method mentioned.
The formula that is used here is given in the wikipedia page listed in the instruction file.
"""
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
    # Co-pilot used to help remove error in this sub-section.
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
        
        #  merging the two closest clusters
        merg_cluster = f"({cluster1},{cluster2})"
        
        # dictionary updating function called here
        updating_2d_dict(conv_dict, cluster1, cluster2)
        
    # the root of the tree suggested by Co-pilot to get the final output
    return list(conv_dict.keys())[0]



#printing final tree
final_tree = main_function(matrix, labels)
print("Final tree:", final_tree)
  
