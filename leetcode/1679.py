# This was an unsorted array, so it took a long time to sort it which reduced performance. If we can find a better way to sort it, or use 2 pointers on an 
# unsorted list, this could be quicker.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        ptr2 = len(nums) - 1
        ops = 0
        nums.sort()
        while ptr1 < ptr2:
            sum = nums[ptr1] + nums[ptr2]
            if sum == k:
                ops += 1
                nums.pop(ptr1)
                ptr2 -= 1
                nums.pop(ptr2)
                ptr2 -= 1
            elif sum < k:
                ptr1 += 1
            elif sum > k:
                ptr2 -= 1
        
        return ops
