class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        ctr = 1
        longest = 1

        # Find start of sequence
        for num in num_set:
            if num - 1 in num_set:
                continue
                
            ctr = 1
            # Increment counter while consecutive elements exist
            while num + 1 in num_set:
                ctr += 1
                num += 1

            # Update longest streak and return
            longest = max(longest, ctr)
        return longest
        
