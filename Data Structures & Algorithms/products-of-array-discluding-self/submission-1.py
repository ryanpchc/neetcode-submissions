class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = []
        right = [1] * len(nums)
        product = 1

        # build leftmost product
        for i in range(len(nums)): # [1, 2, 4, 6] -> [1, 1, 2, 8]
            left.append(product)
            product *= nums[i]

        product = 1

        # build rightmost product
        for i in range(len(nums) - 1, -1, -1): # [1, 2, 4, 6] -> [48, 24, 6, 1]
            right[i] = product
            product *= nums[i]

        # return output
        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output
