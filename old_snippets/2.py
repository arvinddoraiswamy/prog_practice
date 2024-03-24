"""
# https://practice.geeksforgeeks.org/problems/maximum-index/0
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j]

* 2 counters. both at 0
* if counters equal increment 1
* Check if a[i] <= a[j], if not increment j. if yes, store the index difference and increment j
* Repeat till end of array
*

Input
2
2
1 10
3
1 2 3
Output
1

# Works here but FAILS online due to taking too much time. My algorithm is shitty clearly :/. Need to figure a way
# to not do so many comparisons
"""

T = int(input())

for x in range(0, (2 * T), 2):
    N = int(input())
    num = input().split(' ')
    num = [int(x) for x in num if x != '']
    print("\n")
    max_val = 0
    for i in range(0, N):
        for j in range(0, N):
            if num[i] > num[j]:
                continue
            else:
                if (j-i) > max_val:
                    max_val = (j-i)

    print(max_val)