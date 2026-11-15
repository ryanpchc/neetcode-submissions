class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        ctr = 1
        longest = 1

        for i in range(1, len(nums)):
            j = i - 1
            if sorted_nums[i] == sorted_nums[j] + 1:
                ctr += 1
            elif sorted_nums[i] == sorted_nums[j]:
                continue
            else:
                ctr = 1
            longest = max(longest, ctr)
        return longest

        