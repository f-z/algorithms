# -*- coding: utf-8 -*-
"""
Created on Sun May  2 21:03:26 2021

@author: filzo
"""

def count_pronic_in_range(A, B):
    count = 0
    for n in range(A, B + 1):
        if is_pronic(n):
            count += 1
    return count

def is_pronic(n) :
    x = int(math.sqrt(n))
    if (x * (x + 1) == n):
        return True
    else:
        return False
