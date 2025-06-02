
def is_definitely_lying(arr):
    n = len(arr)
    arr = [x - 1 for x in arr]
    
    for i in range(n):
        j = arr[i]
        if arr[j] == i:
            return "Definitely lying"
    return "Not Definitely lying"

# Test Cases
inputs = [
    [3, 1, 1],
    [1, 3, 1],
    [2, 2, 2],
    [2, 2, 3],
    [3, 2, 3]
]

for case in inputs:
    print(f"Input: {case} → Output: {is_definitely_lying(case)}")
