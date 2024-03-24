# https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints/0

T = int(input())

lengths = []

for i in range(0, T):
    x = int(input())
    if x>=1 and x<=1000:
        lengths.append(x)
    else:
        continue

for l in lengths:
    val = 0
    if l == 1:
        print(3)
    elif l == 2:
        print(8)
    elif l == 3:
        print(19)
    else:
        # Only a's
        val = 1

        # a and b
        val += l

        # a and c
        val += l

        # b and c
        val += l * (l-1)

        # a and 2c
        val += (l * (l-1)) / 2

        # a, b and 2c
        val += (l * (l-1) * (l-2)) / 2

        print(int(val))
