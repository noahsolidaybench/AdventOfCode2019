# Copyright 2019 Noah Soliday Bench
# Made for Advent of Code 2019

import os
import itertools

SHOW_LOGS = True
DATA_PATH = 'day2_input.txt'
script_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_path, DATA_PATH)) as day2_input:
    input_array = day2_input.readline().split(',')
    input_array = list(map(int, input_array))
    successes = 0

    for a, b in itertools.product(range(100), range(100)):
        new_array = input_array
        new_array[1] = a
        new_array[2] = b

        if SHOW_LOGS:
            print("A: {0}  B: {1}".format(a, b))

        i = 0
        while i < len(new_array):

            if new_array[i] == 1:
                new_array[new_array[i+3]] = new_array[new_array[i+1]] + new_array[new_array[i+2]]
                i += 3
            elif new_array[i] == 2:
                new_array[new_array[i+3]] = new_array[new_array[i+1]] * new_array[new_array[i+2]]
                i += 3
            elif new_array[i] == 99:
                successes +=1
                if new_array[0] == 19690720:
                    print("Correct value: {0}".format(100 * a + b))
                break

            i += 1

    print("\nSuccesses: {0}".format(successes))
