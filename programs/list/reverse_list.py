lst = [2, 4, 6, 8, 10, 12, 14]

i = 0
j = len(lst)-1

while (i<=j): # termination conditon

    # swap i and j pointers
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

    # increment i and j
    i+=1
    j-=1

print(lst) # [14, 12, 10, 8, 6, 4, 2]