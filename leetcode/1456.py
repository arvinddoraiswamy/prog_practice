class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ptr1 = 0
        ptr2 = k-1
        cur_vowels = max_vowels = 0

        # Iterate till the end of the window reaches the end of the string
        while ptr2 < len(s):
            # Find no of vowels only for first iteration. After that you don't need to recompute each time
            if ptr1 == 0:
                window = s[ptr1:ptr2+1] #Array slicing syntax to get first k elements
                for ch in window:
                    if ch in vowels:
                        cur_vowels += 1
            # For all other iterations except the 1st one
            elif ptr1 > 0:
                # Check if the new character is a vowel
                if window[k-1] in vowels:
                    cur_vowels += 1
            
            # Set max number of vowels accordingly
            if cur_vowels > max_vowels:
                max_vowels = cur_vowels
            
            # If the OLD first char was a vowel we have to decrease count by 1 so we don't double count
            if window[0] in vowels:
                cur_vowels -= 1

            # Move the pointers to get the new window
            ptr1 += 1
            ptr2 += 1
            
            # Add the next char to the window
            if ptr2 < len(s):
                window += s[ptr2]
                window = window[1:]
    
        return max_vowels
