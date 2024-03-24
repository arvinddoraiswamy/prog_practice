T = int(input())
for t in range(0, T):
    N = int(input())
    values = [int(x) for x in input().split(' ') if x != '']

    height = values[0]
    width = 1
    max_size = []
    for i in range(0, N):
        width = 1
        height = values[i]
        size = height * width
        for j in range(i + 1, N):
            width += 1
            if height > values[j]:
                height = values[j]
            else:
                pass
            cur_size = height * width
            if cur_size > size:
                size = cur_size
        #print("size", size)
        max_size.append(size)
    print(max(max_size))