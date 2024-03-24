# https://practice.geeksforgeeks.org/viewSol.php?subId=8725383&pid=583&user=PranjalVerma1

def find(arr, n):
    stack, ans = [0], [-1] * n
    print(arr)

    for i in range(1, n):
        print(i, arr[stack[-1]], arr[i])
        while stack and arr[stack[-1]] >= arr[i]:
            print("In stack")
            print(arr[stack[-1]], arr[i])
            stack.pop()

        if stack:
            ans[i] = arr[stack[-1]]
        stack.append(i)
        print("Ans", ans)
        print("Stack", stack)
        print('-' * 10)

    print(' '.join(map(str, ans)))


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    find(arr, n)