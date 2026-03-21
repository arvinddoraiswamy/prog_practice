class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [None] * 2 * len(nums)
        # i = 0
        # while i<len(nums):
        #     ans[i] = nums[i]
        #     ans[i+len(nums)] = nums[i]
        #     i += 1
        ans = []
        ans.extend(nums)
        ans.extend(nums)
        return ans
