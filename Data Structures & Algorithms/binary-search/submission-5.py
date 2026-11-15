class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = low + high // 2

        while low < mid:
            mid = (low + high) // 2

            if target < nums[mid]:
                high = mid

            if target > nums[mid]:
                low = mid
            
            if target == nums[mid]:
                return mid

        return -1