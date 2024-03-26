class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        max_area = 0
        while ptr1 != ptr2:
            for i in range(ptr2, ptr1, -1):
                width = i - ptr1
                ht = min(height[i], height[ptr1])
                area = ht * width
                print(f"i: {i}, ptr1: {ptr1}, Width {width}, Height {ht}, Area {area}")
                if area > max_area:
                    max_area = area
            print(f"Max Area: {max_area}")
            ptr1 += 1
        
        return max_area
