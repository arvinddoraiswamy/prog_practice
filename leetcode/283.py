class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        orig_len = len(nums)
        ptr2 = orig_len
        count = 0

        while count < orig_len:
            if nums[ptr1] == 0:
                nums.append(nums[ptr2])
                nums.pop(ptr1)
            else:
                ptr1 += 1
            count += 1
