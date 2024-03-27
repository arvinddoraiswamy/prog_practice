from collections import OrderedDict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Tried with an inbuilt sorting function on a list
        nums.sort()

        #Tried sorting a dictionary and copying it back but that's not much improvement either
        #numdict = defaultdict(int)
        #for i in nums:
        #    numdict[i] += 1
        #nums = []
        #for k1,v1 in sorted(numdict.items()):
        #    for times in range(0,v1):
        #        nums.append(k1)
      
        ptr1 = 0
        ptr2 = len(nums) - 1
        ops = 0
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
