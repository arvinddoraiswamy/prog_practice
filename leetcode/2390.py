import string
class Solution:
    def removeStars(self, s: str) -> str:
        l2 = []
        i = 0
        while i < len(s):
            if s[i] == '*':
                l2.pop()
            else:
                l2.append(s[i])
            i += 1
        
        return ''.join(l2)
