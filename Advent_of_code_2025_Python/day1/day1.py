"""
Author: Matthieu Borelle
Description: Solution to Day 1 of the Advent of Code 2025 challenge.
"""

import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data from a text file into a NumPy array."""

    with open(SCRIPT_DIR / file_name) as f:
        # for line in f:
        #     print(line.strip()[1:])
        lines = [line.strip() for line in f]
    return [line[0] for line in lines], [int(line[1:]) for line in lines]


# Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day1 challenge as an integer

    The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
    """
    rotation_dir_letter, rotation_clicks = load_data(data_file_name)

    #print(rotation_dir)
    #print(rotation_clicks)

    dial = 50
    counter_pointing_0 = 0

    rotation_dir =  [0 if letter=="R" else 1 for letter in rotation_dir_letter]
    for i in range(len(rotation_dir)): #run all the sequence of rotation
         # Left -> - -> (-1)^1
         # Right -> + -> (-1)^0

        dial = dial + (-1)**rotation_dir[i]*rotation_clicks[i]

        while dial > 99 or dial < 0:
            dial = dial + (-1)**(rotation_dir[i]+1)*100

        #print(dial)

        if dial == 0:
            counter_pointing_0 +=1


    return int(counter_pointing_0)


# Part 2
def part2_solution(data_file_name):
    """
    Returns the solution of the part2 of the day1 challenge as an integer

    The actual password is the number of times the dial is left pointing at 0 after any rotation or rotating over 0 in the sequence.
    """
    rotation_dir_letter, rotation_clicks = load_data(data_file_name)

    #print(rotation_dir)
    #print(rotation_clicks)
    
    dial_previous = 50
    #dial = 50
    counter_pointing_0_during_rotation = 0
    counter_pointing_0 = 0

    rotation_dir =  [0 if letter=="R" else 1 for letter in rotation_dir_letter]
    N_rotations = len(rotation_dir)

    for i in range(N_rotations): #run all the sequence of rotation
         # Left -> - -> (-1)^1
         # Right -> + -> (-1)^0

        dial = dial_previous + (-1)**(rotation_dir[i])*rotation_clicks[i]


        while dial > 99 or dial < 0:

            counter_pointing_0_during_rotation +=1

            dial = dial + (-1)**(rotation_dir[i]+1)*100

        # correction not to count another time 0 during Left rotation starting from 0
        if dial_previous==0 and rotation_dir[i]== 1:
            counter_pointing_0_during_rotation -= 1

        # correction not to count two times 0 during Right rotation
        if dial==0 and rotation_dir[i]== 0:
            counter_pointing_0_during_rotation -= 1    

        print(dial)
        print(counter_pointing_0_during_rotation)

        if dial == 0:  # last dial
            counter_pointing_0 +=1
        print(counter_pointing_0)

        dial_previous = dial

    return counter_pointing_0+counter_pointing_0_during_rotation


if __name__ == "__main__":
    print("Part 1 test:", part1_solution("day1_input_test.txt"))
    print("Part 1 solution:", part1_solution("day1_input.txt"))
    print("---")
    print("Part 2 test:", part2_solution("day1_input_test.txt"))
    print("Part 2 solution:", part2_solution("day1_input.txt"))

# 6475