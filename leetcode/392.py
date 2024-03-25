class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        if not s or s == t:
            return True

        for j in range(0, len(t)):
            if s[i] == t[j]:
                i += 1
        
            if i == len(s):
                return True
        
        return False
