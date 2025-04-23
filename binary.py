

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

number= [2, 4, 6, 8, 10]
target = 8

result = binary_search(number, target)
print("Found at index:", result)  # Output: Found at index: 3
