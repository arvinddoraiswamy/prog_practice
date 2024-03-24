# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def main():
    lines = []
    no_of_tests = int(input())
    no_of_lines = 2 * no_of_tests
    lines.append(no_of_tests)

    for line in range(0, no_of_lines):
        lines.append(input())

    # No of test cases
    T = int(lines[0])

    test_count = 0
    line_count = 1
        
    # Iterate over test cases
    while (test_count < T):

        #Get metadata about test
        N,S = lines[line_count].split(' ')
        N = int(N)
        S = int(S)
        line_count += 1

        #Actual test data

        data = lines[line_count].split(' ')
        data = [int(x) for x in data if x != '']

        # Doing the actual test here
        match = 0
        for i in range(0, N):
            sum = data[i]
            if sum == S:
                print(i+1, i+1)
                match=1
                break
            elif sum > S:
                i += 1
            else:
                for j in range(i+1, N):
                    sum += data[j]
                    if sum == S:
                        print(i+1, j+1)
                        match=1
                        break
                    elif sum > S:
                        i += 1
                        break
                    else:
                        j += 1

            if match == 1:
                break

        line_count += 1
        test_count += 1


        if match == 0:
            print(-1)

main()
