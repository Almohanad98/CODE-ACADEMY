def count_tallest_candles(candles):
    tallest = max(candles)
    return candles.count(tallest)

# Sample Inputs
inputs = [  [4, 4, 1, 3, 4],[3, 2, 1, 3],[1, 2, 3, 4, 5, 5],[7]]

# Apply the function and print results
for line in inputs:
    print(count_tallest_candles(line))


################
defind the list of statiment 
find the highest candels from the list
compering between the candeles
Try to find and count how many time the highst is repet
make for loop start from 0 
0 will chance if the highest number repet [ high= high+1]  
