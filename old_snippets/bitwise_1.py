# https://practice.geeksforgeeks.org/problems/element-left-after-performing-alternate-or-xor-operation/0
"""
TODO:
* Too slow. I think it's because I'm making a copy of the list, but unsure how to avoid it
* Cut out the XOR loop fully and rewrote code but it's still too slow :/. Not sure how to avoid a list copy
"""

T = int(input())
for t in range(0, T):
    n = int(input())
    elements = [int(x) for x in input().split(' ') if x != '']
    q = int(input())
    for nq in range(0, q):
        index, value = [int(x) for x in input().split(' ') if x != '']
        if 0 <= index < n:
            elements[index] = value
        else:
            print(-1)
            continue
        #print(elements)
        l1 = elements[:]
        #print(l1)
        n1 = n
        #print(n1)
        count = 1

        while n1 >= 2:
            if len(l1) == 2:
                l1.append(l1[0] | l1[1])
                del(l1[0:2])
                n1 = int(n1 / 2)
                count += 1
            else:
                for i in range(0, n1, 4):
                    l1.append((l1[i] | l1[i+1]) ^ (l1[i+2] | l1[i+3]))
                    #print(l1, n1)
                    #print('----')
                i = 0
                del (l1[i:i + n1])
                n1 = int(n1 / 4)
                count += 1
            #print("end of loop", l1, n1, count)
            #sys.exit(0)

        print(l1[0])

"""
        # OLD LOOP with 2 passes over the list
        while n1 >= 2:
            if count % 2 == 1:
                # Do OR stuff
                for i in range(0, n1, 2):
                    l1.append(l1[i] | l1[i+1])
         #       print("Or", l1)
            else:
                # Do XOR stuff
                for i in range(0, n1, 2):
                    l1.append(l1[i] ^ l1[i+1])
         #       print("XOR", l1)
            i = 0
            del (l1[i:i + n1])
            n1 = int(n1 / 2)
            count += 1
         #   print("end of loop", l1, n1, count)
 """
        #print('-' * 10)
        #print(l1[0])
