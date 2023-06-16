# Binary Search

input = [0,1,21,33,45,45,61,71,72,73]

# return index of the target search

# recursive way
# O(log(n)) time complexity
# O(lon(n)) space complexity
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    # base case
    if left > right:
        return -1
    middle = (left + right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)

print(binarySearch(input, 33)) # 3
print(binarySearch(input, 102)) # -1

# iteratively
# time complexity: O(log(n))
# space complexity: O(1)
def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right)//2
        if array[middle] == target:
            return middle
        elif target > array[middle] :
            left = middle + 1
        else:
            right = middle - 1
    return -1

print(binarySearch(input, 33)) # 3
print(binarySearch(input, 110)) # -1
