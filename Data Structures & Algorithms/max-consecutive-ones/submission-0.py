class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        consecutive_streak = 0

        for num in nums:
            if num == 1:
                consecutive_streak += 1

                if consecutive_streak > max_streak:
                    max_streak = consecutive_streak
            else:
                consecutive_streak = 0
        
        return max_streak
