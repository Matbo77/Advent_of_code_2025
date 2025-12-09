"""
Author: Matthieu Borelle
Description: Solution to Day 3 of the Advent of Code 2025 challenge.
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
    list_of_digit_lists = [[int(digit) for digit in line] for line in lines]    
    return list_of_digit_lists  



## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day3 challenge as an integer

    The total output joltage
    """
    #print(load_data(data_file_name))
    data = load_data(data_file_name)

    #print(data)    

    total_output_joltage = 0

    for i in range(0,len(data)): # for each line
        
        line_digits = data[i]
        
        max_list = [k for k, x in enumerate(line_digits[:-1]) if x == max(line_digits[:-1])] # remove the last digits for finding the max

        #print(max_list)

        list_candidate = [int(str(line_digits[k])+str(max(line_digits[k+1:]))) for k in max_list] 
        #[line_digits[k:k+1] for k in max_list]

        #print(list_candidate)

        max_output_joltage = max(list_candidate)

        total_output_joltage += max_output_joltage
   

    return total_output_joltage


## Part 2

# 003000000011
# 479103497921

# def look_for_max_digit_sequence(line_digits,sequence_length,candidate):
#     """ recursive search in the list from left to right """

#     #candidate = candidate
#     # legnth _left

#     if  len(line_digits)<=sequence_length:
#             candidate = line_digits
#             print(candidate)

#     elif len(line_digits)>sequence_length:
#         max_list = [k for k, x in enumerate(line_digits[:-sequence_length+1]) if x == max(line_digits[:-sequence_length+1])] 

#         print(max_list)

#         for k in max_list:
            
#             #line_digits[k+1:]
#             #sequence_length-1
#             #candidate
#             #candidate = int(str(line_digits[k])+str(look_for_max_digit_sequence(line_digits[k+1:],sequence_length-1,candidate)))
#             candidate = str(look_for_max_digit_sequence(line_digits[k+1:],sequence_length-1,candidate)) 
#             #print(candidate)
#     else:
#         print("Warning error")

#         # for k in max_list:

#     return candidate




def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day3 challenge as an integer

    The total output joltage (with 12 digits in each bank's joltage output)

    """
    #print(load_data(data_file_name))
    data = load_data(data_file_name)

    #print(data)    

    total_output_joltage = 0

    number_digits_joltage = 12 #  > 0
    

    for i in range(0,len(data)): # for each line
        
        line_digits = data[i]
        remaining_number_digits = number_digits_joltage

        dynamic_line_digits = line_digits[:len(line_digits)-remaining_number_digits+1]
        #max_list = [k for k, x in enumerate(dynamic_line_digits) if x == max(dynamic_line_digits)]
        max_index = dynamic_line_digits.index(max(dynamic_line_digits))
   
        candidate = line_digits[max_index]

        last_max_index  = max_index
        remaining_number_digits -= 1


        while (remaining_number_digits>0):


            dynamic_line_digits =  line_digits[last_max_index+1:len(line_digits)-remaining_number_digits+1]

            #max_list = [k for k, x in enumerate(dynamic_line_digits) if x == max(dynamic_line_digits)] # remove the last digits for finding the max
            max_index = dynamic_line_digits.index(max(dynamic_line_digits))

            candidate = 10*candidate + dynamic_line_digits[max_index]

            last_max_index +=  max_index + 1


            remaining_number_digits -= 1    

            # if remaining_number_digits == len(line_digits) - max_index:

            #     remaining_number_digits = 0
            #     candidate = int(str(candidate) + str(line_digits[max_index+1:]))


        max_output_joltage = candidate

        total_output_joltage += max_output_joltage
   

    return total_output_joltage
    



if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day3_input_test.txt"))   # 357
    #print("Part 1 test:", part1_solution("day3_input_test2.txt")) # 
    print("Part 1 solution:", part1_solution("day3_input.txt")) #  17074
    print("---")
    print("Part 2 test:", part2_solution("day3_input_test.txt"))  # 3121910778619
    print("Part 2 solution:", part2_solution("day3_input.txt")) # 169512729575727

