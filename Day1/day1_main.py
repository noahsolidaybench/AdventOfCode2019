# Copyright 2019 Noah Soliday Bench
# Made for Advent of Code 2019

import os

SHOW_LOGS = True
script_path = os.path.dirname(os.path.abspath(__file__))

data_path = 'day1_input.txt'
fuel_requirement_sum = 0

with open(os.path.join(script_path, data_path)) as weightInput:
    module_weights = weightInput.readlines()

    for weight in module_weights:
        fuel_for_module = int(int(weight) / 3) - 2
        while fuel_for_module > 0:
            fuel_requirement_sum += fuel_for_module
            fuel_for_module = int(int(fuel_for_module) / 3) - 2

print(str.format('\n\nFinal weight:\n{0}', fuel_requirement_sum))
