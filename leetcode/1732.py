class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = max_altitudes = 0

        for i in range(0, len(gain)):
            altitudes += gain[i]
            if altitudes > max_altitudes:
                max_altitudes = altitudes
        
        return max_altitudes
