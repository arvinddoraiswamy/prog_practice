# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring/0

T = int(input())

for t in range(0, T):
    s = list(input())
    length = len(s)
    k = int(input())
    storedlen = 0
    maxlen = 0

    for i in range(0, length):
        if k <= len(s):
            ss = s[i:i+k]
            sjs = ''.join(ss)
            lss = len(set(ss))
            j = i+k
            while lss <= k:
                maxlen = len(sjs)
                if j < length:
                    sjs = sjs + s[j]
                    lss = len(set(sjs))
                    j+=1
                else:
                    break

            if maxlen > storedlen:
                storedlen = maxlen
            else:
                continue
        else:
            storedlen = -1
            break

    print(storedlen)