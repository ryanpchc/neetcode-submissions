class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = low + high // 2

        while low <= high:
            mid = (low + high) // 2

            if target < nums[mid]:
                high = mid - 1

            if target > nums[mid]:
                low = mid + 1
            
            if target == nums[mid]:
                return mid

        return -1