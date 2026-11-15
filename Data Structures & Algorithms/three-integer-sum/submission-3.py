class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        triplets = []

        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    if [nums[i], nums[j], nums[k]] in triplets:
                        j += 1
                        k -= 1
                    else:
                        triplets.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1

                if three_sum < 0:
                    j += 1
                
                if three_sum > 0:
                    k -= 1
        
        return triplets