# https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not/0

import collections

T = int(input())
for t in range(0, T):
    s1 = input()
    s2 = input()
    c1 = collections.deque(s1)
    c2 = collections.deque(s1)
    match = 0
    for i in range(0, len(c1)):
        c1.rotate(1)
        r1 = ''.join(c1)
        c2.rotate(-1)
        r2 = ''.join(c2)
        # print(r1, r2)
        if r1 == s2 or r2 == s2:
            print(1)
            match = 1
            break

        if match == 1:
            break
        else:
            continue

    if match == 0:
        print(0)
