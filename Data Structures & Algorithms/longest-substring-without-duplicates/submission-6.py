class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, longest = 0, 0

        for r in range(len(s)):
            # if duplicate char found
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # add char to set + update longest
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest