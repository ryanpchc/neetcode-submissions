class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l, replacements_needed = 0, 0
        
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

        most_frequent_count = max(counts.values())
        replacements_needed = len(s) - most_frequent_count

        if replacements_needed == 0:
            return most_frequent_count
        else:
            return most_frequent_count + k