class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zc = max_ones = current = 0
        ptr1 = ptr2 = 0
        while ptr2 < len(nums):
            if nums[ptr2] == 1:
                ptr2 += 1
            elif nums[ptr2] == 0:
                if zc < 1:
                    zc += 1
                    ptr2 += 1
                else:
                    while nums[ptr1] == 1:
                        ptr1 += 1

                    # You decrement zc once ptr1 hits the first zero, but also append a new zero
                    # So in effect, you don't need to play with zc at all
                    ptr1 += 1
                    ptr2 += 1
            
            current = ptr2 - ptr1 - 1       
            if current > max_ones:
                max_ones = current

        return max_ones
