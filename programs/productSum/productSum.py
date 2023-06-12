arr = [ 5,2, [7,-1] , 3, [6, [-13,8] ,4] ]
# output = 12

"""
approach

iterate through array:

for element 5:
    gsum = 5
    m = 1

for element 2:
    gsum = 7
    m = 1

for element [7,-1]:
    sum = 0
    m = 2

    for element 7
    sum = 7
    m = 2

    for element -1
    sum --> 7 + (-1) = 6
    m = 2

    sum * m --> 6 * 2 = 12

gsum + sum --> 7 + 12 = 19

repeat same for remaining elements.
"""


def productSum(inputArray, multiplier = 1):
    sum = 0
    for element in inputArray:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier

print(productSum(arr)) # 12

# time complexity: O(n)
# space complexity: O(d)