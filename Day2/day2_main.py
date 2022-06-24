# Copyright 2019 Noah Soliday Bench
# Made for Advent of Code 2019

import os

SHOW_LOGS = True
DATA_PATH = 'day2_input.txt'
script_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_path, DATA_PATH)) as day2_input:
    input_array = day2_input.readline().split(',')
    input_array = list(map(int, input_array))

    input_array[1] = 59
    input_array[2] = 36

    i = 0
    while i < len(input_array):
        if input_array[i] == 1:
            input_array[input_array[i+3]] = input_array[input_array[i+1]] + input_array[input_array[i+2]]
        elif input_array[i] == 2:
            input_array[input_array[i+3]] = input_array[input_array[i+1]] * input_array[input_array[i+2]]
        elif input_array[i] == 99:
            break

        i += 4

    print(input_array[0])
