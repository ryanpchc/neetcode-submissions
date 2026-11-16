class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # track lowest and highest speeds to eat bananas
        low, high = 1, max(piles)
        
        # continue iterating until minimum integer k is found
        while low <= high:
            hours = 0
            mid = (low + high) // 2

            # calculate hours taken for each eating speed
            for pile in piles:
                hours += (mid + pile - 1) // mid

            # compare hours with parameter h
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1

        return low
            