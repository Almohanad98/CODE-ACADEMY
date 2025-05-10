#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  6 14:18:56 2025

@author: almohanadalfarei
"""




def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return 'NO'
    if v1 != v2:
        num = x2 - x1
        den = v1 - v2
        if den == 0 or num % den != 0 or num/den < 0:
            return 'NO'
        return 'YES'
    return 'NO'

inputs = [ (0, 3, 4, 2),   (2, 1, 1, 2),   (0, 2, 5, 3),  (0, 2, 0, 2)]

for x1, v1, x2, v2 in inputs:
    print(f'For x1 = {x1}, v1 = {v1}, x2 = {x2}, v2 = {v2}, the answer is: ' + kangaroo(x1, v1, x2, v2))

