class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ptr1 = 0
        ptr2 = k-1
        max_avg = 0
        if len(nums) <= k:
            max_avg = sum(nums)/len(nums)
            return max_avg
        else:
            int_sum = sum(nums[ptr1:ptr2+1])
            while ptr2 < len(nums):
                avg = int_sum / k
                if avg > 0 and avg > max_avg:
                    max_avg = avg
                #This logic shouldn't work, but negative numbers are for some reason treated as > 0 and this works
                elif avg < 0:
                    if max_avg == 0:
                        max_avg = avg
                    elif avg > max_avg:
                        max_avg = avg
                
                int_sum -= nums[ptr1]
                ptr1 += 1
                ptr2 += 1
                if ptr2 < len(nums):
                    int_sum += nums[ptr2]

        return max_avg
