#!/bin/python3
import numpy as np


def find_closest_fibonacci_number(x):
    a = 1
    b = 1
    while (a + b) / 2 < x:
        a, b = b, a + b
    return a


def find_distance_closest_fibonacci_number(x):
    closest_fib = find_closest_fibonacci_number(x)
    return abs(closest_fib - x)


input_array = [1, 3, 4, 6, 7, 11, 17, 63, 101, 377, 467, 500, 1399]
closest_fibonacci_numbers = [1, 3, 3, 5, 8, 13, 13, 55, 89, 377, 377, 610, 1597]

test_result = [find_closest_fibonacci_number(x) for x in input_array]
print(np.array_equal(test_result, closest_fibonacci_numbers))
