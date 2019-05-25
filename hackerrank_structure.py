#!/bin/python3

# Imports
import math
import os
import random
import re
import sys

#
# Instructions
#


def solution_function(a, b):
    # Write your code here
    return [a, b]


if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = solution_function(a, b)

    print('\n'.join(map(str, result)))
    print('\n')
