"""
Author: Matthieu Borelle
Description: Solution to Day 2 of the Advent of Code 2025 challenge.
"""

import numpy as np
import math
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data from a text file into a NumPy array."""
    with open(SCRIPT_DIR / file_name) as f:
        data = f.read().split(',')
    return data



## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day2 challenge as an integer

    The sum of all invalid IDs
    """
    #print(load_data(data_file_name))
    data = load_data(data_file_name)

    #print(data)    

    list_begin_id = []
    list_end_id = []

    list_invalid_IDs = []

    # list_begin_id, list_end_id = zip(*[map(int, pair.split('-')) for pair in data]) # alternative compact form

    for i in range(len(data)):


        begin_id,end_id = data[i].split("-")

        list_begin_id.append(int(begin_id))
        list_end_id.append(int(end_id))
        
        
        #check_number = min(max(int(begin_id),10**((2*len(begin_id)+1)//2)),int(end_id))

        check_number = int(begin_id)


        if len(begin_id)%2 == 1: # odd number
            
            corrected_begin_id = str(10**(len(begin_id))) # str as begin_id

        else:
            
            corrected_begin_id = begin_id

        #print(corrected_begin_id)

        #if len(begin_id) == len(end_id) and len(begin_id)%2 == 1:
        # odd number can't be invalid IDs

        if len(corrected_begin_id)%2 == 0 : # even number of digits
            
            even_number = int(len(corrected_begin_id)/2)
            repeated_number = corrected_begin_id[0:even_number]
            #math.log10(begin_id)
            check_number = int(repeated_number+repeated_number)

            while check_number<= int(end_id): # check_number>= int(begin_id) and 
                
                if check_number>= int(begin_id):
                    list_invalid_IDs.append(check_number)

                repeated_number = str(int(repeated_number)+1)    
                check_number = int(repeated_number+repeated_number)


    #print(list_invalid_IDs)

    if list_invalid_IDs:
        sum_false_IDs = sum(list_invalid_IDs)
    else:
        sum_false_IDs = 0

    return int(sum_false_IDs)


def is_invalid_ID(x):
    s = str(x)
    # Check all possible repeated sequences

    return len(s)%2==0 and s[:len(s)//2] == s[len(s)//2:]


def part1_solution2(data_file_name):
    """
    Returns the solution of the part1 of the day2 challenge as an integer,
    alternative method
    The sum of all invalid IDs
    """
    data = load_data(data_file_name)
    total = 0
    list_invalid_IDs = []
    for pair in data:
        begin_id, end_id = map(int, pair.split('-'))
        for num in range(begin_id, end_id + 1):
            if is_invalid_ID(num):
                #print("invalid ID: ",num)
                total += num
                list_invalid_IDs.append(num)

    #print(list_invalid_IDs)

    return total



## Part 2
def is_invalid_ID_new_rules(x):
    s = str(x)

    ok = False

    i_mult = 1 # bounded by len(s)//2

    # Check all possible repeated sequences according to the new rules
    #for k in range(1,len(s)+1):
    k = 1

    while(i_mult <= len(s)//2 and k<len(s)):

        if s[:i_mult] == s[k:k+i_mult]:
            ok = True
            k = k + i_mult
        else: 
            ok = False
            i_mult = k + 1  # + 1
            k = i_mult

    if ok:
        return True
    else:
        return False


def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day2 challenge as an integer

    The sum of invalid IDs (with the new rules), brute force
    """
    data = load_data(data_file_name)
    total = 0
    list_invalid_IDs_new = []
    for pair in data:
        begin_id, end_id = map(int, pair.split('-'))
        for num in range(begin_id, end_id + 1):
            if is_invalid_ID_new_rules(num):
                total += num
                list_invalid_IDs_new.append(num)

        #print(list_invalid_IDs_new)
    #print(total)
    return total




if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day2_input_test.txt"))   # 1227775554
    #print("Part 1 test:", part1_solution2("day2_input_test2.txt")) # 26607752633
    print("Part 1 solution:", part1_solution("day2_input.txt")) # 54234399924
    print("Part 1 solution 2:", part1_solution2("day2_input.txt")) # 54234399924 
    print("---")
    print("Part 2 test:", part2_solution("day2_input_test.txt"))  # 4174379265 
    print("Part 2 solution:", part2_solution("day2_input.txt")) # 70187097315

