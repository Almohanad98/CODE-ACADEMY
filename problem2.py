#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:04:55 2025

@author: almohanadalfarei
"""

row = int(input('Enter number of rows: '))
col = int(input('Enter number of columns: '))

if row == col:
    matrix = []
    print(f"Enter the values row by row (each row should have {col} values):")

    for i in range(row):
        row_values = input(f"Enter values for row {i+1}, separated by space: ").split()
        if len(row_values) != col:
            print("ERROR: Each row must have exactly", col, "values.")
            break
        matrix.append([int(x) for x in row_values])

    print("You entered this matrix:")
    for r in matrix:
        print(r)

    # Main diagonal
    main_diag = [matrix[i][i] for i in range(row)]
    main_sum = sum(main_diag)
    print("Main diagonal:", main_diag)
    print("Sum of main diagonal:", main_sum)

    reverse_diag = [matrix[i][col - 1 - i] for i in range(row)]
    reverse_sum = sum(reverse_diag)
    print("Reverse diagonal:", reverse_diag)
    print("Sum of reverse diagonal:", reverse_sum)

    # Difference and absolute value
    diff = abs(main_sum - reverse_sum)
    print("Absolute difference between diagonals:", diff)

else:
    print("ERROR: Number of rows and columns must be equal to form a square matrix.")
