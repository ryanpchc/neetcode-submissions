class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in smap:
                return [smap[difference], i]
            else:
                smap[nums[i]] = i