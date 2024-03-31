class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = right = 0
        for index, num in enumerate(nums):
            if index == 0:
                left=0
                right=total-num
            elif index == len(nums)-1:
                left=total-num
                right=0
            else:
                right -= num
            
            if left == right:
                return index
            left += num
        
        return -1
