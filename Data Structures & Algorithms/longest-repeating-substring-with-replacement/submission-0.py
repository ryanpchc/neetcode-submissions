class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        first_char, l = s[0], 0
        char1_count, char2_count = 0, 0
        max_count = 0

        while l < len(s):
            if s[l] == first_char:
                char1_count += 1
            else:
                char2_count += 1
            l += 1
        
        max_count = max(char1_count, char2_count)
        return max_count + k
