sequence = [5,1,22,25,6,-1,8,10]
sub_sequence = [1,6,-1,10]

# solution 1 using for loop
# time complexity: O(N)
# space complexity: O(1)
def validateSubsequence(sequence, sub_sequence):
    seqIndx = 0
    for list_item in sequence:
        if seqIndx == len(sub_sequence):
            break
        if sub_sequence[seqIndx] == list_item:
            seqIndx+=1

    return seqIndx == len(sub_sequence)

validateSubsequence(sequence, sub_sequence) # True


# solution 2 using while loop
# time complexity: O(N)
# space complexity: O(1)
def validateSubsequence(sequence, sub_sequence):
    seqIndx = 0
    subseqIndx = 0

    while seqIndx < len(sequence) and subseqIndx < len(sub_sequence):
        if sequence[seqIndx] == sub_sequence[subseqIndx]:
            subseqIndx += 1
        seqIndx += 1

    return subseqIndx == len(sub_sequence)

validateSubsequence(sequence, sub_sequence) # True