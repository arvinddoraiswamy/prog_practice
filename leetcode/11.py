# Fancy 2 pointer solution which I have no clue why it works except my blindly following hints
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Init two pointers now with 1 ptr at each end of the array
        ptr1 = 0
        ptr2 = len(height) - 1

        #Store max area per "iteration"
        max_area = 0

        #Program ends when ptr1 == ptr2
        while ptr1 != ptr2:
            width = ptr2 - ptr1
            ht = min(height[ptr1], height[ptr2])
            area = width * ht
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
            
            if area > max_area:
                max_area = area

        return max_area

# original O(n^2) solution from which I could not move
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
