"""
Author: Matthieu Borelle
Description: Solution to Day 6 of the Advent of Code 2025 challenge.
"""

import numpy as np
import math
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent

def load_data(file_name,strip_split_option):
    """Load data from a text file into arrays."""
    with open(SCRIPT_DIR / file_name) as f:

        if strip_split_option:
            lines = [line.strip().split() for line in f]
            # # Split each line into a list of integers   
        else:
            lines = [line.strip('\n') for line in f]

        n_c = len(lines[0])

        columns = [[] for i in range(n_c)]

        for line in lines:
            
            for i in range(n_c):    
                
                columns[i].append(line[i]) 
        

    return lines,columns



## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day6 challenge as an integer

    The sum of the operations
    """
    lines,columns = load_data(data_file_name,True)

    #print(columns) 
    #print(lines)   

    n_c = len(columns)
    n_l = len(lines)


    results_operations = list(map(int,lines[0][:])) 

  
    for i in range(0,n_c):

        if columns[i][n_l-1] == "+":

            results_operations[i] = sum(list(map(int,columns[i][:-1]))) 

        elif columns[i][n_l-1] == "*":

            results_operations[i] = np.prod(list(map(int,columns[i][:-1]))) 
            #list_number[] =

        #print(results_operations)

    # #print("Dim: ",n_l,n_c)

    # print(list_symbol)

    sum_operations = sum(results_operations)



    return sum_operations


## Part 2


def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day6 challenge as an integer

    The sum of the operations
    """
    lines_split,columns_split = load_data(data_file_name,True)
    # list of int
    # print(columns_split) 
    #print(lines_split)  

    lines,columns = load_data(data_file_name,False)
    # list of string
    # print(columns) 
    #print(lines)  

    n_l = len(lines)-1

    i = 0
    i_split = 0

    list_number = []

    sum_results_operations = 0

    while i<len(lines[0]):
        
        operator = lines_split[n_l][i_split]

        # read the column and construct the number 
        number = "".join(columns[i][:len(lines_split)-1])  

        if number.strip() != "":
            
            number_int = int(number)

            #print(number_int)

            list_number.append(number_int)

        elif number.strip() == "":
            
            if operator == "+":
                results_operations = sum(list_number)

            elif operator == "*":

                results_operations = np.prod(list_number)

            #print(results_operations)    

            sum_results_operations += results_operations

            list_number = []
            i_split +=1

        i+=1
    
    if i==len(lines[0]):
        if operator == "+":
            results_operations = sum(list_number)

        elif operator == "*":

            results_operations = np.prod(list_number)

        #print(results_operations)    

        sum_results_operations += results_operations

    return sum_results_operations
    
# # .replace(" ", "")



if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day6_input_test.txt"))   # 4277556
    # #print("Part 1 test:", part1_solution("day6_input_test2.txt")) # 
    print("Part 1 solution:", part1_solution("day6_input.txt")) # 7098065460541
    print("---")
    print("Part 2 test:", part2_solution("day6_input_test.txt"))  # 3263827
    print("Part 2 solution:", part2_solution("day6_input.txt")) # 13807151830618


