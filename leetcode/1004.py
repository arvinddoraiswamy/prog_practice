class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        ptr2 = 0
        zc = max_ones = 0
        while ptr2 < len(nums):
            if nums[ptr2] == 1:
                ptr2 += 1
            elif nums[ptr2] == 0:
                if zc < k:
                    zc += 1
                    ptr2 += 1
                else:
                    # Reached max contiguous length possible
                    while nums[ptr1] == 1:
                        ptr1 += 1
                    #The moment you hit a zero you're decreasing and increasing zc by 1, and moving ptr2
                    #Effectively hence, zc -1 + 1 = zc. So just move ptr2 to the right by 1
                    #Also it's a new start, so we have to reset our current count
                    current = 0
                    ptr1 += 1
                    ptr2 += 1

            current = ptr2 - ptr1
            if current > max_ones:
                max_ones = current
        
        return max_ones
