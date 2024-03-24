# https://practice.geeksforgeeks.org/problems/meta-strings/0

T = int(input())

for t in range(0, T):
    count = 0
    tuple_count = -1
    diff = []
    s1 = input()
    s2 = input()

    if s1 == s2:
        print(0)
    else:
        for x in zip(s1, s2):
            tuple_count += 1
            if x[0] != x[1]:
                diff.append(tuple_count)
                count += 1
            else:
                continue

        if count == 2:
            split_str = list(s1)
            split_str[diff[0]], split_str[diff[1]] = split_str[diff[1]], split_str[diff[0]]
            if ''.join(split_str) == s2:
                print(int(count/2))
            else:
                print(0)
        else:
            print(0)