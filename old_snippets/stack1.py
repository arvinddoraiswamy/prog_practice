# T = int(input())
# for t in range(0, T):
#     N = int(input())
#     final = []
#     match = 0
#     values = [int(x) for x in input().split(' ') if x != '']
#     for count, val in enumerate(values):
#         ic = count + 1
#         match = 0
#         while ic < N:
#             if val < values[ic]:
#                 match = 1
#                 break
#             else:
#                 ic += 1
#
#         if match == 1:
#             final.append(str(values[ic]))
#         else:
#             final.append(str(-1))
#
#     print(' '.join(final))

T = int(input())
for t in range(0, T):
    N = int(input())
    values = [int(x) for x in input().split(' ') if x != '']
    final = []
    for count, val in enumerate(values):
        st_val = [val]
        match = 0
        ic = count + 1
        k = st_val.pop()
        while ic < N:
            if k < values[ic]:
                match = 1
                break
            else:
                ic += 1

        if match == 1:
            final.append(str(values[ic]))
        else:
            final.append(str(-1))

    print(' '.join(final))