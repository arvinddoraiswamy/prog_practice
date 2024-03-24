# https://practice.geeksforgeeks.org/problems/jumping-numbers/0

T = int(input())

for t in range(0, T):
    total = []
    num = int(input())

    if num < 10:
        total = [str(x) for x in range(0, num+1)]
    elif 1 > num > 100000:
        continue
    else:
        total = [str(x) for x in range(0, 10)]
        maxnum = str(num)[:-1]

        for i in range(1, int(maxnum)+1):
            s1 = s2 = ''
            si = str(i)

            if si in total:
                last = int(str(i)[-1])
                if last < 9:
                    t1 = str(last + 1)
                    s1 = si + t1
                    total.append(str(s1))
                if last > 0:
                    t2 = str(last - 1)
                    s2 = si + t2
                    total.append(str(s2))
            else:
                continue

        total.sort()

        # Everything after this is so weird - need all this just to sort things :/
        d1 = {}
        for val in total:
            x = val[0]
            if x not in d1:
                d1[x] = val + ':'
            else:
                d1[x] += val
                d1[x] += ':'

        l2 = []
        for k1, v1 in sorted(d1.items()):
            l1 = sorted(v1[:-1].split(':'), key=len)
            l2.append(' '.join(l1))

        print(' '.join(l2))

    """
    else:
        total = [str(x) for x in range(0, 11)]
        for i in range(11, num+1):
            s1 = list(str(i))
            m = 1
            for j in range(0, len(s1)-1):
                x = abs(int(s1[j]) - int(s1[j+1]))
                if x != 1:
                    m = 0
                    failed.append(i)
                    break

            if m == 1:
                total.append(str(i))
            else:
                continue

    sorted(total)
    print(' '.join(sorted(total)))
    """