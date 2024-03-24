# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0

# Tried iterating through and finding max values per array but that didn't work
# Fix the largest values first by looking at largest differences works

import operator
T = int(input())
for t in range(0, T):
    N, X, Y = [int(x) for x in input().split(' ') if x != '']
    A = [int(x) for x in input().split(' ') if x != '']
    B = [int(x) for x in input().split(' ') if x != '']

    tip = 0
    count_A = 0
    count_B = 0
    diff = {}

    for i in range(0, N):
        if A[i] > B[i]:
            diff[str(i)+'_A'] = A[i] - B[i]
        elif A[i] < B[i]:
            diff[str(i)+'_B'] = B[i] - A[i]
        else:
            diff[str(i)+'_S'] = 0

    diff = sorted(diff.items(), key=operator.itemgetter(1), reverse=True)

    left = []
    equal = []

    for tup in diff:
        l = list(tup[0].split('_'))
        if l[1] == 'A' and count_A < X:
            count_A += 1
            tip += A[int(l[0])]
        elif l[1] == 'B' and count_B < Y:
            count_B += 1
            tip += B[int(l[0])]
        else:
            if l[1] == 'S':
                equal.append(tup)
            else:
                left.append(tup)

    for tup in left:
        l = list(tup[0].split('_'))
        if l[1] == 'A':
            count_B += 1
            tip += B[int(l[0])]
        elif l[1] == 'B':
            count_A += 1
            tip += A[int(l[0])]

    for tup in equal:
        l = list(tup[0].split('_'))
        if count_A < X:
            count_A += 1
            tip += A[int(l[0])]
        else:
            count_B += 1
            tip += B[int(l[0])]

    print(tip)