class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest, l = 0, 0

        for r in range(len(s)):
            # remove repeating chars
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # add new elements
            seen.add(s[r]) # a
            longest = max(longest, r - l + 1)
            
        return longest
