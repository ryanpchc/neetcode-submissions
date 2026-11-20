class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, longest = 0, 0

        # iterate over the string
        for r in range(len(s)):
            # sliding window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # add element to set
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest

