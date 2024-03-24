# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list/0

T = int(input())

for t in range(0, T):
    even = []
    counter = []
    N = int(input())
    values = [int(x) for x in input().split(' ') if x != '']

    for i in range(0, N):
        if values[i] % 2 == 0:
            even.append(values[i])
            counter.append(i)

    for i in range(0, N):
        if i not in counter:
            even.append(values[i])
            counter.append(i)

    s1 = ''
    for x in even:
        s1 += str(x)
        s1 += ' '

    print(s1)
