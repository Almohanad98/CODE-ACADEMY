def birthday_chocolate(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    return count

# Example test cases from the board:
print(birthday_chocolate([2, 2, 1, 3, 2], 4, 2))  # Output: 2
print(birthday_chocolate([1, 1, 1, 1, 1], 3, 2))  # Output: 0
print(birthday_chocolate([1, 2, 1, 3, 2], 3, 2))  # Output: 2
print(birthday_chocolate([4], 4, 1))              # Output: 1
