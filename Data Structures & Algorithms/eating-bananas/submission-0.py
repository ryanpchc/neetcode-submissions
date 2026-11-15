class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) # eating speeds
        hours = 0

        while low <= high:
            mid = (low + high) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours > h:
                low = mid + 1
            else:
                high = mid - 1

        return low