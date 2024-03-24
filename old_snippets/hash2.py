"""
Tried 3 different solutions but they all exceed time. Not sure what to do now.
* Substring needs 2 loops for sure
* Need to optimize inner loop even quicker but how?
"""


from collections import Counter
import sys

T = int(input())
for t in range(0, T):
    value = input()
    #counter = Counter(value)
    zc = value.count('0')
    oc = value.count('1')
    #l1 = list(value)
    #print(l1)
    #print(zc, oc)
    maxlen = 0

    # print("Value is", value, len(value))
    # print('-' * 10)
    if zc == oc:
        print(len(value))
        continue
    else:
        done = {}
        match = 0
        count = len(value)
        i = 0
        #print(count)

        while count > 0:
            i = 0
            while i + count <= len(value):
                s1 = value[i:i+count]
                if s1 not in done.keys():
                    i += 1
                    zc = s1.count('0')
                    oc = s1.count('1')
                    if zc == oc:
                        match = 1
                        break
                    #print(s1)
                else:
                    i += 1
            count -= 1

            if match == 1:
                print(zc + oc)
                #print("Match", s1)
                break
            #print('-' * 10)

        # for i in range(len(value), 0, -1):
        #     s1 = ''
        #     done = 0
        #     j = 0
        #     for j in range(0, len(value)):
        #         if (j + i) <= len(value):
        #             s1 = value[j:j+i]
        #             # print(s1)
        #             # c2 = Counter(s1)
        #             zc1 = s1.count('0')
        #             oc1 = s1.count('1')
        #
        #             if zc1 == oc1 and (zc1 + oc1) > maxlen:
        #                 maxlen = zc1 + oc1
        #                 # print("match")
        #                 # print(s1, zc1, oc1)
        #                 # print(maxlen)
        #                 done = 1
        #                 break
        #         else:
        #             break
        #
        #     if done == 1:
        #         print(maxlen)
        #     # print('-' * 10)
        #
        #     #sys.exit(0)

    # else:
    #     for i in range(0, len(value)):
    #         s1 = value[i:i + maxlen]
    #         j = i + maxlen
    #         for j in range(i + maxlen, len(value)):
    #             s1 += value[j:j+1]
    #             c2 = Counter(s1)
    #             zc1 = c2['0']
    #             oc1 = c2['1']
    #
    #             if zc1 == oc1 and (zc1 + oc1) > maxlen:
    #                 maxlen = zc1 + oc1
    #                 # print("match")
    #                 # print(s1, zc1, oc1)
    #                 # print(maxlen)
    #
    #         # print('-' * 10)
