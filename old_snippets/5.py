# https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary/0

import re

T = int(input())
for t in range(0, T):
    num = int(input())
    words = input().split(' ')
    words.sort()
    words.sort(key=len, reverse=True)
    junk_str = input()

    for word in words:
        t1 = list(word)
        pattern = ''
        for x in t1:
            pattern += '.*'
            pattern += x
        pattern += '.*'
        regex = re.compile(pattern)
        m = regex.search(junk_str)
        if m:
            print(word)
            break
        else:
            continue
