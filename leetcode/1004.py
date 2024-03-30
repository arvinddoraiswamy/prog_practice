class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        ptr2 = 0
        current = zeros = ones = max_ones = 0
        for ptr2 in range(0, len(nums)):
            if nums[ptr2] == 1:
                ones += 1
            elif (nums[ptr2] == 0 and zeros < k):
                zeros += 1
            else:
                print("max reached. move ptr1")
                current = ones + zeros
                if nums[ptr1] == 0:
                    zeros -= 1
                else:
                    ones -= 1
                ptr1 += 1
                zeros += 1
                
                if current > max_ones:
                    max_ones = current
                current = 0
            print(f"Ptr1: {ptr1}, Ptr2: {ptr2}, Ones: {ones}, Zeros: {zeros}, Max: {max_ones}")
    
        print(f"Last: {ones} {zeros}")
        current = ones+zeros
        if current > max_ones:
            max_ones = current

        return max_ones
