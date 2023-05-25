distinct_array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
answer = [11,-1]

# solution 1 (least efficient) ---------------------
# time complexity: O(n^2)
# space complexity: O(1)
def twoNumberSum(distinct_array):
    for i in range(len(distinct_array)-1):
        for j in range(i+1,len(distinct_array)-1):
            print(distinct_array[i], distinct_array[j+1], distinct_array[i] + distinct_array[j+1])
            if distinct_array[i] + distinct_array[j+1] == targetSum:
                return [distinct_array[i],distinct_array[j+1]]
    return []

print(twoNumberSum(distinct_array))
"""
3 -4 -1
3 8 11
3 11 14
3 1 4
3 -1 2
3 6 9
5 8 13
5 11 16
5 1 6
5 -1 4
5 6 11
-4 11 7
-4 1 -3
-4 -1 -5
-4 6 2
8 1 9
8 -1 7
8 6 14
11 -1 10
[11, -1]
 """

# solution 2 (efficient) --------------------
# time complexity: O(N)
# space complexity: O(N)

seen_numbers = {}

def twoNumberSum(distinct_array):

    for i in range(len(distinct_array)-1):
        y = targetSum - distinct_array[i]
        print(f"Target: {targetSum}, Current Number: {distinct_array[i]}, y: {y}")
        if y not in seen_numbers:
            seen_numbers[distinct_array[i]] = True
            print(seen_numbers)
        else:
            return [y, distinct_array[i]]

    return []

print(twoNumberSum(distinct_array))
"""
Target: 10, Current Number: 3, y: 7
{3: True}
Target: 10, Current Number: 5, y: 5
{3: True, 5: True}
Target: 10, Current Number: -4, y: 14
{3: True, 5: True, -4: True}
Target: 10, Current Number: 8, y: 2
{3: True, 5: True, -4: True, 8: True}
Target: 10, Current Number: 11, y: -1
{3: True, 5: True, -4: True, 8: True, 11: True}
Target: 10, Current Number: 1, y: 9
{3: True, 5: True, -4: True, 8: True, 11: True, 1: True}
Target: 10, Current Number: -1, y: 11
[11, -1] """


# solution 3 (most efficient) ------------------
# time complexity: O(N)
# space complexity: O(1)

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

# quick sort time complexity: O(n log(n))
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

distinct_array_sorted = quick_sort(distinct_array)
print(distinct_array_sorted)
# [-4, -1, 1, 3, 5, 6, 8, 11]

def twoNumberSum(distinct_array_sorted):

    left = 0
    right = len(distinct_array_sorted) - 1
    while left < right:
        print(f"left: {left}. right: {right}")
        currentSum = distinct_array_sorted[left] + distinct_array_sorted[right]
        print(f"current sum: {currentSum}. left array value: {distinct_array_sorted[left]}. right array value: {distinct_array_sorted[right]}")
        if currentSum == targetSum:
            return [distinct_array_sorted[right],distinct_array_sorted[left]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

print(twoNumberSum(distinct_array_sorted))
"""
left: 0. right: 7
current sum: 7. left array value: -4. right array value: 11
left: 1. right: 7
current sum: 10. left array value: -1. right array value: 11
[11, -1] """