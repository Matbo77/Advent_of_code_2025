"""
Author: Matthieu Borelle
Description: Solution to Day 4 of the Advent of Code 2025 challenge.
"""

import numpy as np
import math
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data from a text file into a NumPy array."""
    with open(SCRIPT_DIR / file_name) as f:
        lines = [line.strip() for line in f]
    # Split each line into a list of integers
    list_of_digit_lists = [[1 if x =="@" else 0 for x in line] for line in lines]
    # 1 : @,  0 : .    
    return list_of_digit_lists  



## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day4 challenge as an integer

    The number of rolls of paper that can be accessed by a forklift
    """
    data = load_data(data_file_name)

    #print(data)    

    
    n_l = len(data)
    n_c = len(data[0])

    #print("Dim: ",n_l,n_c)


    max_neighbor_rolls = 3

    paper_rolls_accessed = 0


    for l in range(0,n_l):

        #rolls_of_papers = data[l].index(1) 
        rolls_of_papers = [i for i, elt in enumerate(data[l]) if elt == 1] 

        for c in rolls_of_papers:

            j_l = -1

            neighbor_rolls = -1 # to take into account the roll for j_l and j_c = 0

            while j_l<2 and neighbor_rolls<=max_neighbor_rolls: #min(), max()
                
                j_c = -1

                while j_c<2 and neighbor_rolls<=max_neighbor_rolls:
                        
                        if 0<=l+j_l<=n_l-1 and 0<=c+j_c<=n_c-1:

                            if data[l+j_l][c+j_c] == 1:
                                neighbor_rolls += 1

                        j_c += 1

                j_l += 1

            if neighbor_rolls<=max_neighbor_rolls:

                paper_rolls_accessed+= 1
                #print(l,c)
   

    return paper_rolls_accessed


## Part 2

def is_accessible(data,l,c,max_neighbor_rolls):
    """ Check if a roll is accessible  """

    n_l = len(data)
    n_c = len(data[0])

    j_l = -1

    neighbor_rolls = -1 # to take into account the roll for j_l and j_c = 0

    while j_l<2 and neighbor_rolls<=max_neighbor_rolls: #min(), max()
        
        j_c = -1

        while j_c<2 and neighbor_rolls<=max_neighbor_rolls:
                
                if 0<=l+j_l<=n_l-1 and 0<=c+j_c<=n_c-1:

                    if data[l+j_l][c+j_c] == 1:
                        neighbor_rolls += 1

                j_c += 1

        j_l += 1

    if neighbor_rolls<=max_neighbor_rolls:
        return True
    else:
        return False


def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day3 challenge as an integer

    The number of rolls of paper that can be accessed by a forklift (with the iterative procedure)

    """
    data = load_data(data_file_name)

    #print(data)    

    
    n_l = len(data)
    n_c = len(data[0])

    #print("Dim: ",n_l,n_c)


    max_neighbor_rolls = 3

    paper_rolls_accessed = 0

    #for i in range(0,len(data)): # for each line
    l=0
    
    accessible_roll_removed = False

    while l<n_l:

        #rolls_of_papers = data[l].index(1) 
        rolls_of_papers = [i for i, elt in enumerate(data[l]) if elt == 1] 


        for c in rolls_of_papers:   
        
        #print(c)

            if is_accessible(data,l,c,max_neighbor_rolls):
                data[l][c] = 0
                #print(l,":",data[l])
                paper_rolls_accessed +=1
                accessible_roll_removed = True
                #l=-1
                #break
            
        if accessible_roll_removed:
            l=-1
            accessible_roll_removed = False
                  

        l+=1

    return paper_rolls_accessed
    



if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day4_input_test.txt"))   # 13
    # #print("Part 1 test:", part1_solution("day4_input_test2.txt")) # 
    print("Part 1 solution:", part1_solution("day4_input.txt")) # 1428
    print("---")
    print("Part 2 test:", part2_solution("day4_input_test.txt"))  # 43
    print("Part 2 solution:", part2_solution("day4_input.txt")) # 8936

