class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l, longest = 0, 0
        replacements_needed = 0
        
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            # check window validity 
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            # update longest
            longest = max(longest, r - l + 1)
        
        return longest



