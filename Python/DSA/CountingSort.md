# Explanation of Code with Comments:
# Define the Function:

def countingSort(arr):
Defines the countingSort function which takes a list arr as input.
Find the Maximum Value:

max_val = max(arr)
Finds the maximum value in the input array arr. This is used to determine the size of the count array.
Initialize the Count Array:

count = [0] * (max_val + 1)
Initializes the count array with zeros. The length of this array is max_val + 1 to accommodate all possible values in arr.
Count Occurrences of Each Value:

while len(arr) > 0:
Starts a loop that continues until arr is empty.
num = arr.pop(0)
Removes the first element from arr and stores it in num.
count[num] += 1
Increments the count of the value num in the count array.
Reconstruct the Sorted Array:

for i in range(len(count)):
Iterates over each index i in the count array.
while count[i] > 0:
Loops until the count of i is reduced to zero.
arr.append(i)
Appends the value i to arr.
count[i] -= 1
Decrements the count of i by 1.
Return the Sorted Array:

return arr
Returns the sorted arr.
Example Usage:

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
Defines an example unsorted array.
sortedArr = countingSort(unsortedArr)
Calls the countingSort function with unsortedArr and stores the result in sortedArr.
print("Sorted array:", sortedArr)
Prints the sorted array.