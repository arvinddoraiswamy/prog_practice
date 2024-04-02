class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ptr1 = ptr2 = nice = odd = 0
        while ptr2 < len(nums):
            if odd < k:
                if nums[ptr2] % 2 == 1:
                    odd += 1
            if odd == k:
                prevptr1 = ptr1
                while nums[ptr1] % 2 == 0:
                    print(f"ptr1, {ptr1}, ptr2, {ptr2}")
                    nice += 1
                    ptr1 += 1
                if nums[ptr1] != 0:
                    nice += 1
                    print(f"ptr1, {ptr1}, ptr2, {ptr2}")
                ptr1 = prevptr1
            ptr2 += 1
                
        return nice
