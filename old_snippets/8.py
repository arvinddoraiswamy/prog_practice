# https://practice.geeksforgeeks.org/problems/finding-the-numbers/0

T = int(input())
from collections import Counter

for t in range(0, T):
    final = []
    N = int(input())
    numbers = [int(x) for x in input().split(' ') if x != '']

    counter = dict(Counter(numbers))
    for k,v in counter.items():
        if (v % 2) == 1:
            final.append(k)
    final = [str(x) for x in sorted(final)]
    print(' '.join(final))