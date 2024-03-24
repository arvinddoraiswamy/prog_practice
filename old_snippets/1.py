# https://practice.geeksforgeeks.org/problems/remove-b-and-ac-from-a-given-string/0

"""
Input:

2
acbac
aababc

Output:
<BLANK LINE>
aaac

Notes: Iterate just once, this isn't recursive
"""

from re import sub

T = int(input())
lines = []
for i in range(0,T):
    lines.append(input())

for line in lines:
    line=sub(r'b|ac', '', line)
    print(line)