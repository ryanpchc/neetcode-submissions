class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            key = nums[i]

            if key not in seen:
                seen[key] = 1
            else:
                return True
        return False
