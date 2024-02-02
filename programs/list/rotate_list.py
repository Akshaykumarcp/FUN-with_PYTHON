"""
left (counter clock wise) rotate list/array by 1

example:

list = [1, 2, 3, 4, 5]

POST ROTATE

[2, 3, 4, 5, 1]

"""

lst = [1,2,3,4,5]

def rotateByOne(original_lst):

    temp = original_lst[0]

    for i in range(1, len(lst)):

        original_lst[i-1] = original_lst[i]

    original_lst[len(original_lst)-1] = temp

    return original_lst

print(lst) # [1, 2, 3, 4, 5]
print(rotateByOne(lst)) # [2, 3, 4, 5, 1]

"""
Rotate by k times

OPTMIZATIOM (avoiding unecessary rotations)
    Observation 1: k % len(list) --> for k in large number - counter clockwise rotation
    Observation 2: -k + len(list) --> for k is less than 0 --> clockwise rotation

reuse some lines of above code
"""

lst = [1,2,3,4,5]

def rotateByOne(lst):
    temp = lst[0]

    for i in range(1, len(lst)):
        lst[i-1] = lst[i]

    lst[len(lst)-1] = temp

def rotateByNtimes(lst, k):
    # observation 1
    k = k % len(lst)

    # observation 2
    if k < 0:
        k = -k + len(lst)

    for i in range(1, k+1):
        rotateByOne(lst)

# TEST FOR K=1
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 1)
print(lst) # [2, 3, 4, 5, 1]

# TEST FOR K=2
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 2)
print(lst) # [3, 4, 5, 1, 2]

# TEST FOR K=3
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 3)
print(lst) # [4, 5, 1, 2, 3]

# TEST FOR K=4
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 4)
print(lst) # [5, 1, 2, 3, 4]

# TEST FOR K=5 (observation 1)
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 5)
print(lst) # [1, 2, 3, 4, 5]

# TEST FOR K=7 (observation 1)
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, 7)
print(lst) # [3, 4, 5, 1, 2]

# TEST FOR K=-1 (observation 2)
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, -1)
print(lst) # [3, 4, 5, 1, 2]

# TEST FOR K=-4 (observation 2)
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
rotateByNtimes(lst, -4)
print(lst) # [2, 3, 4, 5, 1]

"""
time complexity = O(k*n)

rotateByNtimes runs for k times
rotateByOne runs for n times

can we make it better?
YES

For rotating an list by n times there is an existing algo present (reverse an list).

"""

lst = [1,2,3,4,5]

def reverse(lst, start, end):

    while(start<end):
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start+=1
        end-=1

def rotate(lst, k):
    # observation 1
    k = k % len(lst)

    # observation 2
    if k < 0:
        k = -k + len(lst)

    reverse(lst, 0, k-1)
    reverse(lst, k, len(lst)-1)
    reverse(lst, 0, len(lst)-1)

# TEST FOR K=1
print(lst) # [1, 2, 3, 4, 5]
rotate(lst, 1)
print(lst) # [2, 3, 4, 5, 1]


# TEST FOR K=2
lst = [1,2,3,4,5]
print(lst) # [1, 2, 3, 4, 5]
rotate(lst, 2)
print(lst) # [3, 4, 5, 1, 2]

"""
Time complexity is O(n)

Three recursive calls, runs on n elements. n + n + n = 3n. 3 removed due to constant. Remaining is n --> O(n)

 """