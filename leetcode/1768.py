class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        append = ''
        merged = ''

        if l1 > l2:
            append = word1[l2:]
            flen = l2
        else:
            append = word2[l1:]
            flen = l1
        
        i = 0
        j = 0
        while j < flen:
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1
        
        merged += append
        return merged
