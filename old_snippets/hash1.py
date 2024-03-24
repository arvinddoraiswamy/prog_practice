T = int(input())
for t in range(0, T):
    n = int(input())
    values = [int(x) for x in input().split(' ') if x != '']

    dict1 = {}
    for val in values:
        if val in dict1.keys():
            continue
        else:
            dict1[val] = 0

    l1 = []
    for key in dict1.keys():
        l1.append(key)
    l1.sort()

    match = 0
    for x in range(0, len(l1) - 1):
        #print(l1[x], l1[x+1])
        if (l1[x] + 1) != l1[x+1]:
            match = 0
            break
        else:
            match = 1

    if match == 0:
        print("No")
    elif match == 1:
        print("Yes")


