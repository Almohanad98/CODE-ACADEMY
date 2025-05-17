# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def is_qusai_always_with_friend(n, x, y, intervals):
    
    for point in range(x, y + 1):
        
        with_friend = False
        for a, b in intervals:
            if a <= point <= b:
                with_friend = True
                break
        
        if not with_friend:
            return "NO"
    
    return "YES"


n1 = 3
x1, y1 = 1, 20
intervals1 = [(1, 5), (4, 15), (10, 20)]
print(is_qusai_always_with_friend(n1, x1, y1, intervals1))  

n2 = 3
x2, y2 = 5, 12
intervals2 = [(8, 10), (10, 12), (7, 8)]
print(is_qusai_always_with_friend(n2, x2, y2, intervals2))  
