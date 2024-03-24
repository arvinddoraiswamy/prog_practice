# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items/0
# https://www.coursera.org/lecture/algorithmic-toolbox/knapsack-with-repetitions-uYVzW


# TODO: NOT DONE. TROUBLE :/ :/ :/
"""
By capital W we denote the total capacity or the total weight of the knapsack. And our goal is to select the subset of
items where each item can be taken any number of times such that the total weight is at most capital W while the total
value is as large as possible.

1           - Tests
3 6         - N,W
1 1 1       - values
1 2 3       - weights
"""
import sys
T = int(input())
for t in range(0, T):
    N,W = [int(x) for x in input().split(' ')]
    val = [int(x) for x in input().split(' ')]
    weights = [int(x) for x in input().split(' ')]


    print(W, val, weights)
    print('-'*10)
    total = []
    iw = val
    iv = weights

    #Outer counter
    for w in range(0, N):
        for k in range(0, N):
            iw[k] = weights[w]
            iv[k] = val[w]
        print(weights)

        for i in range(0,N):
            if iw[i] == W:
                total.append(iv[i])
            elif iw[i] > W:
                continue
            else:
                print(i, iw[i], weights[i])
                iw[i] += weights[i]
                iv[i] += val[i]
                #print(i, iw[i], weights[i])

        sys.exit()