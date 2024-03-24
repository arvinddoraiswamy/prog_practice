# https://practice.geeksforgeeks.org/problems/four-elements/0

import itertools
T = int(input())
for t in range(0, T):
    match = 0
    N = int(input())
    values = [int(x) for x in input().split(' ') if x != '']
    X = int(input())

    l1 = itertools.combinations(values, 4)

    for x in l1:
        if sum(x) == X:
            match = 1
            break
        else:
            continue

    if match == 1:
        print(1)
    else:
        print(0)
