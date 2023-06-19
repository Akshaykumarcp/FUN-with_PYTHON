# time complexity: O(nLog(n) + mLog(m))
# space complexity: O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    smallestPair = []
    smallest = float("inf")
    current = float("inf")
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        if arrayOne[idxOne] < arrayTwo[idxTwo]:
            current = arrayTwo[idxTwo] - arrayOne[idxOne]
            idxOne += 1
        elif arrayTwo[idxTwo] < arrayOne[idxOne]:
            current = arrayOne[idxOne] - arrayTwo[idxTwo]
            idxTwo += 1
        else:
            return [arrayOne[idxOne],arrayTwo[idxTwo]]
        if smallest  > current:
            smallest = current
            smallestPair = [arrayOne[idxOne],arrayTwo[idxTwo-1]]
    return smallestPair, smallest

smallPair, small = smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]) # [28,26] 2