"""
Author: Matthieu Borelle
Description: Solution to Day 5 of the Advent of Code 2025 challenge.
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
    # # Split each line into a list of integers

    # # 1 : @,  0 : .    
        
        #print(lines) 

    return lines 


## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day5 challenge as an integer

    The number of fresh available ingredient IDs
    """
    lines = load_data(data_file_name)

    #print(lines)    

    space = 0
    available_ingredients = []
    min_max_ranges = []
    for line in lines:

        if line == "":
            space = 1
        elif space == 0:
            min_max_ranges.append(list(map(int,line.split('-'))))  
        else:
            available_ingredients.append(int(line[:]))

    #min_max = [line.split('-') for line in lines]
    #[min_max.append(line.split('-')) if not space else available_ingredients.append(line) for line in lines if line != "" or (line == "" and not (space := 1))]

    #print(min_max_ranges)
    #print(available_ingredients)

    fresh_available_ingredient = 0

    for x in available_ingredients:
       
        i=0
        fresh_ingredient = False

        while i<len(min_max_ranges) and not fresh_ingredient:
            
            #print(min_max[i][0]<=x<=min_max[i][1])
            #print(x in range(min_max[i][0]),min_max[i][1]+1) 

            if min_max_ranges[i][0]<=x<=min_max_ranges[i][1]:
                fresh_available_ingredient+=1
                fresh_ingredient = True

                #print(x) 

            i+=1



    return fresh_available_ingredient


## Part 2


def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day3 challenge as an integer

    The number of fresh ingredient IDs

    """
    lines = load_data(data_file_name)

    #print(lines)    

    space = 0
    available_ingredients = []
    min_max_ranges = []
    for line in lines:

        if line == "":
            break
        else:
            min_max_ranges.append(list(map(int,line.split('-'))))  

            
    #min_max = [line.split('-') for line in lines]
    #[min_max.append(line.split('-')) if not space else available_ingredients.append(line) for line in lines if line != "" or (line == "" and not (space := 1))]

    #print(min_max_ranges)

    min_max_ranges.sort(key=lambda x: x[0])

    #print(min_max_ranges)


    i = 0

    fresh_ingredient = 0

    while i<len(min_max_ranges): 

        
        j = 1
        while (i+j<len(min_max_ranges)) and min_max_ranges[i][1] >= min_max_ranges[i+j][0]:

            min_max_ranges[i+j][0] = min_max_ranges[i][1]+1

            if min_max_ranges[i][1] >= min_max_ranges[i+j][1]: 
                #useless range (encapsulated in another) thus we remove it
                 min_max_ranges.pop(i+j)
                 j = j-1

            j += 1

        # add the range of numbers    
        fresh_ingredient +=  min_max_ranges[i][1] - min_max_ranges[i][0] + 1

        i+=1

    return fresh_ingredient
    



if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day5_input_test.txt"))   # 3
    print("Part 1 solution:", part1_solution("day5_input.txt")) # 520
    print("---")
    print("Part 2 test:", part2_solution("day5_input_test.txt"))  # 14
    #print("Part 2 test:", part2_solution("day5_input_test2.txt")) # 14
    print("Part 2 solution:", part2_solution("day5_input.txt")) # 347338785050515

