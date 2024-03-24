# https://practice.geeksforgeeks.org/problems/save-ironman/0

import re

T = int(input())
for i in range(0,T):
    line = re.sub('\W','', input().lower())

    if line == line[::-1]:
        print("YES")
    else:
        print("NO")