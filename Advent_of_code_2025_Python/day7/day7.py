"""
Author: Matthieu Borelle
Description: Solution to Day 7 of the Advent of Code 2025 challenge.
"""

import numpy as np
import math
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data from a text file into arrays."""
    with open(SCRIPT_DIR / file_name) as f:

        lines = [line.strip('\n') for line in f]
            # # Split each line into a list of integers   

    return lines



## Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day7 challenge as an integer

    The number of tachion beam splitted
    """
    lines = load_data(data_file_name)

    #print(lines)   

    n_c = len(lines[0])
    n_l = len(lines)

    sum_beam_splitted = 0

    # # detect tachyon beam enters (S)
    
    list_beam = [[] for i in range(n_l)] #[]

    for j in range(0,n_c-1):

        if lines[0][j] == "S":
             list_beam[0].append(j)

    #print(list_beam)


    for i in range(1,n_l):

        for elt in list_beam[i-1]:
            
            if lines[i][elt] == "^": # beam splitting
                
                sum_beam_splitted += 1

                if elt>= 1:
                    list_beam[i].append(elt-1)
                if elt<n_c:
                    list_beam[i].append(elt+1)


            else:   # vertical beam propagation

                list_beam[i].append(elt)


            # remove plural number redundancies
            list_beam[i] = list(dict.fromkeys(list_beam[i]))

  
    #print("Dim l*c: ",n_l,n_c)
    #print(list_beam)

    return sum_beam_splitted


# def display the beam propagation(lines,list_beam): 

## Part 2


def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day7 challenge as an integer

    The number of tachion beam timelines
    """
    lines = load_data(data_file_name)

    #print(lines)   

    n_c = len(lines[0])
    n_l = len(lines)


    # # detect tachyon beam enters (S)
    
    list_number_beams = [[0]*n_c for i in range(n_l)] #[]

    for j in range(0,n_c-1):

        if lines[0][j] == "S":
             list_number_beams[0][j] += 1

    #print(list_number_beams)


    for i in range(1,n_l):

        #print(i,"/",n_l)
        for elt in range(n_c):
            
            if list_number_beams[i-1][elt] > 0:
            
                if lines[i][elt] == "^": # beam splitting
                    

                    if elt>=1:
                        list_number_beams[i][elt-1] += list_number_beams[i-1][elt] 
                    if elt<n_c:
                        list_number_beams[i][elt+1] += list_number_beams[i-1][elt]


                else:   # vertical beam propagation

                    list_number_beams[i][elt] += list_number_beams[i-1][elt]


            # remove plural number redundancies
            #list_beam[i] = list(dict.fromkeys(list_beam[i]))

    #print("Dim l*c: ",n_l,n_c)
    #print(list_number_beams[n_l-1])

    number_timelines = sum(list_number_beams[n_l-1])

    return number_timelines
    


if __name__ == "__main__": 

    print("Part 1 test:", part1_solution("day7_input_test.txt"))   # 21
    # #print("Part 1 test:", part1_solution("day7_input_test2.txt")) # 
    print("Part 1 solution:", part1_solution("day7_input.txt")) # 1594
    print("---")
    print("Part 2 test:", part2_solution("day7_input_test.txt"))  # 40
    #print("Part 2 test:", part2_solution("day7_input_test2.txt")) 
    print("Part 2 solution:", part2_solution("day7_input.txt")) # 15650261281478
    

